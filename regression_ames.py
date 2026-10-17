"""Multiple linear regression for selected Ames housing variables."""

from pathlib import Path

import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor
import matplotlib.pyplot as plt


DATA_FILE = Path("AmesHousingclean.csv")
OUTPUT_DIR = Path("ames_regression")
PREDICTORS = ["Gr Liv Area", "Overall Qual", "Total Bsmt SF", "Year Built"]
RESPONSE = "SalePrice"

OUTPUT_DIR.mkdir(exist_ok=True)
data = pd.read_csv(DATA_FILE)
model_data = data[PREDICTORS + [RESPONSE]].apply(pd.to_numeric, errors="raise")

X = sm.add_constant(model_data[PREDICTORS])
y = model_data[RESPONSE]
model = sm.OLS(y, X).fit()
predictions = model.predict(X)

# Diagnose relationships among predictors.
correlations = model_data[PREDICTORS].corr(method="pearson")
vif_design = sm.add_constant(model_data[PREDICTORS])
vif = pd.DataFrame(
    {
        "Variable": PREDICTORS,
        "VIF": [
            variance_inflation_factor(vif_design.to_numpy(), i + 1)
            for i in range(len(PREDICTORS))
        ],
    }
)

metrics = pd.DataFrame(
    {
        "Metric": ["Observations", "R-squared", "Adjusted R-squared", "AIC", "BIC"],
        "Value": [len(model_data), model.rsquared, model.rsquared_adj, model.aic, model.bic],
    }
)

(OUTPUT_DIR / "ols_summary.txt").write_text(model.summary().as_text(), encoding="utf-8")
metrics.to_csv(OUTPUT_DIR / "model_metrics.csv", index=False)
correlations.to_csv(OUTPUT_DIR / "predictor_correlations.csv")
vif.to_csv(OUTPUT_DIR / "variance_inflation_factors.csv", index=False)

# Plot observed versus fitted sale prices with an ideal-prediction reference.
fig, ax = plt.subplots(figsize=(8, 7))
ax.scatter(y, predictions, alpha=0.35, s=20, color="#2878B5", edgecolors="none")
plot_min = min(y.min(), predictions.min())
plot_max = max(y.max(), predictions.max())
ax.plot([plot_min, plot_max], [plot_min, plot_max], linestyle="--", color="crimson", linewidth=2, label="Perfect prediction")
ax.set_xlim(plot_min, plot_max)
ax.set_ylim(plot_min, plot_max)
ax.set_xlabel("Observed SalePrice ($)")
ax.set_ylabel("Predicted SalePrice ($)")
ax.set_title(f"Observed vs. Predicted SalePrice\nOLS model ($R^2$ = {model.rsquared:.3f})")
ax.legend()
ax.grid(alpha=0.2)
fig.tight_layout()
fig.savefig(OUTPUT_DIR / "observed_vs_predicted.png", dpi=200)
plt.close(fig)

print("Model metrics:")
print(metrics.to_string(index=False, formatters={"Value": lambda v: f"{v:.4f}" if isinstance(v, float) else str(v)}))
print("\nOLS coefficients:")
print(model.params.to_string())
print("\nPredictor correlation matrix:")
print(correlations.round(3).to_string())
print("\nVariance inflation factors:")
print(vif.to_string(index=False, formatters={"VIF": "{:.3f}".format}))
print(f"\nSaved model summary and diagnostics in: {OUTPUT_DIR.resolve()}")
