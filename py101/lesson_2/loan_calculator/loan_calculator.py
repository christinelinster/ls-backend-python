import json

# Import JSON messages
with open('messages.json', 'r') as file:
    MESSAGES = json.load(file)

print(MESSAGES['welcome'])

# Validate inputs
def is_invalid(user_input):
    if user_input.casefold() == 'nan'.casefold():
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
    return(f'>>> {message}')

def get_loan_amount():
    loan_amount = input(prompt(MESSAGES['loan_amount']))
    while is_invalid(loan_amount):
        print(prompt('Please provide a valid number greater than 0.'))
        loan_amount = input(prompt(MESSAGES['loan_amount']))
    return float(loan_amount)

def get_apr():
    apr = input(prompt(MESSAGES['apr']))
    while is_invalid(apr):
        print(prompt('Please provide a valid '
                     'percentage (%) that is greater than 0.'))
        apr = input(prompt(MESSAGES['apr']))
    return float(apr)

def get_years():
    num_of_years = input(prompt(MESSAGES['num_of_years']))
    while is_invalid(num_of_years):
        print(prompt('Please provide a valid '
                     'number of years that is greater than 0.'))
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
total_monthly_payments = get_monthly_payment(get_loan_amount(),
                                             get_apr(),
                                             get_years())
print(prompt('Your total monthly payments are: '
             f'${total_monthly_payments:.2f}!'))