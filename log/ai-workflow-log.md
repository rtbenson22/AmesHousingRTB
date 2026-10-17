# AI Workflow Log Ames Housing Analysis
# This log provides a Record of prompts and outputs from my Codex session on 10-17-2026. 
# The log was initially generate using Codex and then reviewd and annotated by RTB. 
# The current entry uses the local system time.

## 2026-10-17 — 10:09 AM, 
**Prompt:** 
- “load AmesHousing.csv and provide information on rows,columns, variables, and dimensions”

**Codex produced:** 
- Inspected `AmesHousing.csv` and reported 2,930 rows, 82 columns (2,930 × 82), and listed all variable names.

**Accepted / Modified**
- Accepted the output and results 

**Rejected**
- None

**Rationale**
- Results provided the dataset information expected from csv file before cleaning. 

**Codex produced:** 
**Accepted / Modified**
**Rejected**
**Rationale**

## 2026-10-17 — 10:32 AM
**Prompt:** 
- “Load AmesHousing.csv and clean data for analysis. check for missing and null values, saved the cleaned dataset in AmesHousingclean.csv. Provide infomration on rows, columns, variables, and dimensions of cleaned dataset. provide python code for this work.”

**Codex produced:** 
- Created `AmesHousingclean.csv` and reusable `clean_ames.py`. Found 719 blank cells across 21 columns; filled numeric gaps with column medians and text gaps with `Unknown`, while preserving literal `NA` values used to indicate absent home features. Reported the cleaned dataset as 2,930 rows × 82 columns, with no remaining nulls.

**Accepted / Modified**
- Accepted the cleaned database. 

**Rejected**
- None 

**Rationale**
- Scanned clean file for anomalies.
- Codex note recorded the source had 719 blank cells across 21 columns.The cleaning script fills numeric gaps with each column’s median and text gaps with "Unknown". It preserves literal "NA" values because those indicate absent features in this dataset, such as no alley or pool.
 


## 2026-10-17 — 10:44 AM
**Prompt:** 
- “Load AmesHousingclean.csv and perform descriptive statistics and correlation analysis. use the predictors GrLivArea, OverallQual, TotalBsmtSF, and YearBuilt, with SalesPrice being the response variable. Create summary tables and charts. provide python code for this work.”

**Codex produced:** 
- Created `analyze_ames.py` and the `ames_analysis/` output folder with descriptive statistics, Pearson correlation tables, a correlation heatmap, and predictor scatterplots. Used the dataset headers `Gr Liv Area` and `SalePrice`. Reported their correlations with sale price: Overall Qual 0.799, Gr Liv Area 0.707, Total Bsmt SF 0.632, Year Built 0.558.
- Codex produced descriptive_statistics.csv, pearson_correlations.csv, correlation_heatmap.png, and predictor_scatterplots.png files for seperate analysis. 

**Accepted / Modified**
- Accepted the Descriptive statistics table values and Pearson correlation. 
- Accepted correlation heatmap, descriptive statistics spreadsheet, pearson correlations spreadsheet, and four predictor scatterplots.

**Rejected**
- None

**Rationale**
- Compared output results to selected descriptive statistics information from team project. All the information aligned with selected manual code check work.



## 2026-10-17 — 10:59 AM

**Prompt:** 
- “Load AmesHousingclean.csv and perform multiple linear regression. use the predictors GrLivArea, OverallQual, TotalBsmtSF, and YearBuilt, with SalesPrice being the response variable. provide the R-squared,Adj. R-squared, AIC, BIC. provide an interpretaion of results. check for correlation issues, save results in a file, provide python code for this work.”

**Codex produced:** 
- Created `regression_ames.py` and `ames_regression/` outputs: OLS summary, model metrics, predictor correlation matrix, and VIF diagnostics. For 2,930 observations, reported R² = 0.7786, adjusted R² = 0.7783, AIC = 70,056.03, and BIC = 70,085.94. VIFs ranged from 1.518 to 2.381, interpreted as no severe multicollinearity by common rules of thumb.

**Accepted / Modified**
- Accepted model summary and diagnostics. 
- Accepted interpretation of results.

**Rejected**
- None

**Rationale**
- Investigated difference in results from from previous project work see session log around 16:53 PM
- Different cleaning methods can produce small offset in results. 


## 2026-10-17 — 11:12 AM

**Prompt:** 
- “Create a visual chart of the regression results. save with the regression files. provide python code for this work.”

**Codex produced**
- Updated `regression_ames.py` to save `ames_regression/observed_vs_predicted.png`, showing observed versus predicted sale prices with a perfect-prediction reference line and model R².
- Codex produced a Observed Sale Price vs Predicted Sale Price chart. 

**Accepted / Modified**
- Accepted the plot visualization 

**Rejected**
- None

**Rationale**
- The plot indicated the relationship between actual and predicted sale prices vs a perfect  prediction line. 


## 2026-10-17 11:57:47 -04:00 (America/New_York)

**Prompt:** 
- “create a /log/ai-workflow-log.md: capture per-prompt entries noting the date and time, and what Codex produced. Place in a log file for future editing”

**Codex produced:** 
- Created this editable Markdown log. The date for earlier prompts is recorded from the session environment; their exact times were unavailable in the conversation history.

**Accepted / Modified**
- Accepted log created

**Rejected**
- None

**Rationale**
- Provided a seed file for manual documentation of work flow.



## Querry differences 
## 2026-10-17 - 16:53 PM
**Prompt:** 
- "I have a previous model on the same data set and variable that gave different results. R-squared: 0.815 Adj. R-squared:0.815 AIC: 6.929e+04 BIC:                         6.932e+04 

**Codex produced:** 
- The results differ because they cannot come from the same rows, variables, and ordinary least squares setup. For a fixed dataset and model, OLS produces one set of coefficients and fit statistics.
I checked the five model columns in your cleaned file. They have 2,930 rows and no missing values. To make a direct comparison, check that both runs use the same 2,930 rows, the same five columns (Gr Liv Area, Overall Qual, Total Bsmt SF, Year Built, and SalePrice), and an intercept with no transformations or row filters.

## 2026-10-17  6:55 PM
**Prompt:** 
- "df[["OverallQual", "GrLivArea", "TotalBsmtSF", "YearBuilt", "SalePrice]]  model = smf.ols('SalePrice ~ GrLivArea + OverallQual + TotalBsmtSF + YearBuilt', data=df).fit()"

**Codex produced:**
-"That formula is statistically equivalent to the model I fit: statsmodels formula syntax includes an intercept by default, as did my sm.OLS model. So if df contains the same rows and values, both approaches should give the same results."

## 2026-10-17 -  6:56 PM PM
**Prompt:** 
-"df = pd.read_csv("../data/AmesHousing_clean.csv")  Rows: 2924, Columns: 82"
**Codex produced:** 
That likely explains the difference: your file has 2,924 rows, while the file I analyzed has 2,930. If the six omitted homes have unusual prices or predictor values, excluding them could shift the coefficients and fit statistics—especially if they are outliers.



