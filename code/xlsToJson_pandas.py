
import pandas as pd
import json
from io import StringIO

excel_data_df = pd.read_excel('input/xlsToJson.xlsx', sheet_name='Sheet1')

json_str = excel_data_df.to_json(orient='records')
  
# Writing to sample.json 
with open("output/output.json", "w") as outfile: 
    outfile.write(json_str)