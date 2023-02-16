
#this program demonstrates a guessing game
#get user name
#get a user input
#generate a randon number
#using a while loop:
#check uif a user input is equal to generated number
from random import randint
user_name=input("whats your name")
print("hello there" + user_name + "!")

counter=0
while counter < 5:
    usernumber=eval(input("input your number:"))

number =randint(10,50)
