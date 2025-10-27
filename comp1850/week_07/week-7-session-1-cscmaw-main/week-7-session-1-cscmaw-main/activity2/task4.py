# Define an updated BankAccount class from activity1/task3
# that simulates a bank account with the following new methods:
# (1) deposit_funds - adding money to current balance
# (2) withdraw_funds - withdraw money from current balance. Should check if there is sufficient balance.
# If there is insufficient fund, should not be able to withdraw money. How would you define this method? 
# Should this method return something?
# (3) add_interest - add certain percentage of interest to the current balance
class BankAccount:
    def __init__(self, account_holder, account_number, current_balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.current_balance = current_balance

    def deposit_funds(self, amount):
        if amount > 0:
            self.current_balance += amount
            print(f"Deposited: {amount}. New balance: {self.current_balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw_funds(self, amount):
        if amount > self.current_balance:
            print("Insufficient funds for this withdraw.")
            return False
        elif amount <= 0:
            print("Withdraw amount must be positive.")
            return False
        else:
            self.current_balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.current_balance}")
            return True

    def add_interest(self, interest_rate):
        if interest_rate > 0:
            interest = self.current_balance * (interest_rate / 100)
            self.current_balance += interest
            print(f"Added interest: {interest}. New balance: {self.current_balance}")
        else:
            print("Interest rate must be positive.")

    def get_current_balance(self):
        return self.current_balance








# Once completed, create an instance of BankAccount with your details and 
# make at least one call to each of the new methods, as well as a call
# to retrieve the current_balance at the end.



# In the deposit_funds method, is a negative number allowed? 
# If you did not include validation on the value, please update
# your code to include that. A simple solution is no money is added
# the current balance if a negative amount is deposited into a bank account.




# How about the add_interest method? Can the interest be 0 or a negative number?
# If you have not include validation for that, update your code to deal with it.
