#!/usr/bin/python3
ipchk=input ("Apply an IP Address: ")

if ipchk == "192.168.70.1":
    print (f"Looks like the Gateway was set to {ipchk}. This is not recommended.")
elif ipchk:
    print (f"Looks like the IP was set to {ipchk}.")
else:
    print("You failed to provide input")


