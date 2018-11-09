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

puddle = Dog()
puddle.wag()