class Bank:
    def __init__(self):
        self.money = 0

    def deposit(self, money):
        self.money = self.money + money
    
    def withdraw(self, money):
        self.money = self.money - money

wooribank = Bank()
wooribank.deposit(200)
wooribank.withdraw(100)
print(wooribank.money)

shinhanbank = Bank()
shinhanbank.deposit(300)
shinhanbank.withdraw(150)
print(shinhanbank.money)