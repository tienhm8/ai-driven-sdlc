"""Connect the cost ledger to managed attempts without enabling any transport."""
from collections.abc import Callable, Mapping
from pathlib import Path
from types import MappingProxyType

from .ai_budget import BudgetError, BudgetLedger
from .budget_usage import identifier
from .managed_model import Attempt


class LedgerAttemptBudget:
    def __init__(self, ledger: BudgetLedger, *, workspaces: tuple[Path, ...] = (),
                 policies: Mapping[str, Callable[[Attempt], str | None]]):
        self.ledger = ledger
        self.policies = MappingProxyType({identifier(key, "budget policy"): quote for key, quote in policies.items()})
        if any(not callable(quote) for quote in self.policies.values()):
            raise BudgetError("BUDGET_POLICY_INVALID", "Budget quote policies must be callable")
        if any(ledger.path.resolve().is_relative_to(root.resolve()) for root in workspaces):
            raise BudgetError("BUDGET_STATE_UNSAFE", "Budget state must be outside registered checkouts")

    def reserve(self, attempt: Attempt) -> str:
        if attempt.project != self.ledger.project:
            raise BudgetError("BUDGET_PROJECT_MISMATCH", "Budget ledger belongs to another Project Instance")
        quote = self.policies.get(attempt.budget_policy)
        if quote is None:
            raise BudgetError("BUDGET_POLICY_UNKNOWN", "Configure an approved quote policy for this attempt")
        amount = quote(attempt)
        if amount is None:
            raise BudgetError("BUDGET_QUOTE_MISSING", "No cost projection for this attempt")
        request = attempt.request
        return self.ledger.reserve(request.work_item_id, amount, run_id=attempt.run_id, attempt=attempt.number,
                                   repo=request.repo, stage=request.stage, task=request.task, tool=attempt.route.tool)

    def settle(self, reservation: str, *, usage: dict | None = None, not_dispatched: bool = False,
               budget_cutoff: bool = False) -> str:
        return self.ledger.settle(reservation, usage=usage, not_dispatched=not_dispatched, budget_cutoff=budget_cutoff)
