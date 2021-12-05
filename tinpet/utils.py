from twilio.rest  import Client
account_sid = 'AC96f5105aff90abe7ce797c607ef80e24'
auth_token = '7c95d518d085d309d71128a4e03a815c'
client = Client(account_sid, auth_token)
def send_sms(user_code,phone_number):

        message = client.messages.create(
                                body=f"Hi,you has logged in to Tinpet this is your verifycation code:{user_code}",
                                from_='+12183040773',
                                to=f'+84{phone_number}'
                            )

        print(message.sid)
