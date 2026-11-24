from datetime import date
import json
from pathlib import Path
import sqlite3

ROOT = Path(__file__).resolve().parent
AS_OF = date(2026, 11, 23)
APPROVED = "Return Approved"


def process_return(db, order_id, as_of):
    trace = [{"step": "Planning", "action": "Find order → check eligibility → update → verify"}]
    with db:
        order = db.execute("SELECT delivered_on, status FROM orders WHERE id = ?", (order_id,)).fetchone()
        trace.append({"step": "Tool Use", "action": "Look up order", "found": order is not None})
        if order is None:
            return {"order_id": order_id, "outcome": "Order not found", "trace": trace}

        delivered_on, status = order
        age_days = (as_of - date.fromisoformat(delivered_on)).days
        trace.append({"step": "Eligibility", "days_since_delivery": age_days})
        if not 0 <= age_days <= 30:
            return {"order_id": order_id, "outcome": "Outside 30-day window", "trace": trace}
        if status == APPROVED:
            return {"order_id": order_id, "outcome": "Already approved", "trace": trace}

        update = db.execute(
            "UPDATE orders SET status = ? WHERE id = ? AND status = ?", (APPROVED, order_id, status)
        )
        trace.append({"step": "Tool Use", "action": "Update order status", "rows_changed": update.rowcount})
        observed = db.execute("SELECT status FROM orders WHERE id = ?", (order_id,)).fetchone()
        if update.rowcount != 1 or observed != (APPROVED,):
            raise RuntimeError(f"Approval could not be verified for order {order_id}")
        trace.append({"step": "Reflection", "verified_status": observed[0]})

    return {"order_id": order_id, "outcome": APPROVED, "trace": trace}


def main():
    with sqlite3.connect(":memory:") as db:
        db.execute("CREATE TABLE orders (id INTEGER PRIMARY KEY, delivered_on TEXT, status TEXT)")
        db.executemany("INSERT INTO orders VALUES (?, ?, ?)", [
            (5821, "2026-11-10", "Delivered"),
            (5822, "2026-10-24", "Delivered"),
            (5823, "2026-10-23", "Delivered"),
        ])
        db.commit()
        cases = [(5821, APPROVED), (5822, APPROVED), (5823, "Outside 30-day window"),
                 (9999, "Order not found"), (5821, "Already approved")]
        results = []
        for order_id, expected in cases:
            result = process_return(db, order_id, AS_OF)
            assert result["outcome"] == expected, result
            results.append(result)
        statuses = dict(db.execute("SELECT id, status FROM orders"))
        assert statuses == {5821: APPROVED, 5822: APPROVED, 5823: "Delivered"}

    report = {
        "engine": "SQLite with parameterized SQL and deterministic Python orchestration",
        "data": "Synthetic workshop scenario. Return window measured from delivery in this reproduction.",
        "as_of": AS_OF.isoformat(), "shipping_labels_sent": 0, "cases": results,
        "final_statuses": statuses,
    }
    output = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    path = ROOT / "results" / "customer-return-local.json"
    path.parent.mkdir(exist_ok=True)
    path.write_text(output, encoding="utf-8")
    print(output, end="")


if __name__ == "__main__":
    main()
