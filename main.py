from savings import SavingsAccount
from checking import CheckingAccount

"""tests for checking account module"""
print("=========Checking==========")
customer1 = CheckingAccount("John Doe", 1000, 100, "1", "1337", 500)
customer1.print_customer_information()
print("Test: withdraw $200")
customer1.withdraw(200)
print("Expected Balance: $800")
print(f"Actual Balance: ${customer1.current_balance}")
print("Test: Transfer over limit ($600)\n(This should fail)")
customer1.transfer(600)

print("===========================")
customer2 = CheckingAccount("Jane Doe", 2000, 200, "2", "1234", 1000)
customer2.print_customer_information()
print("Test: Transfer\nExpected Balance: $1500")
customer2.transfer(500)
print(f"Actual Balance: ${customer2.current_balance}")



"""tests for savings account module"""
print("==========Savings==========")
savings1 = SavingsAccount("Jamie Hyneman", 1000, 100, "3", "5678", 0.05)
savings1.print_customer_information()
print("Test: Apply Interest\nExpected Balance: $1050")
savings1.apply_interest()
print(f"Actual Balance: ${savings1.current_balance}")

print("===========================")
savings2 = SavingsAccount("Adam Savage", 3000, 300, "4", "67", 0.03)
savings2.print_customer_information()
print("Test: Deposit\nExpected Balance: $3500")
savings2.deposit(500)
print(f"Actual Balance: ${savings2.current_balance}")
