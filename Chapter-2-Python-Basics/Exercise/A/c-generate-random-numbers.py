# Generate 5 random numbers
# import random
# random.seed(6)
# print(random.randint(5,50))
# print(random.randint(5,50))
# print(random.randint(5,50))
# print(random.randint(5,50))
# print(random.randint(5,50))

# above solution gives same set of random numbers everytime
# to change the seed everytime, seed can be associated with time or execution
import random
from datetime import datetime
random.seed(datetime.now())
print(random.randint(5,50))
print(random.randint(5,50))
print(random.randint(5,50))
print(random.randint(5,50))
print(random.randint(5,50))