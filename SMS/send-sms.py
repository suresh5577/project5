# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACbfb3f0f79c5ee7ac76695671ffc4a85f'
auth_token = '27a04e4dc2dd355be507da50494a316c'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Hi Suresh Surya, how are you?",
                     from_='+12563339360',
                     to='+919618116034'
                 )

print(message.sid)