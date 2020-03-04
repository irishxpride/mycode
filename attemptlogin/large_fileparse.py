#!/usr/bin/python3
loginfail = 0
loginsuccess = 0
with open("./keystone.common.wsgi") as kfile:

    for line in kfile:
        if "- -] Authorization" in line:
            loginfail += 1
            print(f'Failed Login attempt from IP: {line.split("from ")[1]}')
        elif "-] Authorization" in line:
            loginsuccess += 1

print ("The number of failed login attempts is", loginfail)
print ("The number of successful login attempts is", loginsuccess)
