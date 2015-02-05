from twilio.rest import TwilioRestClient
import sys

account_sid = "ACXXXXXXXXXXXXXXXXX" # replace with your account sid (available here: http://www.twilio.com/user/account/voice-messaging)
auth_token = "YYYYYYYYYYYYYYYYYY" # replace with your account token (available above)
client = TwilioRestClient(account_sid, auth_token) # set up the client

contacts = {
        "+441234567890":"Bob",
        "+440987654321":"Alice",
	"Put your Twilio number here":"Twilio"
}

num = raw_input("Send to: ") # ask for a number to send to
while num: # if there is a number...
	msg = raw_input("Message: ") # ...ask for the message to send
        if msg: # if there is a message
               	try: # try to...
                    	message = client.messages.create(to=str(num), from_=contacts.keys()[contacts.values().index("Twilio")], body=str(msg)) #...send a message
                except: # oh no! something went wrong...
                       	print "Unexpected error:", sys.exc_info()[0] # ...say there was an error
                        raise
        num = raw_input("Send to: ") # ask again for another number

#if __name__ == "__main__": # run the script
 #       app.run(debug=True,host="0.0.0.0") # start the Flask web server
