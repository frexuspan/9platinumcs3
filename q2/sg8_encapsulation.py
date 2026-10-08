class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Private attribute
        self.__balance = balance  # Private attribute

    def deposit(self): 
        amount = int(input("Update Balance to: "))
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")
        return f"Account Number: {self.__account_number} \nBalance: {self.__balance}" # Returns the account number and updated balance


    def withdraw(self):
        amount = int(input("Withdraw Amount: "))
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.__balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.") # Invalid withdrawal amount

        return f"Account Number: {self.__account_number} \nBalance: {self.__balance}" # Returns the account number and updated balance
    
    def get_balance(self):
        return self.__balance # Returns the current balance of the account

    def get_account_number(self):
        return self.__account_number  # Returns the account number of the account  


a1 = BankAccount("12345", 1000)

print("Account 1")
print(f"Account Number: {a1.get_account_number()}")  # Output: Account Number: 12345
print(f"Balance: {a1.get_balance()}") # Output: Balance: 1000
print(a1.deposit()) # This will prompt the user to input an amount to deposit and then display the updated balance