# this is again but full practice 
print("Welcome to the quiz , Made by hemant chhetri!")

# here we ask user whether they are ready to play or not 
user_play = input("Are you ready for the exciting quiz ever , Please Enter (yes/no!): ").strip().lower() 
# here we use .strip() to prevent hte un-necessary gaps or space entered by user 
# and .lower() is used to lower the alphabets whether user entered in capital or any 

if user_play != "yes":
    # so here im adding something to feel the user kinda uncomfortable that they miss valuable thing
    print("So you aren't playing which can help you to have something in your mind and can help you to have GF 😉, Start it now ........... ")
    quit()

print("Welcome to the most exciting quiz game! Developed by hemant chhetri ")
print("Lets Play😉")
score = 0 #we use score = 0 to clarify that the initial score of the play is zero 
questions = {
    "What is the capital city of nepal?\n": "kathmandu",
    "Who is the founder of Apple Company?\n": "steve jobs",
    "Where all computing things get stored ?\n":"memory"
}
#HERE WE CREATED A DICTIONARY WITH ITS ITEMS 

# using for loop 
for question, answer in questions.items(): # question { is dictionary : and this symbol is used to clarify that after this is items of dictionary}
    user_input = input( question + "").strip()
    if user_input.lower() == answer.lower():
        print("correct ")
        score += 1
    else:
        print(f"Wrong Answer! The correct answer is {answer}.")    

# in final we show the total points that user got while playing the game 

print(f"Thank You for playing \n You have got {score} out of {len(questions)} are correct!!😎")        




# show this is the process for the quiz game in python 
# which is also my first basic project 



