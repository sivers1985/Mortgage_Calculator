# Python Mortgage Calculator
# First Codecademy project: utilizing Terminal, Git, Github, Object Oriented Programming

class MortgageCalculator:

    def calculate_monthly_percentage(self, yearly_percentage_rate):

        # Monthly percentage rate
        monthly_percentage_rate = yearly_percentage_rate / 12

        return monthly_percentage_rate

    def calculate_number_payments(self, loan_term):
        
        # Number of monthly payments
        number_monthly_payments = loan_term * 12

        return number_monthly_payments

    def calculate_monthly_payment(self, monthly_percentage_rate, principal, number_monthly_payments):
    
        # Calculate monthly payment
        if monthly_percentage_rate != 0:
            monthly_payment = ((monthly_percentage_rate * principal) / (1 - (1 + monthly_percentage_rate) ** -number_monthly_payments))
        else:
            monthly_payment = principal / number_monthly_payments

        return "Your monthly payment = $" + "{:.2f}".format(monthly_payment)

    def calculate_amount_owed(self):
        pass

def run_calculator():

    # Choice to keep running or exit
    print("Enter 1 for mortgage calculator")
    print("Enter 2 to exit")
    
    choice = int(input("Enter your choice: "))

    mortgage1 = MortgageCalculator()

    while choice != 2:

        # Enter the variables for the calculation
        yearly_percentage_rate = float(input("What is the yearly percentage rate? Enter as a decimal: "))
        print("----------------------------------------")
        
        loan_term = int(input("What is the duration of the mortgage? "))
        print("----------------------------------------")
        
        principal = float(input("What is the amount borrowed? $"))
        print("----------------------------------------")

        print(mortgage1.calculate_monthly_payment(mortgage1.calculate_monthly_percentage(yearly_percentage_rate), principal, 
        mortgage1.calculate_number_payments(loan_term)))
        print("----------------------------------------")

        choice = int(input("Enter 1 to calculate another mortgage payment or 2 to exit: "))
        print("----------------------------------------")
        

run_calculator()