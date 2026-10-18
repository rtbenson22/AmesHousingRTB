# AmesHousingRTB
# Week 7 Codex CLI Hands-On

## Project Overview
This repository contains Week 7 Assignment for analysis of the AmesHousing
dataset. The project includes exploratory data analysis and multiple regression 
to predict `SalePrice` based on predictors GrLivArea, OverallQual, TotalBsmtSF, 
and YearBuilt . 

**Analytical Question**
How well do  GrLivArea, OverallQual, TotalBsmtSF, and YearBuilt  predict 
`SalePrice`    

** Codex Dates**: October 17,2026

**Analysis Overview and Findings**
The AmesHousing dataset was cleaned and the analyzed using Codex and Python.  
The resulting cleaned dataset has 2,930 rows and 82 columns (2,930 × 82), with 
82 variables. Descriptive statistics and correlation analysis were performed
for the four predictors  GrLivArea, OverallQual, TotalBsmtSF, and YearBuilt. 
All four predictors have positive correlations with sale price in this dataset. 
Overall Qual has the strongest correlation among them. A Multiple Linear 
Regression was performed to predict SalePrice. The model produced an  
R-squared 0.7786 which explains about 77.9% of the variation in sale prices. 
The predictor correlations range from 0.242 to 0.597. VIF values range from 
1.518 to 2.381, which does not indicate severe multicollinearity. A plot was also
produced comparing actual and predicted sale prices to help visualize the results. 

## Repository Structure
```
project-root/
├── AmesHousing.csv (provided dataset)
├── ames_analysis/   # Pyhton analysis and output
├── ames_regression/ # Pyhton analysis and output (charts, regression results, etc.)
├── README.md        # project description
├── prompts
└── log
```
*