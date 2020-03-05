#!/usr/bin/python3
cfgfile=input("Configfile?")

with open(cfgfile, "r") as configfile:
    configlist = configfile.readlines()
print(configlist)
print(len(configlist))
