
#this program demonstrates a guessing game
#get user name
#get a user input
#generate a randon number
#using a while loop:
#check uif a user input is equal to generated number
from random import randint
user_name=input("whats your name:")
print("hello there" + user_name + "!")
random_number=randint(1,50)
counter=0
while counter < 5:
    usernumber=eval(input("input your number:"))
    counter +=1
    if usernumber<random_number:
        print("your guess is too low")
    elif usernumber>random_number:
        print("your guess is too high")
    elif usernumber==random_number:
    
        break
print("game over:")
if usernumber==random_number:
    print("you win!")
    print("the correct number was",random_number)
else:
    print("game over! the correct numberis")
    print(random_number)