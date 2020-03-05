#!/usr/bin/python3
import netifaces
def mac (i):
    print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr'])

def IP (i):
    print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])

for i in netifaces.interfaces():
    print('\n************Details of interface - ' + i + ' ************')
    try:
        print('MAC: ', end='')
        mac(i)
#        print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr'])
        print('IP: ', end='')
        IP(i)
#        print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])
    except:
        print('could not collect adapter information for ' + i)
