class Progression:
    def __init__(self, start = 0):
        self.cur = start

    def __iter__(self):
        return self

    def advance(self):
        self.cur += 1

    def __next__(self):
        if self.cur is None:
            raise StopIteration
        else:
            data = self.cur
            self.advance()
            return data

    def display(self, n):
        print(' '.join(str(next(self)) for i in range (n)))

class AP(Progression):
    def __init__(self, start = 0, step = 1):
        super().__init__(start)
        self.step = step

    def advance(self):
        self.cur += self.step

class GP(Progression):
    def __init__(self, start = 1, step = 2):
        super().__init__(start)
        self.step = step

    def advance(self):
        self.cur *= self.step

class FP(Progression):
    def __init__(self, first = 0, second = 1):
        super().__init__(first)
        self.prev = second - first

    def advance(self):
        self.prev, self.cur = self.cur, self.prev + self.cur

print('Default progression')
p = Progression()
p.display(10)

print('Ap with step 5:')
a = AP(5)
a.display(10)

print('Ap with start 2 and step 4:')
a = AP(2,4)
a.display(10)

print('Gp with default multiple:')
a = GP()
a.display(10)

print('Gp with start 1 and multiple 3:')
a = GP(1, 3)
a.display(10)

print('Fp with default start values:')
a = FP()
a.display(10)

print('Fp with start values 4 and 6:')
a = FP(4, 6)
a.display(10)