# 03 — GDP, inflation, real values, rates and economic data

[Course map](README.md) · [Practicals](../02-practicals/README.md) · [Questions](../03-questions-and-answers/worked-questions.md#lesson-03)

```mermaid
flowchart LR
 N0["Nominal series"] --> N1["Price index and period"] --> N2["Real comparison"] --> N3["Release vintage"]
```

## On this page

- [The idea](#the-idea)
- [Work through it](#work-through-it)
- [Common mistakes and practical limits](#common-mistakes-and-practical-limits)

## The idea

**Analogy:** A nominal number uses today's ruler; a real comparison adjusts for changes in that ruler.

Nominal values use current prices; real comparisons adjust by a price index under a chosen base/method. GDP measures defined production, not every aspect of welfare or wealth. Stocks describe quantities at a point in time; flows describe quantities over an interval. Avoid comparing annual rates, monthly levels and cumulative totals as if they were the same unit.

Inflation is a rate of price-index change, not the index level. Falling inflation can still mean rising prices, only more slowly. Unemployment measures depend on the defined labour-force population and survey rules. Economic series can be revised, seasonally adjusted and released with delays.

For analytics, retain series definitions, units, seasonal adjustment, publication date and vintage. A backtest using today's revised history can introduce look-ahead information. International comparisons also need consistent currencies, prices, periods and population denominators.

## Work through it

Nominal income increases from 100 to 110 while a relevant price index rises from 100 to 105. The purchasing-power growth under that index is $1.10/1.05-1\approx4.76\%$, not exactly 5%.

If inflation falls from 8% to 4%, the price level still rises 4% over the defined comparison period; it has not returned to the earlier level.

## Common mistakes and practical limits

Do not equate GDP growth with equal benefits for all households. A lower rate does not necessarily mean a lower level. Data release dates matter whenever information is used for historical decisions.

---

[← Supply, demand, equilibrium, elasticity and market structure](lesson-02-markets-and-elasticity.md) · [Cash flows, discounting, NPV and financial statements →](lesson-04-cashflows-and-statements.md)
