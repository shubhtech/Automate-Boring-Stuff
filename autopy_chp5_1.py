stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():     
        item_total = item_total + inventory.get(k, 0)          #count individual key items
    print("Total number of items: " + str(item_total))

displayInventory(stuff)