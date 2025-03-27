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

computer_wins = 0
player_wins = 0
winner = False

# Helper Functions
def prompt(message):
    print(f"==> {message}")

def get_point(player, computer):
    global player_wins
    global computer_wins
    prompt(f"You chose {player}, computer chose {computer}")
    
    if computer in WINNING_CHOICES[player]:
        player_wins += 1
        prompt("One point for you!")

    elif player in WINNING_CHOICES[computer]:
        computer_wins += 1
        prompt("One point for the computer!")
    else:
        prompt("It's a tie!")
    prompt(f"Player points: {player_wins} points")
    prompt(f"Computer points: {computer_wins} points")

def get_choice(choice):
    choice = choice.lower()
    for name, abbr in VALID_CHOICES.items():
        if choice in abbr:
            return name
    return None

def display_winner(p_wins, c_wins):
    global winner
    if p_wins >= 5:
        prompt("WINNER! WINNER! You win this round!")
        winner = True
    elif c_wins >= 5:
        prompt("DEFEAT :( The computer wins!")
        winner = True

def main():
    prompt(f'Choose one: {", ".join(CHOICES)}')
    choice = get_choice(input())

    while choice not in VALID_CHOICES:
        prompt("That's not a valid choice")
        choice = get_choice(input())

    computer_choice = random.choice(CHOICES)
    get_point(choice, computer_choice)

    if player_wins >= 5 or computer_wins >=5:
        display_winner(player_wins, computer_wins)


while not winner or True:
    main()

    if winner:
        while True:
            prompt("Do you want to play again (y/n)?")
            answer = input().lower()
            if answer.startswith('n') or answer.startswith('y'):
                break
            prompt("That's not a valid choice")
        if answer[0] == 'n':
            break
        computer_wins = 0 
        player_wins = 0 
        winner = False

