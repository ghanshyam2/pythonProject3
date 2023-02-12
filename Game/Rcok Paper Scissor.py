import random

while True:
    user_action = input("Enter Choice (rock, paper, scissor):")
    possible_action = ["rock", "paper", "scissor"]
    computer_action = random.choice(possible_action)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "paper":
            print("Rock smashes scissors! You Win !")
        else:
            print("Paper covers rock ! You win!")
    elif user_action == "paper":
        if computer_action == "rock":
            print("paper covers rock! You win")
        else:
            print("Scissors cuts paper! hahaha!")
    elif user_action == "scissor":
        if computer_action == "paper":
            print("scissor cuts paper! You win")
        else:
            print("Rock smashes scissor! Try Again  fella!")

    play_again = input("play again? (y/n):")
    if play_again != 'y':
        break