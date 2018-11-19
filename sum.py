lst = [1, 2, 3]


class A:
    def __init__(self):
        print(">>>>>")

class B(A):
    def anfn(self):
        print("<<<<<")
a = A()
b = B()
b.anfn()
