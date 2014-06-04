from os import environ

from twilio.rest import TwilioRestClient


client = TwilioRestClient(
    environ['TWILIO_ACCOUNT_SID'],
    environ['TWILIO_AUTH_TOKEN']
)

phone_numbers = [
    # Phone numbers go here
]

for number in phone_numbers:
    client.calls.create(
        to=number,
        from_='+27875504585',  # I bought this number at twilio.com
        url="http://hotlines.herokuapp.com/music/"
    )
