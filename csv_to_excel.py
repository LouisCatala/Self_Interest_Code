import pandas as pd
import chardet

with open(r'C:\Users\13473\Downloads\data.csv', 'rb') as f:
    result = chardet.detect(f.read())
    encoding = result['encoding']

df = pd.read_csv(r'C:\Users\13473\Downloads\data.csv', encoding=encoding)

df.to_excel('output.xlsx', index=False, engine='openpyxl')