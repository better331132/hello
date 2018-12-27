class TestClass :
    name = "TEST"

    def get_name(self):
        return self.name

    def area(self, x, y):
        return x * y

class Child(TestClass):
    def get_name(self):
        super().get_name()
        return "child Name:" + self.name

    def area(self, x, y):
        t = super().area(x, y)
        return t / 2

child = Child()
test = TestClass()
print(test.get_name())
print(child.get_name())