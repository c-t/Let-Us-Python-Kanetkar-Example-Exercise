"""
WAP that uses simple inheritance between classes Base and Derived.
If there is a method in Base class, how do you prevent it from being overridden in the Derived class?
"""
class Base:
    def __method(self):
        print('ln Base.__method')

    def func(self):
        self.__method()

class Derived(Base):
    def __method(self):
        print('ln Dervied._method')

b = Base()
b.func()

d = Derived()
d.func()
