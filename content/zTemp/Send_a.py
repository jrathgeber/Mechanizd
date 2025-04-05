import pywhatkit

phone_number = "+1234567890"  # Replace with the recipient's phone number
message = "Hello from Python!"
hour = 14  # 24-hour format
minute = 30

pywhatkit.sendwhatmsg(phone_number, message, hour, minute)