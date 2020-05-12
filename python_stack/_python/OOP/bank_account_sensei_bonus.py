class BankAccount:
    """A class for bank accounts"""

    def __init__(self, acc_number='', interest_rate=0.01, balance=0):
        self.acc_number = acc_number
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
        print('Account Number:', self.acc_number)
        print('Interest Rate:', self.interest_rate)
        print('Balance: $', self.balance)
        return self

    def yield_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(interest)
        return self


class User:
    """A Class for bank users"""
    def __init__(self, name, email):
        self.name = name
        self.email = email
        # self.account = BankAccount()
        self.user_accounts = {}   # to hold account info dictionaries

    def open_account(self, acc_number='', interest_rate=0.01, balance=0):
        self.user_accounts[acc_number] = BankAccount(
                                            acc_number=acc_number,
                                            interest_rate=interest_rate,
                                            balance=balance
                                            )
        print('Opened Account #:', acc_number)
        return self

    def view_user_accounts(self):
        # display account balances for all of user's accounts
        print('Summary of Accounts for', self.name)
        for key, value in self.user_accounts.items():
            self.user_accounts[key].display_account_info()
        return self

    def make_deposit(self, acc_number, amount):
        self.user_accounts[acc_number].deposit(amount)
        print(f'${amount} has been deposited into Account #{acc_number}')
        return self

    def make_withdrawal(self, acc_number, amount):
        self.user_accounts[acc_number].withdraw(amount)
        print(
            f'${amount} has been withdrawn from Account #{acc_number}')
        return self

    def display_user_balance(self, acc_number):
        # print account number and balance
        print(
            f'Account No {acc_number} has a balance of ' +
            f'${self.user_accounts[acc_number].balance}'
            )
        return self


monty = User('Monty Python', 'monty@python.com')

monty.open_account(1).open_account(2, balance=300)
monty.make_deposit(1, 100).make_withdrawal(2, 75).display_user_balance(1)
monty.view_user_accounts()
