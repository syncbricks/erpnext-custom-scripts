#replace the data and url authentication
#for any help contact amjid@syncbricks.com
#This code is to create Leads from Excel file. The file path is provided. The format must be XLSX

import pandas as pd
import requests

url = 'https://erp.syncbricks.com/api/resource/Lead'

# Replace with your own API key and API secret
api_key = 'asdf'
api_secret = 'asdf'

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': f'Token {api_key}:{api_secret}'
}

# Read Excel file
df = pd.read_excel(r'C:\Data\Dev\syncbricks\tutorial\lead2.xlsx')

# Loop through rows and create leads
for index, row in df.iterrows():
    data = {
        'doctype': 'Lead',
        'lead_name': str(row['company_name']),
        'lead_source': 'Website',
        'company_name': str(row['company_name']),
        'phone': str(row['company_phone'])
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        print(f'Lead {row["company_name"]} created successfully')
    else:
        print(f'Failed to create lead {row["company_name"]}:', response.json())
