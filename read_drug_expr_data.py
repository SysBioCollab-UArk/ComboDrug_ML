import pandas as pd
import os

df_gdsc = pd.read_csv(os.path.join('DATA', 'GDSC2_SKCM_Melanoma_Cell_Lines.csv'))

print(df_gdsc.head())           # View the first few rows
print(df_gdsc.columns)          # See column names
print(df_gdsc.dtypes)           # Check data types

df_info = pd.read_csv(os.path.join('DATA', 'sample_info.csv'))

print(df_info.head())
print(df_info.columns)
print(df_info.dtypes)


# Merge the dataframes on the cell line name columns
# We'll do a left join to keep only the rows in df_gdsc
merged = pd.merge(df_gdsc, df_info, how='left', left_on='CELL_LINE_NAME', right_on='cell_line_name')

print(merged.head())
print(merged.columns)
print(merged.dtypes)
