from abc import ABC, abstractmethod
class Printer(ABC):
    def __init__(self, n):
        self.name = n

    @abstractmethod
    def print(self, docName):
        pass

class LaserPrinter(Printer):
    def __init__(self, n):
        super().__init__(n)

    def print(self, docName):
        print('>> LaserPrinter.print')
        print('Trying to print:', docName)

class InkjetPrinter(Printer):
    def __init__(self, n):
        super().__init__(n)

    def print(self, docName):
        print('>> InkjetPrinter.print')
        print('Trying to print:', docName)

p = LaserPrinter('LaserJet 1100')
p.print('hello1.pdf')
p = InkjetPrinter('IBM 2140')
p.print('hello2.doc')