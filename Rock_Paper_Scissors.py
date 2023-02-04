import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_inputs = input("\nType Rock/Paper/Scissors or Q to quit: ").lower()
    if user_inputs == 'q':
        break

    if user_inputs not in options:
        continue
    
    random_number = random.randint(0,2)
    # rock: 0, paper: 1, scissors: 2
    computer_picks = options[random_number]
    print("Computer picked ", computer_picks + ".")

    if user_inputs == "rock" and computer_picks == "scissors":
        print("Congrats, you won!")
        user_wins += 1

    elif user_inputs == "paper" and computer_picks == "rock":
        print("Congrats, you won!")
        user_wins += 1

    elif user_inputs == "scissors" and computer_picks == "paper":
        print("Congrats, you won!")
        user_wins += 1
    
    else:
        print("Sorry, Computer won this time")
        computer_wins += 1

print("You have won", user_wins, " times.")
print("The Computer won", computer_wins, " times.")
print("Goodbye!\n")