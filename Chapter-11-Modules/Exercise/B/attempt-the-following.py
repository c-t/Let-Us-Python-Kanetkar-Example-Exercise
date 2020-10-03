"""
Attempt the following:
a. What is the purpose behind creating multiple packages and modules?
   - ease of development and maintenance
   - reuse of existing code
b. By default, to which module do the statements in a program belong?
   __main__
   How do we access the name of this module?
   print(__main__)
c. In the following statement what do a, b,c, x represent?
   import a.b.c.x
   classes - a, b, c
   x - method
d. If module m contains a function fun(), what is wrong with the following statement?
   import m
   fun()    # should be m.fun()
e. What is the purpose of built-in functions dir(), vars(), global(), and local()?
    dir() - list of attributes in module
    vars() - dict of names in module
    global() - identifiers in global namespace
    local() -  identifiers in local namespace
f.  What are the contents of PYTHONPATH variable?
    PYTHONPATH is an environment variable set to add additional directories where python looks for modules and packages.
    How can we access its contents programmatically?
    import sys
    print(sys.path) # this approach is platform independent
g.  What does the content of sys.path signify?
    A list of strings that specifies the search path for modules. Initialized from the environment variable PYTHONPATH,
    plus an installation-dependent default.
    What does the order of contents of sys.path signify?
    Python searches the paths in the order in which they are listed in sys.path.
h.  What will be the output of the following program?
    var = 1.1
    print(var)  #output - 1.1

    def fun():
        var = 2.2
        print(Var)      #output - 2.2

    fun()               #output - 2.2
    print(var)          #output - 1.1
i. Do the following import statements serve the same purpose? - Yes
    # version 1
    import a, b, c

    # version 2
    import a
    import b
    import c

    # version 3
    from a import *
    from b import *
    from c import *
"""
