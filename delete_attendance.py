#this will delete the attendance if person is Absent
#Code created by amjid ali

import json
from datetime import date, timedelta
import requests

# Set the URL and authentication credentials for the ERPNext API
url = 'https://erp.syncbricks.com/api/resource/Attendance'
api_key = 'asdf'
api_secret = 'asdf'

# Calculate the start and end date for the current month
today = date.today()
start_date = date(today.year, today.month, 1)
end_date = today

# Set the filters for the attendance records to retrieve
filters = {
    'status': 'Absent',
    'attendance_date': ['between', [start_date.isoformat(), end_date.isoformat()]]
}

# Set the headers for the API request
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Token {api_key}:{api_secret}'
}

# Make the API request to retrieve the attendance records
response = requests.get(url, headers=headers, params={'filters': json.dumps(filters)})

# Check the response status code
if response.status_code == 200:
    # Convert the response data to a list of dictionaries
    attendance_list = response.json()['data']

    # Loop through the attendance list and cancel each record
    for attendance in attendance_list:
        try:
            # Make the API request to cancel the attendance record
            data = {
                'status': 'Cancelled',
                'docstatus': 2
            }
            response = requests.put(f'{url}/{attendance["name"]}', headers=headers, json=data)

            # Check the response status code
            if response.status_code == 200:
                print(f"Attendance record {attendance['name']} cancelled.")
            else:
                print(f"Error cancelling attendance record {attendance['name']}: {response.content}")
        except Exception as e:
            print(f"Error cancelling attendance record {attendance['name']}: {str(e)}")
else:
    print(response.content)
