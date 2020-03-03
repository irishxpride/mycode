#!/usr/bin/python3

hostname = input("What value should we set for hostname?")

if hostname.lower() == "mtg":
    print (f"the hostname was entered as {hostname}")
    print (f"the hostname was changed to {hostname.lower()} before assessment")

print(f"Exiting the script. The entered hostname was {hostname}")

