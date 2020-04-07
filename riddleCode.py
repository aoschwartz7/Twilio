import random
import json
from riddleBank import riddleBank


# function name: randomRiddle()
# parameters: riddles
# application: load riddles and return a random riddle
# output: random riddle
# called by: send_sms.py
def randomRiddle(riddles):
    riddlesLoaded = json.loads(riddles)
    return random.sample(list(riddlesLoaded), 1)


# function name: riddleAnswer()
# parameters: riddleBank, riddle
# application: Return riddle's correctAnswer from riddleBank.
# output: correctAnswer
# function called by:
def riddleAnswer(riddleBank, riddle):
    correctAnswer = riddleBank[riddle]
    return correctAnswer


# function name: cleanString()
# parameters: stringToClean
# application: Make user's response more flexible by lower-casing answer.
# output: stringToClean
# function called by:
def cleanString(stringToClean):
    stringToClean = stringToClean.lower()
    return stringToClean

if __name__ == '__main__':
    riddle = randomRiddle(riddleBank)
    print(riddle)
    print(riddleAnswer(riddleBank, riddle))
    print(riddleAnswer)
