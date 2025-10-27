# Define a BankAccount class with the following fields:
# (1) holder_name
# (2) account_no
# (3) current_balance

# The value to each field needs to be provided when an instance of BankAccount is created.
# Write code to create an instance of BankAccount




# Write code to print the details of the bank account



# How would you change the __init__ method so that by the current_balance is an
# optional argument with a default value of 10 indicating that amount is needed to create
# a bank account? Recall optional argument in function definition?

# Once done, create another instance of BankAccount with only holder's name and 
# account number, and then print the all details of the new instance.
class BankAccount:
    def __init__(self, holder_name, account_no, current_balance=10):
        self.holder_name = holder_name
        self.account_no = account_no
        self.current_balance = current_balance
account1 = BankAccount("Alice Smith", "123456789", 500)
print(f"Account Holder Name: {account1.holder_name}")
print(f"Account Number: {account1.account_no}")
print(f"Current Balance: {account1.current_balance}")
account2 = BankAccount("Bob Johnson", "987654321")
print(f"Account Holder Name: {account2.holder_name}")
print(f"Account Number: {account2.account_no}")
print(f"Current Balance: {account2.current_balance}")   
