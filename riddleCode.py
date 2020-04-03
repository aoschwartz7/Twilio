import random
import json
from riddles import riddles

riddlesLoaded = json.loads(riddles)

def randomRiddle():
    return random.sample(riddlesLoaded, 1)[0]
