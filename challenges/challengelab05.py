#!/usr/bin/python3

lieBool = ''
buttBool = ''

butts = input("Do you like big butts(yes/no)?\n")
lie = input ("Can you lie(yes/no)?\n")
if not (butts) or not (lie):
    print ("\n\nIt's no fun if you don't answer both questions.")
    exit()

if( butts.lower() == "yes") or (butts.lower() =="y"):
    buttBool = 1

elif not ((butts.lower() == "no") or (butts.lower() == "n")):
    print ("\n\nI have no idea what to do with that, please answer yes or no")
    exit()

if ( lie.lower() == "yes") or (lie.lower() =="y"):
    lieBool = 1

elif not ((lie.lower() == "no") or (lie.lower() == "n")):
    print ("\n\nI have no idea what to do with that, please answer yes or no")
    exit()

if (buttBool):
    if (lieBool):
        print(f"\n\nI find you untrustworthy")
    else:
        print(f"\n\nYou have a lot in common with Sir Mix-a-Lot")

else:
    if (lieBool):
        print(f"\n\nI think you're fibbing")
    else:
        print(f"\n\nThat seems unlikely, but you seem trustworthy")
