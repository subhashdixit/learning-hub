# 06 — Backtesting, costs, leakage, selection bias and model risk

[Course map](README.md) · [Practicals](../02-practicals/README.md) · [Questions](../03-questions-and-answers/worked-questions.md#lesson-06)

```mermaid
flowchart LR
 N0["Historical information cutoff"] --> N1["Signal"] --> N2["Execution and costs"] --> N3["Temporal evaluation"] --> N4["Robustness"]
```

## On this page

- [The idea](#the-idea)
- [Work through it](#work-through-it)
- [Common mistakes and practical limits](#common-mistakes-and-practical-limits)

## The idea

**Analogy:** A backtest is a simulation with an information budget, not a certificate of future profit.

Define the decision timestamp, available data, universe, execution assumptions, transaction costs and evaluation procedure before computing performance. Use historical constituents/availability to avoid survivorship bias. Apply the proper publication delay to features and keep training/tuning separate from later evaluation.

Costs include spread, fees, slippage, financing and market impact where relevant. A signal at the closing price may not be executable at that same price after observing it. Repeated strategy searches select lucky histories; report the search process, robustness and untouched temporal results rather than only the best curve.

Stress assumptions, inspect turnover/exposure, compare benchmarks and account for liquidity/capacity. A model can fail because the relationship changed, the data were revised, a trade could not execute or its own activity changes the market. Paper results remain conditional simulations. The purpose here is learning sound measurement, not recommending trades.

## Work through it

A strategy makes an illustrative 10 basis points gross per turnover unit but costs 12 basis points under a realistic cost model. Net is−2 basis points before other effects. Ignoring a small-looking cost changes the sign.

A feature containing a firm's later-restated earnings should not be used as if it were known on the original decision date.

## Common mistakes and practical limits

Do not report only the winner after thousands of trials. A chronological split can still leak revised/future features. Avoid representing simulated gains as realized or guaranteed returns.

---

[← Compounding, volatility, drawdown, diversification and factor ideas](lesson-05-returns-and-risk.md) · [Continue with practicals](../02-practicals/README.md)
