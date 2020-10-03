"""
Rewrite the import statements in Prog 11.3, such that using functions in different modules becomes convenient.
"""
# client.py
from messages_mod.funny.modf1 import funf1
from messages_mod.funny.modf2 import funf2
from messages_mod.funny.modf3 import funf3

from messages_mod.curt.modc1 import func1
from messages_mod.curt.modc2 import func2
from messages_mod.curt.modc3 import func3

funf1()
funf2()
funf3()

print('')

func1()
func2()
func3()
