"""
Primetrade.ai — Bitcoin Market Sentiment vs Trader Performance Analysis
Author: Deep Kumar
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

# ── Style ──────────────────────────────────────────────────────────────────────
plt.rcParams.update({
    'figure.facecolor': '#0d1117',
    'axes.facecolor':   '#161b22',
    'axes.edgecolor':   '#30363d',
    'axes.labelcolor':  '#c9d1d9',
    'xtick.color':      '#8b949e',
    'ytick.color':      '#8b949e',
    'text.color':       '#c9d1d9',
    'grid.color':       '#21262d',
    'grid.linewidth':   0.6,
    'font.family':      'DejaVu Sans',
    'font.size':        11,
})

SENTIMENT_COLORS = {
    'Extreme Fear': '#f85149',
    'Fear':         '#ff7b72',
    'Neutral':      '#e3b341',
    'Greed':        '#56d364',
    'Extreme Greed':'#3fb950',
}
SENTIMENT_ORDER = ['Extreme Fear', 'Fear', 'Neutral', 'Greed', 'Extreme Greed']

# ── Load Data ──────────────────────────────────────────────────────────────────
print("Loading data...")
df = pd.read_csv('historical_data.csv')
fg = pd.read_csv('fear_greed_index.csv')

# ── Clean & Merge ──────────────────────────────────────────────────────────────
df['date'] = pd.to_datetime(df['Timestamp IST'], dayfirst=True).dt.date.astype(str)
fg['date'] = pd.to_datetime(fg['date']).dt.date.astype(str)

merged = df.merge(fg[['date', 'value', 'classification']], on='date', how='inner')
merged.rename(columns={'value': 'sentiment_score', 'classification': 'sentiment'}, inplace=True)
print(f"Merged rows: {len(merged):,}  |  Date range: {merged['date'].min()} → {merged['date'].max()}")

# ── Daily aggregates ───────────────────────────────────────────────────────────
daily = merged.groupby(['date', 'sentiment', 'sentiment_score']).agg(
    total_pnl    = ('Closed PnL', 'sum'),
    avg_pnl      = ('Closed PnL', 'mean'),
    trades       = ('Closed PnL', 'count'),
    win_trades   = ('Closed PnL', lambda x: (x > 0).sum()),
    vol_usd      = ('Size USD', 'sum'),
).reset_index()
daily['win_rate'] = daily['win_trades'] / daily['trades'] * 100

# ── Sentiment aggregates ───────────────────────────────────────────────────────
sent = merged.groupby('sentiment').agg(
    total_pnl  = ('Closed PnL', 'sum'),
    avg_pnl    = ('Closed PnL', 'mean'),
    trades     = ('Closed PnL', 'count'),
    win_trades = ('Closed PnL', lambda x: (x > 0).sum()),
    vol_usd    = ('Size USD', 'sum'),
).reset_index()
sent['win_rate'] = sent['win_trades'] / sent['trades'] * 100
sent = sent.set_index('sentiment').reindex(SENTIMENT_ORDER).reset_index()

# ── Account-level ──────────────────────────────────────────────────────────────
acct = merged.groupby('Account').agg(
    total_pnl  = ('Closed PnL', 'sum'),
    avg_pnl    = ('Closed PnL', 'mean'),
    trades     = ('Closed PnL', 'count'),
    win_trades = ('Closed PnL', lambda x: (x > 0).sum()),
).reset_index()
acct['win_rate'] = acct['win_trades'] / acct['trades'] * 100
acct['short_acct'] = acct['Account'].str[:8] + '...'


# ══════════════════════════════════════════════════════════════════════════════
# CHART 1 — Avg PnL by Sentiment
# ══════════════════════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(10, 5))
colors = [SENTIMENT_COLORS[s] for s in sent['sentiment']]
bars = ax.bar(sent['sentiment'], sent['avg_pnl'], color=colors, width=0.55, zorder=2)
ax.axhline(0, color='#8b949e', linewidth=0.8, linestyle='--')
ax.set_title('Average Trade PnL by Market Sentiment', fontsize=14, pad=12, color='#f0f6fc', fontweight='bold')
ax.set_xlabel('Market Sentiment')
ax.set_ylabel('Avg Closed PnL (USD)')
ax.yaxis.grid(True, zorder=0)
for bar, val in zip(bars, sent['avg_pnl']):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + (2 if val >= 0 else -6),
            f'${val:.1f}', ha='center', va='bottom', fontsize=10, color='#f0f6fc')
plt.tight_layout()
plt.savefig('charts/1_avg_pnl_by_sentiment.png', dpi=150, bbox_inches='tight')
plt.close()
print("Chart 1 saved")

# ══════════════════════════════════════════════════════════════════════════════
# CHART 2 — Win Rate by Sentiment
# ══════════════════════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(10, 5))
colors = [SENTIMENT_COLORS[s] for s in sent['sentiment']]
bars = ax.bar(sent['sentiment'], sent['win_rate'], color=colors, width=0.55, zorder=2)
ax.axhline(50, color='#8b949e', linewidth=0.8, linestyle='--', label='50% baseline')
ax.set_title('Win Rate (%) by Market Sentiment', fontsize=14, pad=12, color='#f0f6fc', fontweight='bold')
ax.set_xlabel('Market Sentiment')
ax.set_ylabel('Win Rate (%)')
ax.set_ylim(0, 80)
ax.yaxis.grid(True, zorder=0)
ax.legend(fontsize=10)
for bar, val in zip(bars, sent['win_rate']):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
            f'{val:.1f}%', ha='center', va='bottom', fontsize=10, color='#f0f6fc')
plt.tight_layout()
plt.savefig('charts/2_win_rate_by_sentiment.png', dpi=150, bbox_inches='tight')
plt.close()
print("Chart 2 saved")

# ══════════════════════════════════════════════════════════════════════════════
# CHART 3 — Trade Volume by Sentiment
# ══════════════════════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(10, 5))
colors = [SENTIMENT_COLORS[s] for s in sent['sentiment']]
bars = ax.bar(sent['sentiment'], sent['vol_usd'] / 1e6, color=colors, width=0.55, zorder=2)
ax.set_title('Total Trading Volume by Market Sentiment', fontsize=14, pad=12, color='#f0f6fc', fontweight='bold')
ax.set_xlabel('Market Sentiment')
ax.set_ylabel('Volume (USD Millions)')
ax.yaxis.grid(True, zorder=0)
for bar, val in zip(bars, sent['vol_usd'] / 1e6):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
            f'${val:.1f}M', ha='center', va='bottom', fontsize=10, color='#f0f6fc')
plt.tight_layout()
plt.savefig('charts/3_volume_by_sentiment.png', dpi=150, bbox_inches='tight')
plt.close()
print("Chart 3 saved")

# ══════════════════════════════════════════════════════════════════════════════
# CHART 4 — Sentiment Score vs Daily PnL (scatter)
# ══════════════════════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(10, 6))
for sent_label in SENTIMENT_ORDER:
    sub = daily[daily['sentiment'] == sent_label]
    ax.scatter(sub['sentiment_score'], sub['total_pnl'], 
               color=SENTIMENT_COLORS[sent_label], alpha=0.7, s=40, label=sent_label)

# Regression line
slope, intercept, r, p, _ = stats.linregress(daily['sentiment_score'], daily['total_pnl'])
x_line = np.linspace(daily['sentiment_score'].min(), daily['sentiment_score'].max(), 100)
ax.plot(x_line, slope * x_line + intercept, color='#58a6ff', linewidth=1.5, linestyle='--', label=f'Trend (r={r:.2f})')
ax.set_title('Fear & Greed Index Score vs Daily Total PnL', fontsize=14, pad=12, color='#f0f6fc', fontweight='bold')
ax.set_xlabel('Fear & Greed Score (0=Extreme Fear, 100=Extreme Greed)')
ax.set_ylabel('Daily Total PnL (USD)')
ax.axhline(0, color='#8b949e', linewidth=0.6, linestyle=':')
ax.legend(fontsize=9, framealpha=0.3)
ax.yaxis.grid(True, zorder=0)
plt.tight_layout()
plt.savefig('charts/4_sentiment_vs_pnl_scatter.png', dpi=150, bbox_inches='tight')
plt.close()
print("Chart 4 saved")

# ══════════════════════════════════════════════════════════════════════════════
# CHART 5 — PnL Distribution per Sentiment (box plot)
# ══════════════════════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(11, 6))
data_groups = [merged[merged['sentiment'] == s]['Closed PnL'].clip(-500, 500) for s in SENTIMENT_ORDER]
bp = ax.boxplot(data_groups, patch_artist=True, notch=False,
                medianprops=dict(color='#f0f6fc', linewidth=2),
                whiskerprops=dict(color='#8b949e'),
                capprops=dict(color='#8b949e'),
                flierprops=dict(marker='.', markersize=2, alpha=0.3))
for patch, sent_label in zip(bp['boxes'], SENTIMENT_ORDER):
    patch.set_facecolor(SENTIMENT_COLORS[sent_label])
    patch.set_alpha(0.8)
ax.set_xticks(range(1, 6))
ax.set_xticklabels(SENTIMENT_ORDER)
ax.axhline(0, color='#8b949e', linewidth=0.8, linestyle='--')
ax.set_title('PnL Distribution per Sentiment (clipped ±$500)', fontsize=14, pad=12, color='#f0f6fc', fontweight='bold')
ax.set_ylabel('Closed PnL (USD)')
ax.yaxis.grid(True, zorder=0)
plt.tight_layout()
plt.savefig('charts/5_pnl_distribution_boxplot.png', dpi=150, bbox_inches='tight')
plt.close()
print("Chart 5 saved")

# ══════════════════════════════════════════════════════════════════════════════
# CHART 6 — Top 10 Traders by Total PnL
# ══════════════════════════════════════════════════════════════════════════════
top10 = acct.nlargest(10, 'total_pnl')
fig, ax = plt.subplots(figsize=(10, 6))
colors_bar = ['#3fb950' if v > 0 else '#f85149' for v in top10['total_pnl']]
ax.barh(top10['short_acct'], top10['total_pnl'], color=colors_bar, zorder=2)
ax.set_title('Top 10 Traders by Total PnL', fontsize=14, pad=12, color='#f0f6fc', fontweight='bold')
ax.set_xlabel('Total Closed PnL (USD)')
ax.xaxis.grid(True, zorder=0)
ax.axvline(0, color='#8b949e', linewidth=0.8)
plt.tight_layout()
plt.savefig('charts/6_top_traders.png', dpi=150, bbox_inches='tight')
plt.close()
print("Chart 6 saved")

# ══════════════════════════════════════════════════════════════════════════════
# CHART 7 — Heatmap: Coin × Sentiment avg PnL
# ══════════════════════════════════════════════════════════════════════════════
top_coins = merged.groupby('Coin')['Closed PnL'].count().nlargest(12).index
heat_data = merged[merged['Coin'].isin(top_coins)].groupby(['Coin', 'sentiment'])['Closed PnL'].mean().unstack()
heat_data = heat_data.reindex(columns=SENTIMENT_ORDER)

fig, ax = plt.subplots(figsize=(12, 7))
sns.heatmap(heat_data, ax=ax, cmap='RdYlGn', center=0, fmt='.0f', annot=True,
            linewidths=0.4, linecolor='#0d1117',
            cbar_kws={'label': 'Avg PnL (USD)'})
ax.set_title('Avg PnL by Coin × Market Sentiment (Top 12 Coins)', fontsize=14, pad=12, color='#f0f6fc', fontweight='bold')
ax.set_xlabel('Market Sentiment')
ax.set_ylabel('Coin')
plt.tight_layout()
plt.savefig('charts/7_coin_sentiment_heatmap.png', dpi=150, bbox_inches='tight')
plt.close()
print("Chart 7 saved")

# ══════════════════════════════════════════════════════════════════════════════
# CHART 8 — Buy vs Sell PnL under each sentiment
# ══════════════════════════════════════════════════════════════════════════════
side_sent = merged.groupby(['sentiment', 'Side'])['Closed PnL'].mean().unstack().reindex(SENTIMENT_ORDER)
fig, ax = plt.subplots(figsize=(10, 5))
x = np.arange(len(SENTIMENT_ORDER))
w = 0.35
bars1 = ax.bar(x - w/2, side_sent.get('BUY', 0), w, label='BUY', color='#3fb950', zorder=2)
bars2 = ax.bar(x + w/2, side_sent.get('SELL', 0), w, label='SELL', color='#f85149', zorder=2)
ax.set_xticks(x)
ax.set_xticklabels(SENTIMENT_ORDER)
ax.axhline(0, color='#8b949e', linewidth=0.8, linestyle='--')
ax.set_title('Avg PnL: Buy vs Sell by Sentiment', fontsize=14, pad=12, color='#f0f6fc', fontweight='bold')
ax.set_ylabel('Avg Closed PnL (USD)')
ax.legend()
ax.yaxis.grid(True, zorder=0)
plt.tight_layout()
plt.savefig('charts/8_buy_vs_sell_sentiment.png', dpi=150, bbox_inches='tight')
plt.close()
print("Chart 8 saved")

# ══════════════════════════════════════════════════════════════════════════════
# Print key stats for report
# ══════════════════════════════════════════════════════════════════════════════
print("\n── KEY STATS ──")
print(sent[['sentiment','avg_pnl','win_rate','trades']].to_string(index=False))
print(f"\nCorrelation (sentiment score vs daily total PnL): r={r:.3f}, p={p:.4f}")
print(f"Total trades analyzed: {len(merged):,}")
print(f"Total PnL across all trades: ${merged['Closed PnL'].sum():,.2f}")
print(f"Overall win rate: {(merged['Closed PnL'] > 0).mean()*100:.1f}%")
print("\nAll charts saved to charts/")
