class Weather:
    def __init__(self):
        self._params = ['Temp', 'Rel Hum', 'Cloud Cover', 'Wind Vel']
    def __contains__(self, p):
        return True if p in self._params else False

w = Weather()
if 'Rel Hum' in w:
    print('Valid weather parameter')
else:
    print('Invalid weather parameter')

# To overload the in operator we need to define the function __contains__()