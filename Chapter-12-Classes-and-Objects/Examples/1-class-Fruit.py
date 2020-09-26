class Fruit:
    count = 0

    def __init__(self, name = '', size = 0, color = ''):
        self._name = name
        self._size = size
        self._color = color
        Fruit.count += 1

    def display():
        print(Fruit.count)

f1 = Fruit('Banana', 5, 'Yellow')
f2 = Fruit('Orange', 4, 'Orange')
f3 = Fruit('Apple', 3, 'Red')

Fruit.display()
print(Fruit.count)

# count is a class attribute, not an object attribute
# to be initialized as count = 0, butmust be accessed using Fruit.count