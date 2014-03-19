import os
from time import time
from datetime import datetime


order = {}
filelist = {}
is_saved = False #used to check if tha latest changes are saved
load_count = 0 #used to check if load is already invoked
finish_count = 0 #used to check if finish is already invoked
command = input("Enter command>")
command = command.split()

while True:
    if command[0] == 'take':
        is_saved = False
        name = command[1]
        price = float("%.2f" % float(command[2]))
        if name in order.keys():
            order[name] += price
        else:
            order[name] = price
        print ("Taking order from %s for %.2f" %(name, price))
    elif command[0] == 'status':
        for person in order:
            print("%s - %.2f" %(person, order[person]))
    elif command[0] == 'save':
        is_saved = True
        ts = time()
        filename = 'orders_' + datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
        data = ["%s - %.2f" %(person, order[person]) for person in order]
        file = open(filename, "w")
        file.write("\n".join(data))
        file.close()
        print("Saved the current order to %s" %(filename))
    elif command[0] == 'list':
        files = [f for f in os.listdir('.') if os.path.isfile(f) if 'orders' in f]
        for i, name in enumerate(files):
            filelist[i + 1] = name
            print ("[%s] - %s" %(str(i + 1), name))
    elif command[0] == 'load':
        number = int(command[1])
        if not filelist:
            print("Use list command before loading")
        elif not is_saved and not load_count:
            print("You have not saved the current order.\nIf you wish to discard it, type load <number> again.")
            load_count = 1
        elif not order or load_count:
            load_count = 0
            order = {}
            filename = filelist[number]
            file = open(filename, "r")
            for line in file:
                record = line.split()
                name = record[0]
                price = float("%.2f" % float(record[2]))
                order[name] = price
            file.close()
            print("Loading %s" %(filename))
    elif command[0] == 'finish':
        if not is_saved and not finish_count:
            print("You have not saved your order.\nIf you wish to continue, type finish again.\nIf you want to save your order, type save")
            finish_count = 1
        elif is_saved or finish_count:
            break
    else:
        print("Unknown command!\nTry one of the following:\ntake <name> <price>\nstatus\nsave\nlist\nload <number>\nfinish")
    command = input("Enter command>")
    command = command.split()

