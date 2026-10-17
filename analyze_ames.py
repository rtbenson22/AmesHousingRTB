"""Descriptive statistics and correlation analysis for selected Ames variables."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


DATA_FILE = Path("AmesHousingclean.csv")
OUTPUT_DIR = Path("ames_analysis")
PREDICTORS = ["Gr Liv Area", "Overall Qual", "Total Bsmt SF", "Year Built"]
RESPONSE = "SalePrice"
VARIABLES = PREDICTORS + [RESPONSE]

OUTPUT_DIR.mkdir(exist_ok=True)
data = pd.read_csv(DATA_FILE)
analysis = data[VARIABLES].apply(pd.to_numeric, errors="raise")

# Descriptive statistics and Pearson correlation tables.
summary = analysis.describe().T
summary.to_csv(OUTPUT_DIR / "descriptive_statistics.csv")
correlations = analysis.corr(method="pearson")
correlations.to_csv(OUTPUT_DIR / "pearson_correlations.csv")

# Format the tables for convenient review in the console.
print("Descriptive statistics:")
print(summary.round(2).to_string())
print("\nPearson correlation matrix:")
print(correlations.round(3).to_string())
print("\nPredictor correlations with SalePrice:")
print(correlations[RESPONSE].drop(RESPONSE).sort_values(ascending=False).round(3).to_string())

sns.set_theme(style="whitegrid")

# Correlation heatmap.
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(
    correlations,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    center=0,
    vmin=-1,
    vmax=1,
    square=True,
    ax=ax,
)
ax.set_title("Pearson Correlations: Ames Housing Variables")
fig.tight_layout()
fig.savefig(OUTPUT_DIR / "correlation_heatmap.png", dpi=200)
plt.close(fig)

# Predictor versus response scatterplots with fitted linear trend lines.
fig, axes = plt.subplots(2, 2, figsize=(12, 9))
for predictor, ax in zip(PREDICTORS, axes.flat):
    sns.regplot(
        data=analysis,
        x=predictor,
        y=RESPONSE,
        scatter_kws={"alpha": 0.35, "s": 18},
        line_kws={"color": "crimson"},
        ax=ax,
    )
    ax.set_title(f"{predictor} vs. {RESPONSE}")
    ax.set_xlabel(predictor)
    ax.set_ylabel("Sale price")
fig.suptitle("Selected Predictors and Sale Price", y=1.02)
fig.tight_layout()
fig.savefig(OUTPUT_DIR / "predictor_scatterplots.png", dpi=200, bbox_inches="tight")
plt.close(fig)

print(f"\nSaved tables and charts in: {OUTPUT_DIR.resolve()}")
