import requests
import json
import xlrd

#replace the data and url authentication
#for any help contact amjid@syncbricks.com
#This code is to create Leads from Excel file. The file path is provided. The format must be XLS

# Replace the URL, API key, and API secret with your own ERPNext instance's values
url = 'https://erp.syncbricks.com/api/resource/Lead'
api_key = 'sdfg'
api_secret = 'asdf'

# Update this variable to the path of your leads file
leads_file_path =  r"C:\Data\Dev\python\erpnext_api\files\leads.xls"

# Open the Excel workbook and select the first worksheet
workbook = xlrd.open_workbook(leads_file_path)
worksheet = workbook.sheet_by_index(0)

# Iterate through each row in the worksheet
for row_index in range(1, worksheet.nrows):
    # Read the data from the row
    lead_name = worksheet.cell_value(row_index, 0)
    lead_email = worksheet.cell_value(row_index, 1)
    lead_phone = worksheet.cell_value(row_index, 2)
    lead_status = worksheet.cell_value(row_index, 3)

    # Create a dictionary with the data for the new lead
    new_lead = {
        'lead_name': lead_name,
        'lead_email': lead_email,
        'lead_phone': lead_phone,
        'lead_status': lead_status
    }

    # Convert the dictionary to a JSON string
    json_data = json.dumps(new_lead)

    # Set the headers for the API request
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Token {api_key}:{api_secret}'
    }

    # Make the API request to insert the new lead
    response = requests.post(url, headers=headers, data=json_data)

    # Check the response status code
    if response.status_code == 200:
        print(f'New lead {lead_name} inserted successfully!')
    else:
        print(f'Error inserting new lead {lead_name}.')
