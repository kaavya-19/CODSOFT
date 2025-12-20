# CodSoft Python Internship Task
# Task Name: Rock Paper Scissors
# Author: Kaavya B M


import random

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

def show_instructions():
    print("\n--- ROCK PAPER SCISSORS GAME ---")
    print("Instructions:")
    print("1. Type rock, paper, or scissors")
    print("2. Rock beats Scissors")
    print("3. Scissors beats Paper")
    print("4. Paper beats Rock")

def get_user_choice():
    choice = input("\nEnter your choice (rock/paper/scissors): ").lower()
    if choice in choices:
        return choice
    else:
        print("Invalid choice! Please try again.")
        return None

def get_computer_choice():
    return random.choice(choices)

def decide_winner(user, computer):
    global user_score, computer_score

    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}")

    if user == computer:
        print("Result: It's a tie!")
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "scissors" and computer == "paper") or
        (user == "paper" and computer == "rock")
    ):
        print("Result: You win this round!")
        user_score += 1
    else:
        print("Result: Computer wins this round!")
        computer_score += 1

def show_score():
    print("\n--- SCORE BOARD ---")
    print(f"Your Score: {user_score}")
    print(f"Computer Score: {computer_score}")

# Main Game Loop
show_instructions()

while True:
    user_choice = get_user_choice()
    if not user_choice:
        continue

    computer_choice = get_computer_choice()
    decide_winner(user_choice, computer_choice)
    show_score()

    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("\nThanks for playing! Game Over.")
        break
