# Business Scenario Calculator
## Purpose
This academic analytical model simulates and visualizes business performance under three scenarios — **Base**, **Optimistic**, and **Pessimistic** — for the 2023–2024 period.
It measures revenue, operating expenses, profitability, and margin variations to demonstrate how scenario modeling can support data-driven decision-making.

## Structure
Sheets:
- Calculations - core dataset and formulas containing monthly data for all revenue and expense categories by scenario.
- Summary - interactive dashboard displaying aggregated results and visuals for the selected scenario.

## Core Logic
Each scenario (Base / Optimistic / Pessimistic) is calculated independently in Calculations with its own adjustment parameters.
The Summary sheet dynamically aggregates results via the scenario dropdown using SUMIF() formulas.

**Key computations**:
- Revenue = Fees + Interest + Other
- OPEX = Salaries + Operations + Marketing + IT + Other
- EBITDA = Revenue − OPEX
- Tax = EBITDA × 17%
- Net Income = EBITDA − Tax
- Margin (%) = Net Income ÷ Revenue

## Visual Components
The dashboard contains three primary visualizations:
- Revenue vs OPEX — comparison of total revenue and operating expenses by scenario.
- Net Income by Scenario — comparative view of profitability across scenarios.
- Net Income per Month — monthly trend of profitability over the full period.

## Interaction

- Scenario selector (dropdown) automatically recalculates Summary metrics and visuals.
- Charts update dynamically based on the selected scenario.
- All figures are sourced from Calculations; no manual edits required.

## Analytical Output
The model highlights:
- Structural differences in cost and revenue composition.
- Scenario-driven variations in EBITDA and Net Income.
- Seasonality of profit performance over time.

## Implementation Notes
Fully compatible with Google Sheets and Microsoft Excel.
No macros, add-ins, or scripts required.
Developed for educational and analytical demonstration purposes — not intended for corporate FP&A or investment reporting.
