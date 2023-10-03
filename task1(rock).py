import random
while True:
    user_choice = input("Enter a choice (rock, paper, scissors): ")
    possible_choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(possible_choices)
    print(f"\nYou choose {user_choice}, computer chose {computer_choice}.\n")

    if user_choice == computer_choice:
        print(f"Both players selected {user_choice}. It's a draw match!")
    elif user_choice == "rock":
        if computer_choice == "scissors":
            print(" You win!")
        else:
            print(" You lose.")
    elif user_choice == "paper":
        if computer_choice == "rock":
            print("You win!")
        else:
            print(" You lose.")
    elif user_choice == "scissors":
        if computer_choice == "paper":
            print(" You win!")
        else:
            print(" You lose.")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
