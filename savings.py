from bank import Bank

class SavingsAccount(Bank):
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number, interest_rate):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number) #call to super
        self.interest_rate = interest_rate

    def apply_interest(self):
        self.current_balance += self.current_balance * self.interest_rate

    def print_customer_information(self):
        super().print_customer_information()  #call to super
        print(f"Interest Rate: {self.interest_rate * 100}%")  #interest displayed as percentage
