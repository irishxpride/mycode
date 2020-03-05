#!/usr/bin/python3

configfile=open("vlanconfig.cfg", "r")
configblog=configfile.read()

configlist = configblog.splitlines()
print(configlist)
configfile.close

