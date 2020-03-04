#!/usr/bin/python3
dnsfile = open("dnsservers.txt", "r")

dnslist = dnsfile.readlines()

for svr in dnslist:
    print (svr, end="")
dnsfile.close()
