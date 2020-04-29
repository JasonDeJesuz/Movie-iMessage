import os
from subprocess import call

# We need a valid number
number = '+27123456543'
msg =  "Hello!"

# read the entire dorado.txt file and send a message word for word
with open('dorado.txt','r') as f:
    for line in f:
        for word in line.split():
           print(word)

           call(['osascript', 'sendMessage.applescript', number, word])
