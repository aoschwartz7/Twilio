from flask import Flask, request, redirect
from twilio.rest import Client
from twilio.twiml.messaging_response import Message, MessagingResponse
from twilio import twiml

import json, random
import os

# Twilio SID and token credentials
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")


# Create instances of riddle dictionary and riddle
riddleDict = {}
riddle = ""
file = 'riddles.json'

# Part 1) Create Functions
#-------------------------------------------------------------------------------
# function name: loadRiddles()
# parameters: file
# application: load file containing riddles.
# output: dictionary containing riddles and answers
# called by: Part 2)
def loadRiddles(file):
    global riddleDict
    with open(file) as fh:
      riddleDict = json.load(fh)
      return riddleDict

# function name: randomRiddle()
# parameters: riddles
# application: return a random riddle.
# output: random riddle
# called by: sendRiddle()
def randomRiddle():
    global riddleDict
    return random.sample(list(riddleDict), 1)[0]

# function name: answer()
# parameters: riddle
# application: Return riddle's answer.
# output: riddle key's value
# called by: sendRiddle(), smsReply()
def riddleAnswer(riddle):
    global riddleDict
    return riddleDict[riddle]


# Part 2) Send SMS to Registered Twilio Number
#-------------------------------------------------------------------------------
# Create Flask app instance
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def sendRiddle():
    # Generate random riddle
    global riddle
    riddle = randomRiddle()

    # Pass in Twilio credentials and send user riddle
    client = Client(account_sid, auth_token)
    message = client.messages.create(
                                  body= '{} \n\nFor a new riddle, message "new". For the answer, message "answer".'.format(riddle),
                                  from_='+16613698248',
                                  to='+15082453801'
                          )
# Part 3) Recieve SMS from Registered Twilio Number with Webhook
#-------------------------------------------------------------------------------
@app.route("/sms", methods=['GET', 'POST'])
def smsReply():

    # Retrieve form info from post request
    number = request.form['From']
    message_body = request.form['Body']
    message_body.lower()

    resp = MessagingResponse()
    # Send new riddle
    if message_body == 'new':
        resp.message(sendRiddle())
    # Reveal answer
    if message_body == 'answer':
        global riddle
        resp.message(riddleAnswer(riddle))
    # Repeat user's request options
    else:
        resp.message('Message "new" for another riddle or "answer" to reveal riddles answer')
    return str(resp)

if __name__ == "__main__":
    # Load file containing riddles
    riddleDict = loadRiddles(file)
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
