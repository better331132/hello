class Father:
    def work(self):
        return('근무 중')

class Son(Father):
    def study(self):
        return('공부 중')
    

person = Son()
print(person.work())