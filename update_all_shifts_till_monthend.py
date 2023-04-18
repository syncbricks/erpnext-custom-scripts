import requests
import json
from datetime import datetime, timedelta, date

#replace the data and url authentication
#for any help contact amjid@syncbricks.com
#This will update the shift times for last month refer to the date setting in this code

# Set API key and secret
api_key = 'asdf'
api_secret = 'asdf'

# Set last sync time to end of previous month
today = date.today()
last_month_last_day = date(today.year, today.month, 1) - timedelta(days=1)
last_sync = datetime.combine(last_month_last_day, datetime.max.time())

# Set endpoint URL
url = 'https://erp.syncbricks.com/api/resource/Shift%20Type'

# Get all shift types
response = requests.get(url, auth=(api_key, api_secret))
shift_types = json.loads(response.content)['data']

# Update all shift types
for shift_type in shift_types:
    shift_type_name = shift_type['name']
    shift_type_doc = {
        "last_sync_of_checkin": last_sync.strftime('%Y-%m-%d %H:%M:%S')
    }
    response = requests.put(f'{url}/{shift_type_name}', auth=(api_key, api_secret), data=json.dumps(shift_type_doc))
    if response.status_code == 200:
        print(f'Successfully updated shift type {shift_type_name}')
    else:
        print(f'Error updating shift type {shift_type_name}: {response.content}')
