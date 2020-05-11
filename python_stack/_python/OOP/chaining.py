class User:
    """A Class for bank users"""
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        # print the user's name and account balance to the terminal
        print('Name:', self.name, '\nAccount Balance: $', self.account_balance)
        return self

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self


monty = User('Monty Python', 'monty@python.com')
rowan = User('Rowan Atkinson', 'rowan@bean.com')
john = User('John Cleese', 'john@fawltytowers.com')

monty.make_deposit(100).make_deposit(75).make_deposit(150).make_withdrawal(65).display_user_balance()
rowan.make_deposit(95).make_deposit(175).make_withdrawal(25).make_withdrawal(50).display_user_balance()
john.make_deposit(325).make_withdrawal(50).make_withdrawal(15).make_withdrawal(100).display_user_balance()
monty.transfer_money(john, 75).display_user_balance()
john.display_user_balance()

