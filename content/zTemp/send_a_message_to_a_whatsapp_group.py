import pywhatkit

group_id = "AB123CDEFGhijklmn"
message = "Hello, this is a test message sent from Python!"

pywhatkit.sendwhatmsg_to_group(group_id, message, 15, 30)