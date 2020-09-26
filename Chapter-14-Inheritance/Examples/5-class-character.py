from abc import ABC, abstractmethod
class Character(ABC):
    @abstractmethod
    def patriotism(self):
        pass

class Actor:
    def style(self):
        print('>> Actor.Style:')

class Person(Actor, Character):
    def do_acting(self):
        print('>> Person.doActing')

    def style(self):
        print('>> Person.style')

    def patriotism(self):
        print('>> Person.patriotism')

p = Person()
p.patriotism()
p.style()
p.do_acting()