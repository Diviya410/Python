from twilio.rest import Client


account_sid='ACec5a6263aa726d195fe3584e271b03b6'
auth_token='8ea2222b8ad979f0502ae4153713d8fc'


client= Client(account_sid, auth_token)
phone_number=client.lookups.phone_numbers('+14067294450').fetch()

message = client.messages.create(
    body='Hey bro',
    from_=phone_number.phone_number,
    to='+917868819118'
)


print(message.sid)
