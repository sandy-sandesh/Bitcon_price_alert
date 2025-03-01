from twilio.rest import Client

def send_sms(message):
    try:
        client = Client(
            username="ACb1a227cbdd4e80453d62e4a861665f61", 
            password="06fa6245b7ce1dd967ba1f07b26bcab6"
        )
        message = client.messages.create(
            messaging_service_sid="MG496997b9869b9dce687918c9f68be409",
            body=message, 
            from_ = +16516158786,
            to="+9779860224636",
        )
        print("SMS sent!")
    except Exception as e:
        print(f"Something went wrong: {e}")

# if __name__ == "__main__":
#     send_sms()
