import random

VALID_CHOICES = ["rock", "paper", "scissors", "lizard", "spock"]
WINNING_CHOICES = {"rock": ("scissors", "lizard"),
                   "paper": ("rock", "spock"),
                   "scissors": ("paper", "lizard"),
                   "spock": ("rock", "scissors")}

def display_winner(player, computer):
    prompt(f"You chose {player}, computer chose {computer}")
    
    if computer in WINNING_CHOICES[player]:
        prompt("You win!")
    elif player in WINNING_CHOICES[computer]:
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