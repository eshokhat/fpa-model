# dataset generation
import numpy as np
import pandas as pd

np.random.seed(42)

months = pd.date_range("2023-01-01", periods=24, freq="M")

rows = []
for m in months:
    # revenue (basic)
    revenue_fees      = np.random.randint(800_000, 1_200_000)
    revenue_interest  = np.random.randint(500_000,   900_000)
    revenue_other     = np.random.randint(100_000,   200_000)
    # expences (basic)
    expense_salaries   = np.random.randint(400_000, 600_000)
    expense_operations = np.random.randint(200_000, 400_000)
    expense_marketing  = np.random.randint(100_000, 300_000)
    expense_it         = np.random.randint(150_000, 250_000)
    expense_other      = np.random.randint(50_000,  100_000)

    rows.append({
        "month": m.strftime("%Y-%m"),
        "revenue_fees":      revenue_fees,
        "revenue_interest":  revenue_interest,
        "revenue_other":     revenue_other,
        "expense_salaries":   expense_salaries,
        "expense_operations": expense_operations,
        "expense_marketing":  expense_marketing,
        "expense_it":         expense_it,
        "expense_other":      expense_other
    })

df = pd.DataFrame(rows)
df.to_csv("dataset.csv", index=False)
print("Saved dataset.csv", df.shape)

