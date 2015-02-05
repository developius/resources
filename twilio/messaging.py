# Code adapted from http://www.twilio.com/docs/quickstart/python

from flask import Flask, request, redirect
import twilio.twiml
 
app = Flask(__name__) # set up our Flask server
 
contacts = {
	"+441234567890":"Bob",
	"+440987654321":"Alice"
}
 
@app.route("/text", methods=['GET', 'POST'])
def text(): # the function to handle our incomming texts
    from_number = request.values.get('From', None) # get the sender's number
    if from_number in callers: # if we know them...
	print("%s texted you:" % callers[from_number]) # ...print who it was
    else: # we don't know them
	print("%s texted you:" % from_number) # print the sender's number
    print("	%s" % request.values.get('Body',None)) # print the sender's message
    message = raw_input("	Reply: ") # offer the option to reply (just press return if you don't want to)
    resp = twilio.twiml.Response()
    if message != "": resp.message(message) # if there is a reply, write the response
    else: resp.message("") # if there wasn't a reply, write an empty response
    return(str(resp)) # send the response (your reply - if there is one) back to the server

@app.route("/call", methods=['GET', 'POST'])
def call(): # the function to handle our incomming calls
    from_number = request.values.get('From', None) # get the caller's number
    if from_number in callers: # if we know the caller
        caller = callers[from_number] # get the callers's name
    else: # we don't know the caller so...
	caller = "Monkey" # ...let's call them Monkey

    resp = twilio.twiml.Response()
    # Greet the caller by name, if we can
    resp.say("Hello " + caller)
    # Play an MP3
    resp.play("http://demo.twilio.com/hellomonkey/monkey.mp3")

    return str(resp) # send the reponse to the caller

if __name__ == "__main__": # run our script
    app.run(debug=False,host="0.0.0.0") # start our Flask server
