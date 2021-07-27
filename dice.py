
import random
import time

user_choice = 'yes'

while user_choice=='yes' or user_choice=='y':

    print("Dice is rolling....")
    time.sleep(1)

    dice1=random.randint(1,6)
    dice2=random.randint(1,6)

    print("dice 1 value is :",dice1, "\nDice 2 value is :",dice2)
    time.sleep(1)

    if(dice2 == dice1):
        print("congratulation you got same value")
    
    user_choice = input("do you want to play again ? (y/n)").lower()


print("thank you for playing")