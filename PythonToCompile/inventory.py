'''
Created by Akshat G. to keep inventory during COVID-19 outbreak
by the Human Tech Project
'''
from datetime import *
from math import *
from operator import itemgetter
add = False
inventory = False
search = False
delete = False
print("Welcome to the inventory system")

print("Type one or multiple of the following:")
print("     'a' : add items")
print("     's' : show items")
print("     'd' : delete items")
print("     'f' : find items")
print("Example: 'asdf' would do everything")
action = input("What do you want to do? :  ")
print()

for i in action:
    if i == "a":
        add = True
    elif i == "s":
        inventory = True
    elif i == "f":
        search = True
    elif i == "d":
        delete = True

items = {}

with open('inventory.txt','r+') as file:
    for line in file:
        data = line.split(":")
        items[data[0].strip()] = data[1].strip()

def additem():
    done = False
    while done == False:
        itemname = input("Item Name: ")
        if itemname == "exit":
            done = True
        else:
            expdate = input("Exp Date: ")
            items[itemname] = expdate
    print()
    showitems()
    print()

def showitems():
    file = open("inventory.txt","w")
    file.write("")
    file.close()
    file = open("inventory.txt","a")
    for key, value in sorted(items.items(), key = itemgetter(1)):
        print("{:<20}".format(key), value)
        keyval = str(key) + " : " + str(value)
        file.write(keyval)
        file.write("\n")
        items[key] = value
    file.close()
    print()
    
def searchitem():
    searchitem = input("What item are you looking for? ")
    data = items.get(searchitem, None)
    if data:
        print(searchitem,", your item, is available in the inventory")
    else:
        print(searchitem,", your item, is not currently available in the inventory")
    print()

def delitem():
    itemtodel = input("Which item has to be deleted? ")
    data = items.pop(itemtodel, None)
    if itemtodel == "clear":
        items = {}
    elif data:
        print(itemtodel,", your item, has been deleted")
    else:
        print(itemtodel,", your item, not found")
    print()
    showitems()
    print()

def calcexp():
    for i in items:
        expdate = items[i]
        data = expdate.split(".")
        day = data[1]
        month = data[0]
        year = data[2]
        x = datetime.now()
        currday = [x.strftime("%m"),x.strftime("%d"),x.strftime("%Y")]
        d1 = date(int(currday[2]),int(currday[0]),int(currday[1]))
        d2 = date(int(year),int(month),int(day))
        diff = d2-d1
        if diff.days <= 7 and diff.days >= 0:
            print()
            print("*** Reminder:",i,"expire in",diff.days,"days ***",)
    print()


if inventory == True:
    showitems()
if add == True:
    additem()
if search == True:
    searchitem()
if delete == True:
    delitem()

calcexp()
