from datetime import datetime, timedelta
import json
import requests

#replace the data and url authentication
#for any help contact amjid@syncbricks.com
#This will update the specific shift last sync date from now less 7 days
#This is to ensure that the attendance is marked only after specific date

# Set API key and secret
api_key = 'asdf'
api_secret = 'asdf

# Set last sync time to 7 days ago
last_sync = datetime.now() - timedelta(days=7)

# Set endpoint URL
url = 'https://erp.syncbricks.com/api/resource/Shift%20Type'

# Define the shift type data to be updated
shift_type_name = 'Shift Name Here'
shift_type_doc = {
    "last_sync_of_checkin": last_sync.strftime('%Y-%m-%d %H:%M:%S')
}

# Send PUT request to update the shift type
response = requests.put(f'{url}/{shift_type_name}', auth=(api_key, api_secret), data=json.dumps(shift_type_doc))

# Print the response status code and content
print('Response status code:', response.status_code)
print('Response content:', response.content.decode())
