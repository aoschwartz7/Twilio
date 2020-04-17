# Twilio
This Python-Flask application sends a user an SMS of a random riddle, listens for their response via a Twilio webhook, and sends either the answer or a new riddle. It was built using Flask architecture and Twilio’s Programmable SMS API and Python helper library. 

# Part 1) Create Functions
Establishes several functions that do the following: load JSON file containing riddles in JSON format, generate a dictionary from that file, load a random riddle, and find anwer to riddle.

# Part 2) Send SMS
Once you've created an account with Twilio and registered a new phone number, you can now send a message to your personal number using your Twilio number. This is where we create a Flask app instance, generate a random riddle, and pass in Twilio credentials to send riddle as an SMS. 

# Part 3) Receive SMS from Registered Twilio Number with Webhook
I used ngrok for setting up a webhook with Twilio. Once you give Twilio the ngrok URL address, the route /sms will run when user sends an SMS response and triggers a post request. The user's message then gets processed by conditionals to see if user wants a new riddle or the answer to current riddle.

# How to Run It
1) Call TwilioRiddleApp.py in Terminal
2) Run ngrok in Terminal
3) Give Twilio webhook the ngrok URL
4) Go to localhost in browswer to send SMS to user
