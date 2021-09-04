# Python Mortgage Calculator
# First Codecademy project: utilizing Terminal, git, github


def get_variables():

    # Enter the variables for the calculation
    yearly_percentage_rate = float(input("What is the yearly percentage rate? "))
    print("----------------------------------------")
    loan_term = int(input("What is the duration of the mortgage? "))
    print("----------------------------------------")
    principal = float(input("What is the amount borrowed? $"))
    print("----------------------------------------")

def calculate_monthly_payment():
    pass

def calculate_amount_owed():
    pass

def run_calculator():

    # Choice to keep running or exit
    print("Enter 1 for mortgage calculator")
    print("Enter 2 to exit")
    
    choice = int(input("Enter your choice: "))

    while choice != 2:

        get_variables()

        choice = int(input("Enter 1 to calculate another mortgage payment or 2 to exit: "))
        print("----------------------------------------")
        

run_calculator()