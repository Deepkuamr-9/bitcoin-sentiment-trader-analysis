# 🚀 Bitcoin Market Sentiment vs Trader Performance Analysis

## 📌 Overview

This project explores the relationship between **Bitcoin Market Sentiment (Fear & Greed Index)** and **trader performance on Hyperliquid**. By combining market sentiment data with over **211,000 historical trades**, the analysis uncovers how trader behavior, profitability, and risk-taking vary across different market conditions.

The goal is to identify actionable insights that can support smarter trading decisions and sentiment-driven strategies.

---

## 🎯 Objectives

* Analyze trader profitability across market sentiment categories.
* Measure the impact of Fear and Greed on trading behavior.
* Evaluate win rates, trading volume, and leverage usage.
* Discover patterns between sentiment and trader performance.
* Generate data-driven recommendations for trading strategies.

---

## 📊 Dataset Information

### 1. Bitcoin Fear & Greed Index

| Column         | Description               |
| -------------- | ------------------------- |
| Date           | Trading Date              |
| Classification | Market Sentiment Category |

Sentiment Categories:

* Extreme Fear
* Fear
* Neutral
* Greed
* Extreme Greed

### 2. Hyperliquid Historical Trading Data

Key Fields:

* Account
* Symbol
* Execution Price
* Trade Size
* Side (Buy/Sell)
* Time
* Leverage
* ClosedPnL
* Event
* Position Information

---

## 🛠️ Technologies Used

### Programming

* Python

### Data Analysis

* Pandas
* NumPy
* SciPy

### Visualization

* Matplotlib
* Seaborn

### Development Tools

* Jupyter Notebook
* Visual Studio Code

---

## 📈 Analysis Performed

### Data Preparation

* Data cleaning
* Date formatting
* Missing value handling
* Dataset merging

### Exploratory Data Analysis

* Sentiment distribution
* Trade volume analysis
* Profitability trends
* Win-rate comparison

### Statistical Analysis

* Correlation analysis
* Sentiment impact assessment
* Trader performance evaluation

---

## 📉 Visualizations

The project generates the following charts:

1. Average PnL by Sentiment
2. Win Rate by Sentiment
3. Trading Volume by Sentiment
4. Sentiment vs PnL Scatter Plot
5. PnL Distribution Boxplot
6. Top Performing Traders
7. Coin Sentiment Heatmap
8. Buy vs Sell Analysis by Sentiment

Generated charts are automatically saved in the `charts/` directory.

---

## 🔍 Key Findings

### Trading Statistics

* Total Trades Analyzed: **211,218**
* Total Realized PnL: **$10,254,486.95**
* Overall Win Rate: **41.1%**

### Correlation Analysis

Correlation between sentiment score and daily profitability:

```text
r = -0.083
p = 0.0708
```

The results indicate a weak relationship between overall market sentiment and daily trading profitability.

### Behavioral Insights

* Trading activity increases during Greed periods.
* Extreme Fear periods generally show lower participation.
* Traders tend to take greater risks during optimistic market conditions.
* Profitability is influenced more by trader behavior than sentiment alone.

---

## 📂 Project Structure

```text
primetrade_analysis/
│
├── charts/
│   ├── 1_avg_pnl_by_sentiment.png
│   ├── 2_win_rate_by_sentiment.png
│   ├── 3_volume_by_sentiment.png
│   ├── 4_sentiment_vs_pnl_scatter.png
│   ├── 5_pnl_distribution_boxplot.png
│   ├── 6_top_traders.png
│   ├── 7_coin_sentiment_heatmap.png
│   └── 8_buy_vs_sell_sentiment.png
│
├── analysis.py
├── analysis_notebook.ipynb
├── fear_greed_index.csv
├── historical_data.csv
├── report.md
└── README.md
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/primetrade-analysis.git
cd primetrade-analysis
```

Install dependencies:

```bash
pip install pandas numpy matplotlib seaborn scipy
```

Run the analysis:

```bash
python analysis.py
```

---

## 📌 Future Enhancements

* Machine Learning-based profit prediction
* Trader segmentation and clustering
* Risk-adjusted performance metrics
* Time-series forecasting
* Sentiment-based strategy backtesting

---

## 👨‍💻 Author

**Deep Kumar**

Computer Science Graduate | Data Analyst | AI & Machine Learning Enthusiast

### Skills

* Python
* Data Analytics
* Machine Learning
* Deep Learning
* Data Visualization
* Business Intelligence

---

## ⭐ Conclusion

This project demonstrates practical expertise in:

* Data Cleaning
* Exploratory Data Analysis (EDA)
* Statistical Analysis
* Financial Data Analytics
* Data Visualization
* Market Sentiment Analysis
* Python Programming
* Insight Generation

The analysis highlights how trader performance changes across varying market sentiment conditions and provides valuable insights for data-driven trading strategies.
