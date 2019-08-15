import os.path
import re
from google.colab import files

# This script takes the transcript file (as .txt) and converts it into a json file.
# I know, this is very basic and ugly, with lots of room for improvement :)

# array for storing questions/answers
database = []
arr = []
for i in range(0, 1030):
  database.append(arr)

# read the transcript file
ama = open("transcript.txt", "r", errors='ignore')
data = ama.read()
ama.close()

data = data.replace('Q.', 'Q. ')   # make sure all Q/A delimiters have a space after them
data = data.replace('A.', 'A. ')
data = data.replace('\n', ' ')
data = data.replace('"', '\'')     # text will only contain single quotes
data = data.replace('(edited)', '')

# remove @usernames (only first word for multi part names)
data = ' '.join(re.sub("(@[A-Za-z0-9.]+)"," ", data).split())

# split into sets of question + answer
data = data.split("Q. ")

# split question from the answer, save them
for i in range(0, len(data)):
  question = data[i].split("A. ")
  database[i].append(question)

# save array in a txt file
f = open("transcript.js", "a+")
f.truncate(0)
f.write("transcript = [")

# create the json array
for i in range(1, len(database)): #skip first element as it is [['']]
  template = '{{question: "{}", answer: "{}" }},'.format(database[0][i][0], database[0][i][1])
  f.write(template)

# remove the last character (,) and close the file
f.seek(0, os.SEEK_END)
f.seek(f.tell() - 1, os.SEEK_SET)
f.truncate()
f.write("]")
f.close()

# download only works in Google Chrome
files.download('transcript.js') 