from twilio.rest import Client

def send_spoofed_sms(target_number, spoof_number, message_body):
    client = Client("account_sid", "auth_token")
    message = client.messages.create(
        to=target_number,
        from_=spoof_number,
        body=message_body
    )
    print(f"Sent SMS to {target_number}: {message.sid}")
