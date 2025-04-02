import random
import json

with open('inputs.json', 'r') as file:
    INPUTS = json.load(file)

CHOICES = INPUTS["choices"]
VALID_CHOICES = INPUTS["valid_choices"]
WINNING_CHOICES = INPUTS["winning_choices"]

# Helper Functions
def prompt(message):
    print(f"==> {message}")

def get_choice(choice):
    choice = choice.lower()
    for name, abbr in VALID_CHOICES.items():
        if choice in abbr:
            return name
    return None

def get_point(player, computer):
    prompt(f"You chose {player}, computer chose {computer}.")

    if computer in WINNING_CHOICES[player]:
        result = "player"
    elif player in WINNING_CHOICES[computer]:
        result = "computer"
    else:
        result = "tie"

    return result

def display_points(p_score, c_score):
    prompt(f'+{"-" * 20}+')
    prompt(f'|{" " * 20}|')
    prompt(f"|  Player Score: {p_score}   |")
    prompt(f"|  Computer score: {c_score} |")
    prompt(f'|{" " * 20}|')
    prompt(f'+{"-" * 20}+')

def display_winner(p_wins, c_wins):
    if p_wins >= 5:
        prompt(INPUTS['winner'])
    elif c_wins >= 5:
        prompt(INPUTS['defeat'])

def play_game(p_score, c_score):

    # Get user choice
    prompt(f'Choose one: {", ".join(CHOICES)}.')
    choice = get_choice(input())

    while choice not in VALID_CHOICES:
        prompt(INPUTS['invalid_choice'])
        choice = get_choice(input())

    # Get computer choice
    computer_choice = random.choice(CHOICES)

    # Determine who gets the point
    point = get_point(choice, computer_choice)

    if point == 'player':
        prompt("One point for you!")
        p_score += 1
    elif point == 'computer':
        prompt("One point for the computer!")
        c_score += 1
    else:
        prompt("It's a tie!")

    display_points(p_score, c_score)
    return p_score, c_score

def main():
    player_score = 0
    computer_score = 0
    winner = False

    while not winner:
        player_score, computer_score = play_game(player_score, computer_score)

        # Determine final winner
        if player_score >= 5 or computer_score >=5:
            display_winner(player_score, computer_score)
            winner = True

prompt(INPUTS['welcome'])
prompt(INPUTS['instructions'])

while True:
    main()
    while True:
        prompt(INPUTS['play_again'])
        answer = input().lower()

        if answer.startswith('n') or answer.startswith('y'):
            break
        prompt(INPUTS['invalid_choice'])

    if answer[0] == 'n':
        prompt(INPUTS['goodbye'])
        break