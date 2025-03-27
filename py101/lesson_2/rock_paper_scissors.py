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

def get_point(player, computer):
    prompt(f"You chose {player}, computer chose {computer}")
    result = ""
    if computer in WINNING_CHOICES[player]:
        prompt("One point for you!")
        result = "player"
    elif player in WINNING_CHOICES[computer]:
        prompt("One point for the computer!")
        result = "computer"
    else:
        prompt("It's a tie!")

    return result

def get_choice(choice):
    choice = choice.lower()
    for name, abbr in VALID_CHOICES.items():
        if choice in abbr:
            return name
    return None

def display_winner(p_wins, c_wins):
    if p_wins >= 5:
        prompt("WINNER! WINNER! You win this round!")
    elif c_wins >= 5:
        prompt("DEFEAT... The computer wins!")

def play_game(p_score, c_score):

    # Get user choice
    prompt(f'Choose one: {", ".join(CHOICES)}')
    choice = get_choice(input())

    while choice not in VALID_CHOICES:
        prompt("That's not a valid choice")
        choice = get_choice(input())

    # Get computer choice
    computer_choice = random.choice(CHOICES)

    # Determine who gets the point
    point = get_point(choice, computer_choice)

    if point == 'player':
        p_score += 1
    else:
        c_score += 1
    
    prompt(f"Player Score: {p_score}")
    prompt(f"Computer score: {c_score} points")

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
            prompt(f"The final results are: \n"
                f"Player Score: {player_score} \n"
                f"Computer Score: {computer_score}")
            winner = True

while True:
    main()
    while True:
        prompt("Do you want to play again? (y/n)")
        answer = input()

        if answer.startswith('n') or answer.startswith('y'):
            break
        prompt("That is not a valid option. Please try again.")

    if answer[0] == 'n':
        prompt("Thank you for playing. Come again next time")
        break