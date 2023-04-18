import requests
import json
from datetime import datetime, timedelta, time

#replace the data and url authentication
#for any help contact amjid@syncbricks.com
#This code will update the shift sync time and process attendance after time for all the shift types


# Set API key and secret
api_key = 'asdf'
api_secret = 'asdf'

# Set last sync time to today - 7 days at 11:59 pm
last_sync = datetime.now() - timedelta(days=7)
last_sync = last_sync.replace(hour=23, minute=59, second=0, microsecond=0)

# Set process attendance after to first day of the month at 12:00 am
process_attendance_after = datetime.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)

# Set endpoint URL
url = 'https://erp.syncbricks.com/api/resource/Shift%20Type'

# Get all shift types
response = requests.get(url, auth=(api_key, api_secret))

# Update process attendance after and last_sync for each shift type
if response.status_code == 200:
    shift_types = json.loads(response.content)['data']
    for shift_type in shift_types:
        shift_type_doc = {
            'name': shift_type['name'],
            'process_attendance_after': process_attendance_after.isoformat(),
            'last_sync_of_checkin': last_sync.isoformat()
        }
        response = requests.put(f'{url}/{shift_type["name"]}', auth=(api_key, api_secret), data=json.dumps(shift_type_doc))
        print(f'Response status code: {response.status_code}')
        print(f'Response content: {response.content}')
else:
    print(f'Response status code: {response.status_code}')
    print(f'Response content: {response.content}')
