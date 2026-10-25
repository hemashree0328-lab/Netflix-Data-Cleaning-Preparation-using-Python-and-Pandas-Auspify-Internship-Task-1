
import pandas as pd
from pathlib import Path

# 1. Locate the dataset in the same folder as this script
folder = Path(__file__).parent
input_file = folder / "Dataset.csv"
output_file = folder / "Netflix_Cleaned.csv"
report_file = folder / "cleaning_report.txt"

# 2. Import the dataset
if not input_file.exists():
    raise FileNotFoundError(
        f"Dataset not found: {input_file}\n"
        "Place Dataset.csv in the same folder as clean_netflix.py."
    )

df = pd.read_csv(input_file)

print("=" * 50)
print("AUSPIFY TASK 1: NETFLIX DATA CLEANING")
print("=" * 50)

print("\nOriginal dataset shape:", df.shape)

# Save the original data quality details
original_rows = len(df)
original_duplicates = int(df.duplicated().sum())
missing_before = df.isnull().sum()

# 3. Clean column names
df.columns = df.columns.str.strip().str.lower()

# 4. Remove leading/trailing spaces from text columns
for column in df.select_dtypes(include=["object"]).columns:
    df[column] = df[column].str.strip()

# Treat blank text cells as missing values
df = df.replace(r"^\s*$", pd.NA, regex=True)

# 5. Remove exact duplicate records
df = df.drop_duplicates()

# 6. Handle missing values carefully
# Fill missing text values with "Unknown"
text_columns = df.select_dtypes(include=["object"]).columns

for column in text_columns:
    df[column] = df[column].fillna("Unknown")

# Keep numeric missing values visible rather than inventing values
# 7. Standardize selected text columns
if "type" in df.columns:
    df["type"] = df["type"].str.title()

if "country" in df.columns:
    df["country"] = df["country"].str.replace(
        r"\s*,\s*", ", ", regex=True
    )

if "rating" in df.columns:
    df["rating"] = df["rating"].str.upper()

# 8. Convert date_added to a consistent date format
if "date_added" in df.columns:
    dates = pd.to_datetime(
        df["date_added"].replace("Unknown", pd.NA),
        format="mixed",
        errors="coerce"
    )
    df["date_added"] = dates.dt.strftime("%Y-%m-%d")
    df["date_added"] = df["date_added"].fillna("Unknown")

# 9. Export the cleaned dataset
df.to_csv(output_file, index=False, encoding="utf-8-sig")

# 10. Create a quality report
report = [
    "AUSPIFY TASK 1 - NETFLIX DATA CLEANING REPORT",
    "=" * 45,
    f"Original rows: {original_rows}",
    f"Original columns: {len(df.columns)}",
    f"Duplicate rows found initially: {original_duplicates}",
    f"Duplicate rows removed: {original_rows - len(df)}",
    f"Rows after cleaning: {len(df)}",
    f"Columns after cleaning: {len(df.columns)}",
    f"Missing cells before cleaning: {int(missing_before.sum())}",
    f"Missing cells after cleaning: {int(df.isnull().sum().sum())}",
    "",
    "Missing values before cleaning by column:",
    missing_before.to_string(),
    "",
    "Missing values after cleaning by column:",
    df.isnull().sum().to_string(),
    "",
    f"Cleaned file: {output_file.name}",
]

report_file.write_text("\n".join(report), encoding="utf-8")

print("\nOriginal duplicate rows:", original_duplicates)
print("Rows after cleaning:", len(df))
print("Missing cells after cleaning:", int(df.isnull().sum().sum()))
print("\nCleaned dataset saved as:", output_file.name)
print("Quality report saved as:", report_file.name)
print("\nTASK COMPLETED SUCCESSFULLY!")
