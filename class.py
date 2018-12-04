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

class Father:
    def work(self):
        return('근무 중')

class Son(Father):
    def study(self):
        return('공부 중')
    

person = Son()
print(person.work())

class Dog:
    def __init__(self):
        self.name ="dog"
        print("dog was born")

    def speak(self):
        print("Yelp!", self.name)

    def wag(self):
        print("dog's wag tail")

    def __del__(self):
        print("destroy!!")

class Puppy(Dog):
    def __init__(self, name):
        self.name = name
        print("Dog was born")
    
    def wag(self):
        print("Puppy's wag tail")

class Test:
    def test(self):
        print("Puppy's test")
        self.__q()

    def __q(self):
        print("qqqqqqqqqqqq")


puppy = Puppy('탕탕')
puppy.speak()
print("Name is", puppy.name)
print("is it dog?", isinstance(puppy, Dog))
test = Test()
test.__q()