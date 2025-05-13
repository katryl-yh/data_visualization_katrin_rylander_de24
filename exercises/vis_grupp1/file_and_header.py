from pathlib import Path
import pandas as pd
import re

# Folder with your Excel files
MAIN_DIRECTORY = Path(__file__).parents[0] 

data_dir = MAIN_DIRECTORY / "data/resultat_ansokning_program"

# Collect .xls and .xlsx files
all_files = [f for f in data_dir.iterdir() if f.is_file() and f.suffix in ['.xls', '.xlsx']]

# Match filenames ending in a year between 2009–2019
year_pattern = re.compile(r'-20(0[9]|1[0-9])\.(xlsx|xls)$')

# Collect results
results = []

for file_path in all_files:
    if year_pattern.search(file_path.name):
        try:
            df = pd.read_excel(file_path)
            column_names = df.columns.tolist()
        except Exception as e:
            column_names = [f"Error: {e}"]
        results.append({
            "filename": file_path.name,
            "columns": ", ".join(str(col) for col in column_names)
        })

# Convert to DataFrame and save to CSV
output_df = pd.DataFrame(results)
output_path = MAIN_DIRECTORY / "metadata.csv"
output_df.to_csv(output_path, index=False, encoding='utf-8')

print(f"Saved column names to: {MAIN_DIRECTORY}")