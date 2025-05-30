import json

# Import JSON messages
with open('messages.json', 'r') as file:
    MESSAGES = json.load(file)

print(MESSAGES['welcome'])

# Validate inputs
INVALID_INPUTS = {'nan', 'inf'}
def is_invalid(user_input):
    if user_input.casefold() in INVALID_INPUTS:
        return True
    try:
        number = float(user_input)
        if number <= 0:
            raise ValueError
    except ValueError:
        return True
    return False

# Helper Functions
def prompt(message):
    return f'>>> {message}'

def get_loan_amount():
    loan_amount = input(prompt(MESSAGES['loan_amount']))
    while is_invalid(loan_amount):
        print(prompt(MESSAGES['zero_error']))
        loan_amount = input(prompt(MESSAGES['loan_amount']))
    return float(loan_amount)

def get_apr():
    apr = input(prompt(MESSAGES['apr']))
    while is_invalid(apr):
        print(prompt(MESSAGES['zero_error']))
        apr = input(prompt(MESSAGES['apr']))
    return float(apr)

def get_years():
    num_of_years = input(prompt(MESSAGES['num_of_years']))
    while is_invalid(num_of_years):
        print(prompt(MESSAGES['zero_error']))
        num_of_years = input(prompt(MESSAGES['num_of_years']))
    return float(num_of_years)

# Main Function
def get_monthly_payment(amount, apr, years):
    monthly_interest_rate = (apr / 12) / 100
    num_of_months = years * 12
    monthly_payment = amount * ((monthly_interest_rate) /
                      (1 - (1 + monthly_interest_rate) ** (-num_of_months)))
    return monthly_payment

# Calculate and output monthly payments to user
while True:
    total_monthly_payments = get_monthly_payment(get_loan_amount(),
                                                get_apr(),
                                                get_years())

    print(prompt('Your total monthly payments are: '
             f'${total_monthly_payments:.2f}!'))

    # Prompt for another calculation
    while True:
        answer = input(prompt(MESSAGES['continue'])).lower()

        if answer.startswith('n') or answer.startswith('y'):
            break
        print(prompt(MESSAGES['invalid_choice']))

    if answer[0] == 'n':
        break