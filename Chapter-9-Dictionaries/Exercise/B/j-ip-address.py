"""
Create a dictionary which stores the following data:

Interface   IPAddress  status
eth0        1.1.1.1     up
eth1        2.2.2.2     up
wlan0       3.3.3.3     down
wlan1       4.4.4.4     up


WAP to perfrom the following operations:
- Find the status of a given interface
- Find the interface and IP of all interfaces which are up
- Find the total number of interfaces
- Add two new entries to the dictionary
"""

interfaces = {('eth0', '1.1.1.1'): 'up', ('eth1', '2.2.2.2'): 'up', ('wlan0', '3.3.3.3') : 'down', ('wlan1', '4.4.4.4'): 'up'}

interface = input('Enter the interface: ')
