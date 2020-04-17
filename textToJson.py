# textToJSON.py is a program to convert text files to JSON.
# It was used to convert the text file provided by Nate Tan's repository https://github.com/natetan/riddler
# which contains a big list of riddles.

import json

# The file to be converted to JSON format
filename = 'inFile.txt'

# Dictionary where txt file line content will be stored
dict1 = {}

# Creating dictionary
with open(filename) as fh:
    for line in fh:
        dict1[line] = next(fh)

# Create json file
out_file = open("outFile.json", "w")
json.dump(dict1, out_file, indent = 4, sort_keys = False)
out_file.close()
