"""Strict, metadata-only ingestion and exact money arithmetic for the AI ledger."""
from datetime import date, datetime, timezone
from decimal import Decimal, ROUND_CEILING, localcontext
import re


BASES = ("billed", "reported", "estimated", "unmeasured")
RANK = {basis: i for i, basis in enumerate(reversed(BASES))}
TOKEN_FIELDS = ("input", "output", "cache_read", "cache_write")
KEY = re.compile(r"[A-Za-z0-9][A-Za-z0-9._:/@+-]{0,127}")
ITEM = re.compile(r"[A-Za-z0-9][A-Za-z0-9_-]{0,127}")
MONEY = re.compile(r"(?:0|[1-9][0-9]{0,8})(?:\.[0-9]{1,12})?")
SCALE = 1_000_000
MAX_MICROS = 999_999_999 * SCALE


class BudgetError(ValueError):
    def __init__(self, code: str, message: str):
        self.code = code
        super().__init__(message)


def invalid(message):
    return BudgetError("INVALID_BUDGET_INPUT", message)


def identifier(value, label, *, pattern=KEY):
    if not isinstance(value, str) or not pattern.fullmatch(value):
        raise invalid(f"Invalid {label}")
    return value


def note(value, label):
    if not isinstance(value, str) or not value.strip() or len(value) > 500 or not value.isprintable():
        raise invalid(f"{label} must be a short printable audit summary")
    return value.strip()


def decimal_amount(value, *, label="money"):
    if not isinstance(value, str) or not MONEY.fullmatch(value):
        raise invalid(f"{label} must be a nonnegative decimal string")
    return Decimal(value)


def usd_micros(value, *, positive=False):
    numeric = decimal_amount(value, label="USD amount")
    with localcontext() as context:
        context.prec = 60
        micros = numeric * SCALE
    if micros != micros.to_integral_value() or micros > MAX_MICROS or (positive and not micros):
        raise invalid("USD amount must fit in integer microdollars" + (" and be positive" if positive else ""))
    return int(micros)


def usd_text(micros):
    if micros is None:
        return None
    whole, fraction = divmod(abs(micros), SCALE)
    return f"{'-' if micros < 0 else ''}{whole}.{fraction:06d}"


def utc(value):
    if not isinstance(value, str) or len(value) > 40 or "T" not in value:
        raise invalid("observed_at must be an ISO UTC timestamp")
    try:
        parsed = datetime.fromisoformat(value.removesuffix("Z") + "+00:00" if value.endswith("Z") else value)
        if parsed.utcoffset() == timezone.utc.utcoffset(None):
            return parsed.astimezone(timezone.utc).isoformat()
    except ValueError:
        pass
    raise invalid("observed_at must be an ISO UTC timestamp")


def pricing_date(value):
    if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        raise invalid("price_effective_on must be an ISO date")
    try:
        return date.fromisoformat(value).isoformat()
    except ValueError:
        raise invalid("price_effective_on must be an ISO date") from None


_REQUIRED = {"work_item_id", "repo", "stage", "task", "run_id", "provider", "account", "session_id", "event_id",
             "unit", "observed_at", "status", "basis"}
_OPTIONAL = {"request_id", "model", "effort", "tool", "attempt", "charge", "amount", "currency", "fx_to_usd",
             "fx_source", "usage", "pricing", "price_source", "price_effective_on", "sequence"}


def normalize_usage(raw):
    if not isinstance(raw, dict) or not _REQUIRED <= raw.keys() or raw.keys() - _REQUIRED - _OPTIONAL:
        raise invalid("Usage requires the documented metadata fields only")
    fields = _REQUIRED - {"observed_at"}
    data = {field: identifier(raw[field], field, pattern=ITEM if field == "work_item_id" else KEY) for field in fields}
    data["observed_at"] = utc(raw["observed_at"])
    for field in ("request_id", "model", "effort", "tool", "price_source", "fx_source"):
        if field in raw:
            data[field] = identifier(raw[field], field)
    for field in ("attempt", "sequence"):
        if field in raw:
            if type(raw[field]) is not int or not 1 <= raw[field] <= 1_000_000_000:
                raise invalid(f"Invalid {field}")
            data[field] = raw[field]
    unit, basis = data["unit"], data["basis"]
    charge = raw.get("charge", "metered")
    if (unit not in ("request", "session") or basis not in BASES or charge not in ("metered", "seat")
            or (charge == "seat" and basis not in ("estimated", "unmeasured"))
            or (unit == "request" and "sequence" in data)
            or (unit == "session" and ("request_id" in data or "attempt" in data))):
        raise invalid("Invalid accounting unit, basis, charge type or sequence")
    data["charge"] = charge
    if "price_effective_on" in raw:
        data["price_effective_on"] = pricing_date(raw["price_effective_on"])
        if data["price_effective_on"] > data["observed_at"][:10]:
            raise invalid("Price date is after observed usage")
    if ("price_source" in data) != ("price_effective_on" in data):
        raise invalid("Price source and effective date must be provided together")
    usage = raw.get("usage", {})
    if not isinstance(usage, dict) or set(usage) - set(TOKEN_FIELDS):
        raise invalid("Invalid token usage fields")
    if any(type(value) is not int or not 0 <= value <= 1_000_000_000_000 for value in usage.values()):
        raise invalid("Token counts must be nonnegative integers")
    data["usage"] = usage
    currency = raw.get("currency", "USD")
    if not isinstance(currency, str) or not re.fullmatch(r"[A-Z]{3}", currency):
        raise invalid("Invalid currency")
    data["currency"] = currency
    with localcontext() as context:
        context.prec = 60
        fx = Decimal(1)
        if currency != "USD":
            fx = decimal_amount(raw.get("fx_to_usd"), label="USD exchange rate")
            if not fx or "fx_source" not in data:
                raise invalid("A positive USD exchange rate and its source are required")
            data["fx_to_usd"] = format(fx.normalize(), "f")
        elif {"fx_to_usd", "fx_source"} & raw.keys():
            raise invalid("USD records do not take an exchange rate")
        amount = None
        if basis in ("billed", "reported"):
            if "pricing" in raw:
                raise invalid("Billed/reported amounts do not take estimate rates")
            amount = decimal_amount(raw.get("amount"))
            data["amount"] = format(amount.normalize(), "f")
        elif basis == "estimated":
            if "amount" in raw or "price_source" not in data:
                raise invalid("An estimate requires versioned pricing, not an input amount")
            rates = raw.get("pricing")
            if not isinstance(rates, dict) or set(rates) - {*TOKEN_FIELDS, "fee"}:
                raise invalid("Invalid estimate rates")
            if set(rates) - {"fee"} != set(usage) or (not usage and "fee" not in rates):
                raise invalid("Every estimate token bucket needs a count and price; use zero explicitly")
            numeric = {k: decimal_amount(v, label=k) for k, v in rates.items()}
            data["pricing"] = {k: format(v.normalize(), "f") for k, v in numeric.items()}
            amount = sum((count * numeric[k] / SCALE for k, count in usage.items()), numeric.get("fee", Decimal(0)))
        elif {"pricing", "amount", "currency", "fx_source", "fx_to_usd"} & raw.keys():
            raise invalid("Unmeasured records must not contain a cost or exchange rate")
        micros = None if amount is None else int((amount * fx * SCALE).to_integral_value(rounding=ROUND_CEILING))
    if micros is not None and micros > MAX_MICROS:
        raise invalid("Usage cost exceeds the supported per-record range")
    return data, micros
