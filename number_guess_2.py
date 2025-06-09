# practicing again 

import random 
print("Welcome to number game !!") 
print("You have 7 chance to guess the correct number")
print("For example : 1-100,10-40\n")


low_num = int(input("Enter low number:  "))
high_num = int(input("Enter high number:  "))

user_num = random.randint(low_num, high_num)
chance = 7
guess = 0

while guess < chance:
    guess += 1
    print(f"\nchance {guess} of {chance} ")
    user_guess = int(input("Enter your guess:  "))

    if user_guess == user_num:
        print(f"You guessed correct number {user_num} in {guess} chances")
        break

    elif user_guess < user_num:
        print("To Low !! Guess some bigger numbers")

    elif  user_guess > user_num:
        print("To Big, Try some smaller one ")             

if user_guess != user_num:
    print(f"You lost every chances {guess} of {chance} , Please try again later on")