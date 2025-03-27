import random

CHOICES = ["rock", "paper", "scissors", "lizard", "spock"]
VALID_CHOICES = {
    "rock": ["rock", "r"],
    "paper": ["paper", "p"],
    "scissors": ["scissors", "s"],
    "spock": ["spock", "sp"],
    "lizard": ["lizard", "l"]
}
WINNING_CHOICES = {
    "rock": ["scissors", "lizard"],
    "paper": ["rock", "spock"],
    "scissors": ["paper", "lizard"],
    "spock": ["rock", "scissors"],
    "lizard": ["paper", "spock"]
}

# Helper Functions
def prompt(message):
    print(f"==> {message}")

def display_winner(player, computer):
    prompt(f"You chose {player}, computer chose {computer}")
    
    if computer in WINNING_CHOICES[player]:
        prompt("You win!")
    elif player in WINNING_CHOICES[computer]:
        prompt("Computer wins!")
    else:
        prompt("It's a tie!")

def get_choice(choice):
    for name, abbr in VALID_CHOICES.items():
        if choice in abbr:
            return name
    return None

while True:
    prompt(f'Choose one: {", ".join(CHOICES)}')
    choice = get_choice(input())

    while choice not in VALID_CHOICES:
        prompt("That's not a valid choice")
        choice = get_choice(input())

    computer_choice = random.choice(CHOICES)

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