#This will create the sameple leave from the data provided below 
#replace the data and url authentication
#for any help contact amjid@syncbricks.com
import requests
import json

url = 'https://erp.syncbricks.com/api/resource/Lead'
api_key = 'asdf'
api_secret = 'asdf'

# Sample lead data
lead = {
    "lead_name": "Subject of Leaddd" ,   
    "first_name" : "Amjid Ali",
    "status" : "Open",
    "company_name" : "Syncbricks ABC",
    "email_id" : "amjid@syncbricks.com",
    "lead_details" : "Please share product details"
}

# Encode the lead data as JSON
lead_json = json.dumps(lead)

# Set the authentication headers
headers = {
    'Authorization': 'token {}:{}'.format(api_key, api_secret),
    'Content-Type': 'application/json'
}

# Send the request to create the lead
response = requests.post(url, headers=headers, data=lead_json)

# Check the status code of the response
if response.status_code == 200:
    print("Lead created successfully.")
else:
    print("Failed to create lead. Status code: {}".format(response.status_code))
