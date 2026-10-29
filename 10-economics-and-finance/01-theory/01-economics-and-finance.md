# Economics and finance: understand the quantities before modelling

[Subject home](../README.md) · [Theory index](README.md)

Economics studies choices under scarcity. Financial data adds prices, returns, cash flows and risk. These concepts help explain a business problem, but a correlation or backtest alone does not establish a causal or profitable strategy.


## On this page

- [1. Scarcity, opportunity cost and incentives](#1-scarcity-opportunity-cost-and-incentives)
- [2. Demand, supply and elasticity](#2-demand-supply-and-elasticity)
- [3. Macroeconomic measurement](#3-macroeconomic-measurement)
- [4. Prices, returns and compounding](#4-prices-returns-and-compounding)
- [5. Risk and the mean-reversion practical](#5-risk-and-the-mean-reversion-practical)

## 1. Scarcity, opportunity cost and incentives

Resources have alternative uses. Opportunity cost is the value of the best forgone alternative. A team assigning one engineer to a dashboard may delay another project; the salary alone does not express that trade-off. Marginal analysis asks what changes from one additional unit, rather than comparing only totals.

Microeconomics studies individual markets and agents; macroeconomics studies aggregate output, prices, employment and related quantities. Models simplify assumptions to clarify a mechanism; ask which assumptions matter in the case you are analysing.

```mermaid
flowchart LR
 A["Limited resources"] --> B["Alternative uses"] --> C["Opportunity cost"] --> D["Decision at the margin"] --> E["Observed response and constraints"]
```

## 2. Demand, supply and elasticity

A demand curve relates quantity demanded to price with other conditions held fixed; a supply curve relates quantity supplied. A price change moves along a curve; a change in income, input costs or other conditions can shift a curve. Their intersection is a model of market equilibrium, not a guarantee that every real market clears instantly.

Price elasticity is a proportional quantity response divided by a proportional price change under a stated definition. For a small illustrative change from price 100 to 110 and quantity 200 to 180, using the initial base gives $(−20/200)/(10/100)=−1$. A midpoint definition gives a different finite-change number; state the convention. Sales and price moving together in observational data do not by themselves identify a causal demand curve.

## 3. Macroeconomic measurement

GDP measures production of final goods/services within an economy over a period. Distinguish stocks from flows, nominal from real quantities, and levels from growth rates. Inflation is the change in a price index under its measurement definition. A higher nominal revenue can reflect higher prices rather than greater volume.

Keep units, frequency and revisions consistent when joining economic series. A quarterly observation should not be treated as a fresh independent daily measurement just because it was forward-filled. For forecasting, use information available on the actual release date, including revision policy.

## 4. Prices, returns and compounding

Simple return is $r_t=P_t/P_{t-1}-1$ when prices are comparable and the chosen series accounts for required adjustments. Log return is $\log(P_t/P_{t-1})$ for positive prices. Log returns add over time; simple returns compound as $\prod_t(1+r_t)-1$.

A 10% gain followed by a 10% loss produces $1.1\times0.9-1=-1\%$, not zero. A return series and a price series have different properties. Include dividends, splits, fees and the exact instrument definition where relevant.

## 5. Risk and the mean-reversion practical

Volatility describes variation; drawdown measures a drop from a previous peak. Correlation between asset returns can change across periods and regimes. A backtest must define transaction timing, signal construction, fees, slippage, data quality and the selection process.

A mean-reversion signal compares a value with a reference level, often a rolling mean and spread. It assumes deviations may reverse; that assumption can fail during regime shifts. Calculate the signal with past data, then shift the trade decision so an unavailable closing value is not used to trade at that same earlier close. Inspect the existing Python notebook as a learning experiment. No result in this subject is a prediction or investment recommendation.


[Try the practicals](../02-practicals/README.md)
