import random

while True:
    user_action = input("Enter your choise (rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scossors"]
    computer_action = random.choice(possible_actions)

    print(f"You chose {user_action}, computer chose {computer_action}")

    if user_action == computer_action:
        print("Its a tie!")
    elif user_action == "rock":
        if computer_action == "paper":
            print("You lost!")
        else:
            print("You won!")
    elif user_action == "paper":
        if computer_action == "scissors":
            print("You lost!")
        else:
            print("You won!")
    elif user_action == "scissors":
        if computer_action == "rock":
            print("You lost!")
        else:
            print("You won!")
    play_again = input("Play again?(y/n)")
    if play_again != "y":
        break