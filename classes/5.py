class Account:
    def __init__(self, owner, balance=0): #The constructor initializes an Account class object with two attributes
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount): #Method for depositing funds into the account. Checks that the deposit amount is positive
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount): #Method for withdrawing funds from the account
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Withdrawal amount must be positive.")

owner = input()
x = int(input())
y = int(input())
z = int(input())
balance = float(input())
acc= Account(owner, balance)

acc.deposit(x)
acc.withdraw(y)
acc.withdraw(z)

'''Owner's name: "Alice"
Deposit amount (x): 100
First withdrawal amount (y): 50
Second withdrawal amount (z): 60
Initial balance: 20.0'''
