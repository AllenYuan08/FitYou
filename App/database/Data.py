import pandas as pd
import sqlite3

excel_path = '../Data/Data.xlsx'
db_path1 = 'DietData.db'
db_path2 = 'ExerciseData.db'


df_sheet1 = pd.read_excel(excel_path, sheet_name=0)
conn1 = sqlite3.connect(db_path1)

df_sheet1.to_sql('Diet', conn1, if_exists='replace', index=False)
conn1.close()

df_sheet2 = pd.read_excel(excel_path, sheet_name=1)

conn2 = sqlite3.connect(db_path2)
df_sheet2.to_sql('Exercise', conn2, if_exists='replace', index=False)
conn2.close()

