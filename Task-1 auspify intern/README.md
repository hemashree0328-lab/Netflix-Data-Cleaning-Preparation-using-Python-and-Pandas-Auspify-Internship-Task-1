# Netflix Data Cleaning & Preparation

**Internship Task:** Auspify — Task 1 

## Project Overview

This project prepares the Netflix titles dataset for business analytics and reporting using Python and Pandas.

## Objectives

- Inspect the dataset and assess data quality.
- Identify and handle missing values.
- Detect and remove duplicate records.
- Standardize column names and text formatting.
- Standardize date formatting.
- Export the cleaned dataset for further analysis.

## Tools & Technologies

- Python
- Pandas
- CSV
- Git and GitHub

## Project Files

| File | Description |
|---|---|
| `Dataset.csv` | Original dataset |
| `clean_netflix.py` | Data-cleaning script |
| `Netflix_Cleaned.csv` | Cleaned dataset |
| `cleaning_report.txt` | Data-quality report |

## How to Run

1. Install Python.
2. Install Pandas:

   ```bash
   python -m pip install pandas
   ```

3. Run the cleaning script:

   ```bash
   python clean_netflix.py
   ```

4. Review `Netflix_Cleaned.csv` and `cleaning_report.txt`.

## Data Quality

The script checks missing values and duplicate records, standardizes selected text fields, and formats the date-added column when present. The cleaning report records the results from the dataset being processed.

## Outcome

The project produces a cleaned CSV dataset and a report to support subsequent data analysis.

---

**Completed as part of the Auspify internship task.**