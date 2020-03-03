#!/usr/bin/python3

hostname = input("What value should we set for hostname?")

if hostname.lower() == "mtg":
    print (f"the hostname was entered as {hostname}")
    print (f"the hostname was changed to {hostname.lower()} before assessment")

else:
    print (f"You entered {hostname}, which does not work for our purposes")

print(f"Exiting the script. The entered hostname was {hostname}")

