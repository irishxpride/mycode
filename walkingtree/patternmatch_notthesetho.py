#!/usr/bin/python3
import os, fnmatch

EXCLUDE = ["/usr", "/home", "/var"]

def find(info):
    result = []
    for root, dirs, files in os.walk(info[1], topdown=True):
        if root in EXCLUDE:
            dirs[:] = []
            files[:] = []
        for name in files:
            if fnmatch.fnmatch(name, info[0]):
                result.append(os.path.join(root, name))
    return result
def lkfor():
    lkresult = []
    lookfor = input("What am I looking for? ")
    lkresult.append(lookfor)
    lookwhere = input("What is the path in which I should search? ")
    lkresult.append(lookwhere)
    return lkresult

def main():
    print(find(lkfor()))
main()
