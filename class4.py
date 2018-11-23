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
# print("Name is", puppy.name)
# print("is it dog?", isinstance(puppy, Dog))
# test = Test()
# test.__q()