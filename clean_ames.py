"""Clean AmesHousing.csv and write AmesHousingclean.csv."""

from pathlib import Path

import pandas as pd


source = Path("AmesHousing.csv")
output = Path("AmesHousingclean.csv")

# Keep literal "NA" values: in this dataset they describe absent features
# (for example, no alley or no pool), rather than missing observations.
data = pd.read_csv(source, dtype=str, keep_default_na=False)

# Empty or whitespace-only cells are true missing values.
data = data.replace(r"^\s*$", pd.NA, regex=True)
missing_before = data.isna().sum()

# Convert columns that contain numeric values throughout to numeric dtype.
numeric_columns = []
for column in data.columns:
    converted = pd.to_numeric(data[column], errors="coerce")
    observed = data[column].notna()
    if observed.any() and converted[observed].notna().all():
        data[column] = converted
        numeric_columns.append(column)

# Fill numeric gaps with each column's median; use an explicit category for
# missing text values. Keep the source rows and columns intact.
for column in data.columns:
    if data[column].isna().any():
        if column in numeric_columns:
            data[column] = data[column].fillna(data[column].median())
        else:
            data[column] = data[column].fillna("Unknown")

data.to_csv(output, index=False)

print(f"Missing cells before cleaning: {int(missing_before.sum())}")
print("Missing cells by column before cleaning:")
print(missing_before[missing_before > 0].to_string())
print(f"Missing cells after cleaning: {int(data.isna().sum().sum())}")
print(f"Rows: {data.shape[0]}")
print(f"Columns: {data.shape[1]}")
print(f"Dimensions: {data.shape[0]} x {data.shape[1]}")
print("Variables:")
print(", ".join(data.columns))
