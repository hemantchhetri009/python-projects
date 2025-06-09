# so this is number guessing game using python in-built module of py 

import random

print("Welcome to our second game!! 🕹️")
print("You have 7 chances to guess the correct number. 🥸")
print("For example: choose a range like 1-100 or 10-40.\n")

low_number = int(input("Enter the low number: "))
high_number = int(input("Enter the high number: "))

user_num = random.randint(low_number, high_number)
chances = 7
guesses = 0

while guesses < chances:
    guesses += 1
    print(f"\nChance {guesses} of {chances}")
    guess = int(input("Enter your guess: "))

    if guess == user_num:
        print(f"🎉 Correct! The number was {user_num}. You guessed it in {guesses} tries.")
        break
    elif guess > user_num:
        print("❌ Too high! Try a smaller number.")
    elif guess < user_num:
        print("❌ Too low! Try a bigger number.")

if guess != user_num:
    print(f"\n😞 You've used all your chances. The correct number was {user_num}. Better luck next time!")
