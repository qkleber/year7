#V1-chatting Robot
#Programmer: Mr. Quevedo-----Date: October 20, 2017



import os
import time
import random

"""
Create a chatting robot that will make the user believe that he/she is 
talking to an intelligent machine.
http://www.cleverbot.com/
"""
#welcome text
print()
print("""Hi! My name is Kelso. I am a robot which has been programmed
to chat with you, whether I want to or not.""")

os.system("""say 'Hi! My name is Kelso. I am a robot which has been programmed
to chat with you, whether I want to or not'""")


#user input
print()
time.sleep(1)
name = input("What is your name? ")
print("Nice to meet you {0}.".format(name))
os.system("say 'Nice to meet you {0}'".format(name))


#feeling
print()
feeling = input("How are you today? ")
feeling = feeling.lower()

if "happy" in feeling:
    print("I am happy too.")
elif "fine" in feeling:
    print("I am fine too.")
elif "awesome"in feeling:
    print("I am happy to hear that.")
else:
    print("I am sorry to hear that...")

#colour
print()
colours = ["Blue", "Yellow", "Green", "Red"]
time.sleep(1)
favColour = input("What is your favourite colour? ")
print("I see that your favourite colour is {0}.".format(favColour))
print("My favourite colour is {0}.".format(random.choice(colours)))

#exit
print()
time.sleep(1)
print("Sleep time.......")
time.sleep(1)
print("Sleep......sleep....")
time.sleep(1)

print()
print("It was nice talking to you, but I have to go now. Sorry...personal issues... ")