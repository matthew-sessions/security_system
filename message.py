import os
from twilio.rest import Client
from datetime import datetime

def send_message(url):
    time = datetime.now()
    time = time.strftime(
			"%A %d %B %Y %I:%M:%S%p")    
    account_sid = 'AC67bf9a0daec49e827813cc4217ac72b4'
    auth_token = '594123f49a07912f38be01795f6ecf30'

    client = Client(account_sid, auth_token)

    client.messages.create(from_='+17039912018',
                        to='+13856261463',
                        body=f'Motion detected on {time}. View here: \n{url}')