inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToInventory(inventory, addedItems):
    for item in dragonLoot:
        if item not in inventory:
            inventory.setdefault(item, 1)
        else:
            inventory[item] += 1
    return inventory

def displayInventory(inventory):
    print ('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print (str(v)+' ' + k)
        item_total = item_total + inventory.get(k, 0)
    print("Total number of items: " + str(item_total))
    print (inv)

inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
