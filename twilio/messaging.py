# Code adapted from http://www.twilio.com/docs/quickstart/python

from flask import Flask, request, redirect
import twilio.twiml
 
app = Flask(__name__)
 
# Try adding your own number to this list!
callers = {
	"+441234567890":"Bob",
	"+440987654321":"Alice"
}
 
@app.route("/text", methods=['GET', 'POST'])
def text():
    from_number = request.values.get('From', None)
    if from_number in callers:
	print("%s texted you:" % callers[from_number])
    else:
	print("%s texted you:" % from_number)
    print("	%s" % request.values.get('Body',None))
    message = raw_input("	Reply: ")
    resp = twilio.twiml.Response()
    if message != "": resp.message(message)
    else: resp.message("")
    return(str(resp))

@app.route("/call", methods=['GET', 'POST'])
def call():
    from_number = request.values.get('From', None)
    if from_number in callers:
        caller = callers[from_number]
    else:
	caller = "Monkey"

    resp = twilio.twiml.Response()
    # Greet the caller by name
    resp.say("Hello " + caller)
    # Play an MP3
    resp.play("http://demo.twilio.com/hellomonkey/monkey.mp3")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=False,host="0.0.0.0")
