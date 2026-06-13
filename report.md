# Primetrade.ai — Trader Performance vs Market Sentiment Analysis

**Author:** Deep Kumar  
**Dataset:** Hyperliquid Historical Trades + Bitcoin Fear & Greed Index  
**Period:** May 2023 – May 2025  
**Total Trades Analyzed:** 211,218  

---

## 1. Executive Summary

This analysis explores how Bitcoin market sentiment (Fear & Greed Index) influences trader performance on Hyperliquid. Across 211,218 trades over two years, several clear patterns emerge:

- **Extreme Greed** produces the highest average PnL ($67.89/trade) and highest win rate (46.5%)
- **Fear periods** still generate healthy profits ($54.29/trade avg) — traders adapt
- **Extreme Fear** surprisingly delivers $34.54/trade avg — but with the lowest win rate (37%), suggesting a few large wins skew the average
- Overall platform PnL: **$10.25 million** across all analyzed trades
- Overall win rate: **41.1%** — slightly below 50%, consistent with leveraged crypto markets

---

## 2. Dataset Overview

| Dataset | Rows | Columns | Period |
|---|---|---|---|
| Hyperliquid Trader Data | 211,224 | 16 | Dec 2023 – May 2025 |
| Fear & Greed Index | 2,644 | 4 | Feb 2018 – May 2025 |
| **Merged (analysis set)** | **211,218** | **18** | **May 2023 – May 2025** |

**Key columns used:** Account, Coin, Execution Price, Size USD, Side, Closed PnL, Timestamp IST, Fear/Greed Score, Sentiment Classification

---

## 3. Sentiment Distribution in Trades

| Sentiment | Trades | % of Total |
|---|---|---|
| Fear | 61,837 | 29.3% |
| Greed | 50,303 | 23.8% |
| Neutral | 37,686 | 17.8% |
| Extreme Greed | 39,992 | 18.9% |
| Extreme Fear | 21,400 | 10.1% |

Most trades occurred during **Fear** periods — consistent with high crypto volatility driving activity.

---

## 4. Key Findings

### 4.1 Avg PnL by Sentiment

| Sentiment | Avg PnL (USD) | Win Rate | Total Trades |
|---|---|---|---|
| Extreme Fear | $34.54 | 37.1% | 21,400 |
| Fear | $54.29 | 42.1% | 61,837 |
| Neutral | $34.31 | 39.7% | 37,686 |
| Greed | $42.74 | 38.5% | 50,303 |
| Extreme Greed | **$67.89** | **46.5%** | 39,992 |

> **Insight:** Extreme Greed is clearly the best environment for traders — both higher average returns and highest win rates. The "buy the greed" contrarian hypothesis does NOT hold here; greedy markets reward participation.

### 4.2 Correlation Analysis

- Pearson correlation between Fear/Greed score and daily total PnL: **r = -0.083** (p = 0.07)
- The weak negative correlation suggests sentiment alone is **not a strong linear predictor** of daily profits
- However, categorical analysis (above) reveals non-linear patterns — Extreme Greed is an outlier

### 4.3 Buy vs Sell Performance

- **BUY trades** consistently outperform **SELL trades** across all sentiment categories
- This is expected in a bull-trending market (2023–2025 Bitcoin cycle)
- SELL trades perform best during Extreme Fear — suggesting short-sellers capitalize on crash conditions

### 4.4 Coin-Level Patterns (Top 12 Coins)

From the heatmap analysis:
- **BTC and ETH** show more consistent PnL across all sentiment conditions
- **Altcoins** show higher variance — large positive PnL in Greed, but deeper losses in Fear
- Some coins show negative avg PnL in Extreme Fear but positive in Greed, confirming sentiment-dependent behavior

### 4.5 Trader Performance Distribution

- 32 unique traders in the dataset
- Top performers concentrate gains during Greed and Extreme Greed periods
- Win rate distribution: most traders cluster between 35–55% win rate
- A few high-volume traders drive most of the total PnL

---

## 5. Trading Strategy Recommendations

### Strategy 1: Greed-Momentum Strategy
**Signal:** Fear & Greed score > 70 (Extreme Greed)  
**Action:** Increase position sizing on BUY side  
**Rationale:** Highest avg PnL ($67.89) and win rate (46.5%) observed in this regime  

### Strategy 2: Fear-Accumulation Strategy
**Signal:** Fear & Greed score < 30 (Fear / Extreme Fear)  
**Action:** Accumulate long positions on high-conviction coins (BTC, ETH)  
**Rationale:** Fear periods drive overselling; recovery bounces generate outsized returns  

### Strategy 3: Avoid Neutral / Sideways Markets
**Signal:** Fear & Greed score 40–60 (Neutral)  
**Action:** Reduce position sizes, tighten stop-losses  
**Rationale:** Lowest avg PnL ($34.31) and mediocre win rates — choppy conditions  

### Strategy 4: Short Only in Extreme Fear
**Signal:** Fear & Greed score < 20  
**Action:** SELL/SHORT positions only in confirmed downtrends  
**Rationale:** SELL trades perform best in Extreme Fear — the one scenario where shorts are rewarded  

---

## 6. Visualizations

| Chart | Description |
|---|---|
| `1_avg_pnl_by_sentiment.png` | Average trade PnL across 5 sentiment categories |
| `2_win_rate_by_sentiment.png` | Win rate % by sentiment |
| `3_volume_by_sentiment.png` | Total trading volume by sentiment |
| `4_sentiment_vs_pnl_scatter.png` | Scatter: Fear/Greed score vs daily PnL with regression |
| `5_pnl_distribution_boxplot.png` | PnL distribution box plots per sentiment |
| `6_top_traders.png` | Top 10 traders by total PnL |
| `7_coin_sentiment_heatmap.png` | Heatmap: avg PnL by Coin × Sentiment |
| `8_buy_vs_sell_sentiment.png` | Buy vs Sell avg PnL across sentiments |

---

## 7. Conclusion

Market sentiment measurably influences trader outcomes on Hyperliquid. While the linear correlation is weak, the categorical patterns are actionable:

1. **Trade more aggressively in Greed/Extreme Greed** — best risk-reward
2. **Use Fear as a buying opportunity** — avg PnL is still strongly positive
3. **Avoid or reduce exposure in Neutral markets** — worst outcomes
4. **BUY side dominates in bull markets** — align direction with macro trend

The data spans a primarily bullish Bitcoin cycle (2023–2025), so these insights should be re-evaluated during prolonged bear markets.

---

*Analysis conducted using Python (Pandas, NumPy, Matplotlib, Seaborn, SciPy)*
