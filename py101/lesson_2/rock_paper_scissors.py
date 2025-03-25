import random

VALID_CHOICES = ["rock", "paper", "scissors", "lizard", "spock"]

def display_winner(player, computer):
    prompt(f"You chose {player}, computer chose {computer}")

    if ((player == "rock" and computer in ["scissors", "lizard"]) or
        (player == "paper" and computer in ["rock", "spock"]) or
        (player == "scissors" and computer in ["paper", "lizard"]) or
        (player == "lizard" and computer in ["spock", "paper"]) or
        (player == "spock" and computer in ["rock" or "scissors"])):
        prompt("You win!")
    elif ((computer == "rock" and player in ["scissors", "lizard"]) or
          (computer == "paper" and player in ["rock", "spock"]) or
          (computer == "scissors" and player in ["paper", "lizard"]) or
          (computer == "lizard" and player in ["spock", "paper"]) or
          (computer == "spock" and player in ["rock" or "scissors"])):
            prompt("Computer wins!")
    else:
        prompt("It's a tie!")

def prompt(message):
    print(f"==> {message}")

while True:
    prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
    choice = input()

    while choice not in VALID_CHOICES:
        prompt("That's not a valid choice")
        choice = input()

    computer_choice = random.choice(VALID_CHOICES)

    display_winner(choice, computer_choice)

    while True:
        prompt("Do you want to play again (y/n)?")
        answer = input().lower()

        if answer.startswith('n') or answer.startswith('y'):
            break
        else:
            prompt("That's not a valid choice")

    if answer[0] == 'n':
        break