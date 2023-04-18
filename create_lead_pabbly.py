import json
import requests


#replace the data and url authentication
#for any help contact amjid@syncbricks.com


# Set the URL and authentication credentials for the Pabbly CRM API
url = 'https://erp.syncbricks.com/api/resource/Lead'
api_key = 'asdf'
api_secret = 'asdf'

# Set the headers for the API request
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}:{api_secret}'
}

# Set the data for the new lead
def create_lead(name, email, phone):
    data = {
        'name': name,
        'email': email,
        'phone': phone
    }
    
    # Make the API request to create the new lead in Pabbly CRM
    response = requests.post(url, headers=headers, json=data)

    # Check the response status code
    if response.status_code == 200:
        print("Lead created successfully.")
    else:
        print(f"Error creating lead: {response.content}")

# Use the WhatsApp API to extract data from the incoming message
def extract_data(message):
    # parse the incoming message using the WhatsApp API
    # extract the required data (name, email, phone)
    # return the extracted data as a tuple
    
    # Example code to extract data from message using WhatsApp API
    # You will need to replace this with the actual code to extract data using WhatsApp API
    data = json.loads(message)
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')
    return name, email, phone

# Main function to handle incoming WhatsApp messages and create leads in Pabbly CRM
def main():
    while True:
        # wait for incoming messages using the WhatsApp API
        message = receive_message()
        
        # extract data from the incoming message
        name, email, phone = extract_data(message)
        
        # create a new lead in Pabbly CRM
        create_lead(name, email, phone)

# Call the main function to start the lead creation process
if __name__ == '__main__':
    main()
