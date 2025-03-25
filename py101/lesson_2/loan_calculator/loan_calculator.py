# Mortgage / Car Loan Calculator 

# 1. Get 3 inputs from user (loan_amount, apr, and num_of_years)
# 2. Validate those inputs are valid
# 3. If inputs are not valid, reprompt the user to share their inputs
# 4. Once inputs are valid, use converted float values to calculate monthly payments 
# 5. Calculate the final monthly payment
# 6. Return the final value to the user

import json
import pdb

# Import JSON messages
with open('messages.json', 'r') as file: 
    MESSAGES = json.load(file)
    
# Welcome message
print(MESSAGES['welcome'])

# Validate inputs
def is_invalid(input):
    if input.casefold() == 'NaN'.casefold():
        return True
    try:
        float(input)
    except ValueError:
        return True
    return False

def is_zero(input):
    if not float(input):
        return True
    return False


# Helper Functions
def prompt(message):
    return(f'>>> {message}')

def get_loan_amount(): 
    loan_amount = input(prompt(MESSAGES['loan_amount']))
    while is_invalid(loan_amount):
        print(prompt('Please provide a valid number'))
        loan_amount = input(prompt(MESSAGES['loan_amount']))
    return float(loan_amount)

def get_apr():
    apr = input(prompt(MESSAGES['apr']))
    while is_invalid(apr) or is_zero(apr): 
        print(prompt('Please provide a valid percentage (%) that is greater than 0.'))
        apr = input(prompt(MESSAGES['apr']))
    
    return float(apr)

def get_years():
    num_of_years = input(prompt(MESSAGES['num_of_years']))
    while is_invalid(num_of_years) or is_zero(num_of_years):
        print(prompt('Please provide a valid number of years that is greater than 0.'))
        num_of_years = input(prompt(MESSAGES['num_of_years']))
    return float(num_of_years)

# Main Function
def get_monthly_payment(amount, apr, years):
    monthly_interest_rate = (apr / 12) / 100
    num_of_months = years * 12 
    monthly_payment = amount * ((monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** (-num_of_months)))
    return monthly_payment

# Calculate and output monthly payments to user 
total_monthly_payments = get_monthly_payment(get_loan_amount(), get_apr(), get_years())
print(prompt(f'Your total monthly payments are: ${total_monthly_payments:.2f}!'))