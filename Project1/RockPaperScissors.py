import random

user_wins = 0
computer_wins = 0

options = [ "rock","poper","scissors"]

while True:
    
    user_input = input("Enter Rock, Paper, Scissors or q to quit: ").lower()
    computer_input = options[random.randint(0,2)]
    if user_input not in options:
        continue
    if user_input == "q":
        print("Your total score: ",user_wins)
        print("Computer total score: ",computer_wins)
        if user_wins > computer_wins:
            print("You achieved mastery!")
        elif computer_wins > user_wins:
            print("Better luck next time. Hard luck!")
        else:
            print("You are as good as computer!")
        break
    print("Computer chose: ",computer_input+".")
    if user_input == "rock" and computer_input == "scissors":
        print ("You won!")
        user_wins+=1
        continue
    elif user_input == "paper" and computer_input == "rock":
        print ("You won!")
        user_wins+=1
        continue
    elif user_input == "scissors" and computer_input == "paper":
        print ("You won!")
        user_wins+=1
        continue
    elif user_input == "rock" and computer_input == "paper":
        print ("Computer won!")
        computer_wins+=1
        continue
    elif user_input == "paper" and computer_input == "scissors":
        print ("Computer won!")
        computer_wins+=1
        continue
    elif user_input == "scissors" and computer_input == "rock":
        print ("Computer won!")
        computer_wins+=1
        continue
    else:
        print ("Draw! No one gets a point.")
        continue
    