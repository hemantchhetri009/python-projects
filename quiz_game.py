# it is the basic program to run a quiz game
print("Welcome to the Quiz Game!")

play = input("Do you want to play? (yes/no): ").strip().lower()
if play != "yes":
    quit()

print("Great! Let's start the game.")
score = 0
questions = {
    "What is the capital of France?\n": "Paris",
    "What is 2 + 2?": "4",
    "What is the largest planet in our solar system?": "Jupiter",
    "Who wrote 'To Kill a Mockingbird'?": "Harper Lee",
    "What is the boiling point of water in Celsius?": "100"
}
for question, answer in questions.items():
    user_answer = input(question + " ").strip()
    if user_answer.lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {answer}.")    

print(f"Game Over! You got {score} out of {len(questions)} correct.")
