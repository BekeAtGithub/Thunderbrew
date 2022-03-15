# functions for actions that the user can use
# for invalid user input - the program will return a list of all available inputs
# will have functions that will put items into inventory when processed
# farm hops will add 1 hop into inventory every 2 seconds

from tkinter import Y
import math

# Invalid User Input Function

#add color coded fun letters
print("Here is a list of available input options:")
print("farm - Used to collect farmable ingredients")
print("mine - Used to collect mineable ingredients")
print("craft - Used to combine items to create other items")
print("inventory - Shows all items the inventory contains")
print("items - Lists a collection of all available items")
print("quit - exits the program")

# Farm Function: farm - Used to collect farmable ingredients



# Mine Function: mine - Used to collect mineable ingredients



# Craft Function: craft - Used to combine items to create other items
# when typing in options of what ingredients to use - it will let you keep typing in lines until you type "done" to complete the input list

def CraftingList():
    print ">>> Crafting List <<<"
    print "1. "
    print "2. "
    print "3. "
    print "4. "
    print "5. "
    print "6. "
    print "7. "
    print "8. "
    print "9. "
    print "10."
    print "11."
    print "Which one do you want to craft?"
    print
    return raw_input(">>> ")


def CraftItem(inventory,required_materials,crafted):
    amtcount = []
    amtcountunique = []
    consumestr = ""
    for i in range(len(required_materials)):
        if required_materials[i] not in amtcountunique:
            amtcount.append([required_materials[i],1])
            amtcountunique.append(required_materials[i])
        else:
            for x in amtcount:
                if required_materials[i] == x[0]:
                    x[1]+=1
    for i in amtcount:
        consumestr = consumestr + str(i[1])+" x "+str(i[0]) + " "
    craftedstr = str(crafted[1])+" x "+str(crafted[0])
    print "Crafting "+str(craftedstr)+" will consume "+str(consumestr)
    print "Are you sure?"
    confirmation = raw_input("Y / N >>> ")
    if confirmation.lower() == "y":
        try:
            for i in required_materials:
                inventory.remove(i)
            for i in range(int(crafted[1])):
                inventory.append(crafted[0])
            return inventory
        except:
            print "You are missing some ingredients"
            return inventory


def FireMethod(inventory):
    items = ['', '', '', '']
    ownedlighting = []
    for i in inventory:
        if i in lightingitems:
            ownedlighting.append(i)
    print "You have these items:"
    DisplayInventoryTry2(ownedlighting)
    print "Which one do you want to use?"
    tolight = raw_input(">>> ").lower()
    found = False
    for i in ownedlighting:
        if tolight == i.lower():
            removeitem = i
            found = True
    if not found:
        print "You cannot you do not have the item"
    for i in inventory:
        if i == '':
            if tolight == '':
                inventory.remove(removeitem)
            else:
                pass
            inventory.remove('')
    return inventory


def UseableItemsOutput(inventory):
    useableitems = ['','','']
    useableowned = []
    for i in inventory:
        if i in useableitems:
            useableowned.append(i)
    if len(useableowned) != 0:
        print 'You own these useable items:'
        DisplayInventoryTry2(useableowned)
        print ">>> Which one do you want to use? <<<"
        use = raw_input("Please type in the full item name >>> ").lower()
        for i in useableowned:
            if use == i.lower():
                inventory.remove(i)
                return [inventory,i]
                break
    else:
        print 'You do not own any useable items'


def UsedItem(,useitem):
    import time
    useableitems = ['', '', '']
    if useitem not in useableitems:
        print "Error 001, item to use is not in the Useable Items List!"
        print "Creating Crash Log."
        f = open('CrashLog: Error 001','a+')
        f.writelines(time.asctime())
        f.writelines('Item To Use: '+useitem)
        f.close()
        raise ValueError,'item to use is not in the Useable Items List!'
    else:
        if useitem == useableitems[0]:
            hydration = 100
            print ""
        elif useitem == useableitems[1]:
             = 100
            print ""
        elif useitem == useableitems[2]:
             -= 30
            print ""
        return [,,]




# Inventory Function: inventory - Shows all items the inventory contains



# Items Function: items - Lists a collection of all available items



# Quit Function: quit - exits the program
# use quit() to exit game