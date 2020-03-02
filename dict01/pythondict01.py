#!/usr/bin/python3

switch = {"hostname": "sw1", "ip": "10.0.0.1", "version": "1.2", "vendor": "cisco"}

print ( switch ["hostname"] )
print ( switch ["ip"] )
#print ( switch ["lynx" )
print ( "First test - .get()" )
print ( switch.get("lynx") )
print ( "secnd text - .get()")
print ( switch.get('lynx', "THE KEY IS IN ANOTHER CASTLE"))
print ( "Third test - .get()" )
print ( switch.get("version"))
print ("test4")
print (switch.keys())
print ("test5")
print (switch.values())
print ("test6")
print (switch.pop("version"))
print (switch.keys())
print (switch.values())
print ("test7")
switch["adminlogin"] = "karl08"
print(switch.keys())
print(switch.values())
print ("test8")
switch["password"] = "qwerty"
print (switch.keys())
print (switch.values())
