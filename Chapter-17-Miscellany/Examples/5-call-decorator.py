def calldecorator(func):
    def _decorated(*arg, **kwargs):
        print(f'Calling {func.__name__}{arg},{kwargs})')
        ret = func(*arg, **kwargs)
        print(f'Called {func.__name__}{arg},{kwargs}) got ret val:{ret}')
        return ret
    return _decorated

@calldecorator
def sum_num(arg1, arg2):
    return arg1+arg2

@calldecorator
def prod_num(arg1, arg2):
    return arg1*arg2

@calldecorator
def message(msg):
    pass

sum_num(10, 20)
prod_num(10, 20)
message('Errors should never pass silently')