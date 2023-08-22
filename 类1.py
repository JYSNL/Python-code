import datetime

class Person:
    count = 0
    def __init__(self,tage):
        self.age = tage
    def __le__(self, other):
        if self.age<=other.age:
            return True
        else:
            return False
p1 = Person(50)
p2 = Person(40)
if (p1<=p2):
    print('1')
else:
    print('0')