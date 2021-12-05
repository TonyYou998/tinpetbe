from twilio.rest  import Client
account_sid = 'AC96f5105aff90abe7ce797c607ef80e24'
auth_token = '350f43c3518181222ba71e73ff0192c0'
client = Client(account_sid, auth_token)
def send_sms(user_code,phone_number):

        message = client.messages.create(
                                body=f"Hi,you has logged in to Tinpet this is your verifycation code:{user_code}",
                                from_='+12183040773',
                                to=f'+84{phone_number}'
                            )

        print(message.sid)
