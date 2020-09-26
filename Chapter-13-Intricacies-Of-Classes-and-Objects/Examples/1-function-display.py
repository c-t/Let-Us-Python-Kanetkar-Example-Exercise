def display():
    """Display a message"""
    print('Hello')
    print(display.__doc__)

def show(msg1 = '', msg2 = ''):
    """
    Display 2 messages.

    Arguments:
    msg1 -- message to be displayed in lowercase (default '')
    msg2 -- message to be displayed in uppercase (default '')
    """
    print(msg1.lower())
    print(msg2.upper())
    print(show.__doc__)

display()
show('Cindrella', 'Mozrella')
help(display)
help(show)