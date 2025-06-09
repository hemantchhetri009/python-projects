# so it a rock, paper and scissor game\
import random

print("Game Rule fo defeating computer \n\n"
      
      +"Rock vs Paper -> Paper\n"
      +"Rock vs scissor-> Rock wins\n"
      +"paper vs scissor-> scissor wins.\n")

while True:
    # remember we cant have string so we need to do all in integer
    print("Your Choices\n 1 - Rock\n 2 - Paper\n 3 - Scissor\n")
    # break 
    # so here we take User input 
    user_choice = int(input("Enter your choice\n for eg:1,2,3:  "))

    # looping with while loop until user entered correct number 

    while user_choice > 3 or user_choice < 1:
        print("Invaild number choice")
        user_choice = int(input("Enter Valid Number :  "))

        # after valid entry of number then 

    if user_choice == 1:
            user_choice_name = "Rock"

    elif user_choice == 2:
            user_choice_name = "Paper"    

    else:
            user_choice_name = " Scissor"

    print("User Choice is :", user_choice_name)
    print("Computer bot choicing .......")

    computer_choice = random.randint(1,3)

    if computer_choice == 1:
          computer_choice_name = "Rock"

    elif computer_choice == 2:
          computer_choice_name = "Paper"       

    else:
          computer_choice_name = "Scissor"

    print("Computer Choice is :", computer_choice_name)            
    print(user_choice_name, "vs", computer_choice_name)

    # now time for comparing 

    if user_choice == computer_choice:
          result = "Draw"

    elif (user_choice == 1 and computer_choice == 2) or (computer_choice == 1 or user_choice == 2):
          result = "Paper"

    elif (user_choice == 1 and computer_choice == 3) or (computer_choice == 1 and user_choice == 3):
          result = "Rock"

    elif (user_choice == 2 and computer_choice == 3 ) or (computer_choice == 2 and user_choice == 3 ):
          result = " Sicssor" 



    # now 

    if result == "Draw":
          print("Its Tie ")

    elif result == user_choice_name:
          print("Congratulation!! You just beat best bot ") 

    else:
          print("use your silly brain human!! Computer Won")


    print(" Do you wanna play it again?? (Y/N):  ")
    answer =input().lower()
    if answer == 'n':
       break

print(" Thank you")


# finallyyy done with this project tooo 

# late night code 




