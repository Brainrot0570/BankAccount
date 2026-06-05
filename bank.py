class Bank:
    bankName = "Bank of America"
    def __init__(self, customer_name, current_balance, minimum_balance):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance

    def deposit(self, amount):
        self.current_balance += amount

    def withdraw(self, amount):
        #Validation - if currentBalance-amount is less than minimum
        #balance, the withdrawal does not happen and a message is printed
        if self.current_balance-amount >= self.minimum_balance:
            self.current_balance -= amount
        else:
            print("Insufficient funds")

    def print_customer_information(self):
        print(f"==={Bank.bankName}===")
        print(f"Name: {self.customer_name}")
        print(f"Balance: {self.current_balance}")
        print(f"Minimum Balance: {self.minimum_balance}")
