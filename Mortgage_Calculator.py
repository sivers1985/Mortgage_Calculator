# Python Mortgage Calculator
# First Codecademy project: utilizing Terminal, Git, Github, Object Oriented Programming

class MortgageCalculator:

    def __init__(self, yearly_percentage_rate, loan_term, principal):
        self.yearly_percentage_rate = yearly_percentage_rate
        self.loan_term = loan_term
        self.principal = principal
        self.monthly_percentage_rate = self.yearly_percentage_rate / 12
        self.number_monthly_payments = self.loan_term * 12

    def monthly_percentage(self):

        # Monthly percentage rate
        return "Your monthly percentage rate = " + "{:.3f}".format(self.monthly_percentage_rate)

    def number_payments(self):
        
        # Number of monthly payments
        return "Your number of payments = " + str(self.number_monthly_payments)

    def calculate_monthly_payment(self):
    
        # Calculate monthly payment
        if self.monthly_percentage_rate != 0:
            monthly_payment = ((self.monthly_percentage_rate * self.principal) / (1 - (1 + self.monthly_percentage_rate) ** -self.number_monthly_payments))
        else:
            monthly_payment = self.principal / self.number_monthly_payments

        return "Your monthly payment = $" + "{:.2f}".format(monthly_payment)

    def calculate_debt_schedule(self):
        for i in range(self.number_monthly_payments):
            p = self.principal
            x = (1 + self.monthly_percentage_rate)
            # Polynomial of x
            pn_x = ((x ** i - 1) / (x - 1))
            # Monthly payment
            c = ((self.monthly_percentage_rate * self.principal) / (1 - (1 + self.monthly_percentage_rate) ** -self.number_monthly_payments))
            amount_owed = x ** i * p - pn_x * c
            print("Amount owed at month {} = {:.2f}".format(i + 1, amount_owed))
            i += 1

def run_calculator():

    # Choice to keep running or exit
    print("Enter 1 for mortgage calculator")
    print("Enter 2 to exit")
    
    choice = int(input("Enter your choice: "))

    while choice != 2:

        # Enter the variables for the calculation
        yearly_percentage_rate = float(input("What is the yearly percentage rate? Enter as a decimal: "))
        print("----------------------------------------")
        
        loan_term = int(input("What is the duration of the mortgage? "))
        print("----------------------------------------")
        
        principal = float(input("What is the amount borrowed? $"))
        print("----------------------------------------")

        mortgage1 = MortgageCalculator(yearly_percentage_rate, loan_term, principal)

        print(mortgage1.number_payments())
        print("----------------------------------------")

        print(mortgage1.monthly_percentage())
        print("----------------------------------------")

        print(mortgage1.calculate_monthly_payment())
        print("----------------------------------------")

        mortgage1.calculate_debt_schedule()
        print("----------------------------------------")

        choice = int(input("Enter 1 to calculate another mortgage payment or 2 to exit: "))
        print("----------------------------------------")
        

run_calculator()