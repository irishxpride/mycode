#!/usr/bin/python3
loginfail = 0
keystone_file = open("./keystone.common.wsgi")
keystone_file_lines = keystone_file.readlines()
for line in keystone_file_lines:
    if "- -] Authorization" in line:
        loginfail += 1
print ("The number of failed login attempts is", loginfail)
keystone_file.close()
