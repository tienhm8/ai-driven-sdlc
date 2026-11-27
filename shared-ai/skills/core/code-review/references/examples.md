# Review examples

Illustrations of bug patterns, not project rules. Thresholds and layer model come from project docs.

## 1. PR description missing items

```text
Title: fix order
Body: fix order creation bug
```

Return it without reading the code:

```text
Not enough information to review. Fill in per the PR template:
- Which Task and acceptance criterion? How is the bug reproduced?
- Behavior change or refactor only?
- Does it touch schema, API, job, or cache?
- How was it tested (command and result)?
```

## 2. Wrong placement

```ts
router.post('/orders', async (req, res) => {
  let total = req.body.subtotal;
  if (req.user.isVip && total > 1_000_000) total *= 0.9;
  await db.order.create({ data: { ...req.body, total } });
});
```

```text
[Medium] orders/handler.ts:24
The VIP discount rule lives in the handler, so other order-creation flows (import, mobile API)
will not apply it or must copy it. Move it to the business layer.
```

The `...req.body` spread is a separate security finding (section 5).

## 3. Concurrency

```python
product = Product.objects.get(id=pid)
if product.stock >= qty:
    product.stock -= qty
    product.save()
```

```text
[High] inventory/services.py:41
Scenario: stock = 1 and two requests buy 1 at the same time. Both read 1, both pass the check,
stock becomes 0 but 2 are sold.
Fix direction: a conditional update (UPDATE ... SET stock = stock - :qty WHERE id = :id AND stock >= :qty,
then check the affected row count), or a row lock or optimistic locking per the project's mechanism.
```

An event queued inside the transaction:

```text
[High] OrderService:88
The confirmation job is queued before commit. The worker may run first and not find the order;
on rollback the customer still gets the email. Emit after commit (hook or outbox).
```

## 4. Performance

```ts
for (const o of await repo.find()) { console.log((await o.customer).name) }
```

```text
[Medium] reports/OrderReport:15
One order query plus N customer queries; with 10,000 orders that is 10,001 queries, and the whole table
is loaded into memory. Eager load the relation and process in batches.
Raise to High if this is a hot path with a performance requirement.
```

## 5. Security

| Pattern | Example | Fix direction |
|---|---|---|
| Mass assignment | `create({ ...req.body })`, binding a request straight to an entity | Accept only validated fields (DTO with a whitelist) |
| IDOR | `findById(id)` from the URL with no ownership check | Scope the query to the user, or check per-record authorization |
| SQL injection | `` `SELECT ... ${id}` `` | Parameterized queries |
| XSS | `dangerouslySetInnerHTML` with user data | Escape by default; sanitize if HTML is needed |
| Sensitive field exposure | Returning the raw entity as JSON | A serializer or DTO |

```text
[Critical] orders/handler.ts:27
create({ ...req.body }) lets the client send "status":"paid", "total":0 and create a paid order priced 0.
Use a DTO that declares only the allowed fields. Touches money: trigger a security review.
```

## 6. Sample report

```text
PR #142 · Task SHOP-31 · High risk (touches money)
Understanding: adds a VIP discount on order creation; behavior change; touches the orders table; no API change.
PR description: missing rollback.

Critical
1. orders/handler.ts:27 mass assignment
High
2. InventoryService:41 negative stock on concurrent purchase
3. No test for AC-SHOP-31-02 (an order of exactly 1,000,000)
Medium
4. orders/handler.ts:24 discount rule in the handler
Questions
- BR-ORD-07: is the 1,000,000 threshold before or after tax?
Good points
- Migration has a down step; regression test for the old rounding bug.
Not applicable: operability (no new job or config).
Not reviewed: mobile client.

Recommendation: Request Changes (1 Critical, 2 High). Gate G4 pending a human reviewer.
```
