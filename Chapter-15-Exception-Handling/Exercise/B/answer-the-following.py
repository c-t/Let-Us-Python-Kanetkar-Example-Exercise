"""
a. If we do not catch the exception thrown at runtime then who will catch it?
   Python runtime
b. Explain in short most compelling reasons fro using exception handling over conventional error handling approaches.
   Exception handling is an object oriented way of handling errors.
c. Is it necessary that all classes that can be used to represent exceptions be derived from base class exception?
   Yes
d. What is the use of a finally block in Python exception handling sequence?
   performs cleanup operations
e. How does nested exception handling work in Python?
   by using try-except
f. Program file is provided as a separate file.
g. What's wrong with the following code snippet?
    try:
        # some statements
    except:
        # report error 1
    except ZeroDivisionError:
        # report error 2

    order is incorrect. First 'except' captures all exceptions, the second one will never get executed.
h. Which of these keywords is not part of Python's exception handling - try, catch, throw, raise, finally, else?
   catch, throw, and raise
j. What will be the output of the following code?
   def fun():
    try:
        return 10
    finally:
        return 20

    k = fun()
    print(k)

    output will be 20.
"""