class BankAccount:
    """A class for bank accounts"""

    def __init__(self, interest_rate=0.01, balance=0):
        self.interest_rate = interest_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        # if there is not enough money: tell user and deduct $5
        if amount > self.balance:
            print('Insufficient funds: Charging a $5 fee.')
            self.balance -= 5
        return self

    def display_account_info(self):
        print('Balance: $', self.balance)
        return self

    def yield_interest(self):
        self.balance += self.balance * self.interest_rate
        return self


class User:
    """A Class for bank users"""
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount()


    def make_deposit(self, amount):
        self.account.deposit(amount)
        print('New Balance: $', self.account.balance)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        print('New Balance: $', self.account.balance)
        return self

    def display_user_balance(self):
        # print the user's name and account balance to the terminal
        print('Account Balance: $', self.account.balance)
        return self


monty = User('Monty Python', 'monty@python.com')
rowan = User('Rowan Atkinson', 'rowan@bean.com')

monty.make_deposit(100).make_withdrawal(25).display_user_balance()
