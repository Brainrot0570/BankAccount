from bank import Bank

class CheckingAccount(Bank):
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number, transfer_limit):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)  #call to super
        self.transfer_limit = transfer_limit

    def transfer(self, amount):
        if amount > self.transfer_limit:
            print(f"Cannot transfer funds.\nYour limit is: ${self.transfer_limit}")  #does not allow transfers above limit
        else:
            self.withdraw(amount)

    def print_customer_information(self):
        super().print_customer_information()  #call to super
        print(f"Transfer Limit: {self.transfer_limit}")  #add additional checking acc info to customer info
