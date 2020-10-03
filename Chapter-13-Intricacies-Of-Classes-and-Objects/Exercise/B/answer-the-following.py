"""
a. Which functions should be defined to overload the + and - operators?
   + => __add__(self, other)
   - => __sub__(self, other)

b. Which functions should be defined to overload the / and // operators?
   / => _truediv(self, other)
   // => _floordiv(self, other)

c. What is the purpose of id() function?
   returns the location of object in memory.
   e.g. i = 45
   print(type(i), id(i))
   output => <class 'int'> 43452345
   <class 'int'> => type of object
   43452345 => location of object in memory

d. How will you define a structure Employee containing attributes Name, Age, Salary, Address, Hobbies dynamically?
   class Employee:
        pass

    b = Employee()

    # creating attributes dynamically
    b.Name = "Arnold"
    b.Age = 75
    b.Salary = 500000
    b.Address = "Hollywood"
    b.Hobbies = "Body building"

e. Is it necessary to mention the docstring for a function immediately below the def statement?
   Yes.
   docstring is available in variable __doc__
"""