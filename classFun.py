#Fire Emblem Alex Legion
#Text based game based on Fire Emblem
#Programmed by You Zhou

from random import randint
from festaples import *
from feclasses import *
from feweapons import *
import copy
allies = []
enemies = []
name = input("Enter your name:\n")
name = name.upper()
askingclass = True
askmsg = "Enter your class (mage,knight,myrmidon) or info for more info:\n"
#^msg asked to user in askingclass loop

#----common weapons and items----#
iron_lance = Weapon("Iron Lance",7,8,45,80,"Lance",100)
fire = Weapon("Fire",5,4,40,95,"Anima",100,0,1,True,"",2)
slim_sword = Weapon("Slim Sword",3,2,35,100,"Sword",200,5)
iron_sword = Weapon("Iron Sword",5,5,47,90,"Sword",100)
iron_axe = Weapon("Iron Axe",8,10,45,75,"Axe",100)
vulnerary = Item("Vulnerary",3,"Heals for 10 HP")

#asking user for class
while askingclass:
    playerclass = input(askmsg)
    if playerclass.lower() == "mage":
        player = Mage(name,18,5,6,5,5,2,5,4,[60,40,60,55,50,20,50])
        player.add_item(copy.deepcopy(fire),False)
        player.equip_w(player.items[0],False)
        player.wskl["Anima"] = 200
        askingclass = False
    if playerclass.lower() == "knight":
        player = Knight(name,21,6,4,4,3,6,1,10,[80,55,50,35,40,55,20])
        player.add_item(copy.deepcopy(iron_lance),False)
        player.equip_w(player.items[0],False)
        player.wskl["Lance"] = 200
        askingclass = False
    if playerclass.lower() == "myrmidon":
        player = Myrmidon(name,20,5,6,6,4,4,2,5,[70,40,60,60,45,25,30])
        player.add_item(copy.deepcopy(slim_sword),False)
        player.equip_w(player.items[0],False)
        player.wskl["Sword"] = 200
        askingclass = False
    if playerclass.lower() == "info":
        print("""Mage - A speedy and accurate user of anima magic. Can't really take physical hits, although magical defense is high. Melts enemies with low resistance.
Knight - A tanky but slow lance-wielder. Strong but inaccurate. Low resistance.
Myrmidon - A speedy sword user. Very skillfull with the sword art, but dies easily.""")
        askmsg = "Enter your class (mage,knight,myrmidon) or info for more info:\n"      
    else:
        askmsg = "Your entry is invalid. Please enter mage, knight, myrmidon or info:\n"
player.sym = "P"
player.x = 3
player.y = 2
allies.append(player)
#creating enemy1
enemy1 = Murderer("Enemy 1",20,6,2,2,0,3,0,8)
enemy1.canLevel = False
enemy1.gift = 40
enemy1.add_item(copy.deepcopy(iron_axe),False)
enemy1.equip_w(enemy1.items[0],False)
enemy1.sym = "E"
enemy1.wskl["Axe"] = 200
enemy1.x = 2
enemy1.y = 2
enemies.append(enemy1)
lvl1map = [["." for i in range(15)]for i in range(12)] #level 1 map
reg_map = [] #regular map
stat_map = copy.deepcopy(reg_map) #static map - never changes
chapter = 1 #chapter we're on
turn = 1
#creating franny
franny = Cavalier("Franny",22,6,7,6,5,4,3,8,[85,40,55,55,35,35,25])
franny.level = 3
franny.wskl["Lance"] = 200
franny.wskl["Sword"] = 200
franny.add_item(copy.deepcopy(iron_lance),False)
franny.add_item(copy.deepcopy(iron_sword),False)
franny.add_item(copy.deepcopy(vulnerary),False)
franny.equip_w(franny.items[0],False)
franny.sym = "F"
franny.x = 3
franny.y = 7
allies.append(franny)

running = True
#main game loop
while running:
    if chapter == 1 and turn == 1:
        reg_map = copy.deepcopy(lvl1map)
        stat_map = copy.deepcopy(lvl1map)
    for a in allies:
        reg_map[len(reg_map)-1-a.y][a.x] = a.sym
    for e in enemies:
        reg_map[len(reg_map)-1-e.y][e.x] = e.sym
    comm = input("Enter a command:\n")
    if comm.upper() == "QUIT":
        running = False
        print("You have quit and lost all progress")
    elif comm.upper() == "ATTACK":
        asking = True
        askingmsg = "Select an ally to attack with: "
        while asking:
            print(askingmsg)
            print("===============================")
            for a in allies:
                isplayer = "(enter me, not this name)" if a == player else ""
                print(a.name,isplayer)
            print("===============================")
            ally = input()
            if ally.lower() == "cancel":
                asking = False
                print("Attack function cancelled")
                break
            for a in allies:
                if ally.upper() == a.name.upper() or (ally.upper() == "ME" and a == player):
                    #action that takes place
                    #displays all stats
                    print("===============================")
                    for e in enemies:
                        print(e.name)
                    print("===============================")
                    asking = True
                    askmsg = "Pick enemy to attack: "
                    while asking:
                        enemy = input(askmsg)
                        if enemy.lower() == "cancel":
                            asking = False
                            print("Attack with",a.name,"cancelled")
                            break
                        for e in enemies:
                            if e.name.lower() == enemy.lower():
                                #ATTACK CODE
                                a.attack(e)
                                e.attack(a)
                                if a.speed >= e.speed + 4 and e.alive:
                                    a.attack(e)
                                elif a.speed <= e.speed - 4 and a.alive:
                                    e.attack(a)
                                asking = False
                                if not a.alive:
                                    allies.remove(a)
                                if not e.alive:
                                    enemies.remove(e)
                                if not player.alive:
                                    print("GAME OVER")
                                    running = False #gonna change this to level restart
                                break
                        askmsg = "Invalid enemy, input a valid enemy name: " 
                    asking = False
                    break
                else:
                    askingmsg = "Not a valid ally. Select an ally to display info:"
    elif comm.upper() == "END":
        turn += 1 #add enemy's turn here
    elif comm.upper() == "DISPLAY":
        #print enemy or ally info. So far only allies done
        asking = True
        askingmsg = "Select a unit to display info:"
        while asking:
            print(askingmsg)
            print("===============================")
            print("----ALLIES-----")
            for a in allies:
                print(a.name)
            print("----ENEMIES----")
            for e in enemies:
                print(e.name)
            print("===============================")
            unit = input()
            if unit.lower() == "cancel":
                print("Display function cancelled")
                asking = False
                break
            for u in allies+enemies:
                if unit.upper() == u.name.upper():
                    #action that takes place
                    #displays all stats
                    u.display()
                    asking = False
                    break
            else:
                askingmsg = "Not a valid ally. Select an ally to display info:"
    elif comm.upper() == "MAP":
        #print map
        showMap(reg_map)
    elif comm.upper() in ["CALC","CALCULATE"]:
        asking = True
        askingmsg = "Select an ally to calculate with: "
        while asking:
            print(askingmsg)
            print("===============================")
            for a in allies:
                print(a.name)
            print("===============================")
            ally = input()
            if ally.lower() == "cancel":
                asking = False
                print("Calculation function cancelled")
                break
            for a in allies:
                if ally.upper() == a.name.upper() or (ally.upper() == "ME" and a == player):
                    #action that takes place
                    #displays all stats
                    print("===============================")
                    for e in enemies:
                        print(e.name)
                    print("===============================")
                    asking = True
                    askmsg = "Pick enemy to calculate against: "
                    while asking:
                        enemy = input(askmsg)
                        if enemy.lower() == "cancel":
                            asking = False
                            print("Calculation with",a.name,"cancelled")
                            break
                        for e in enemies:
                            if e.name.lower() == enemy.lower():
                                a.calculate(e)
                                print("----------------------")
                                e.calculate(a)
                                asking = False
                                break
                        askmsg = "Invalid enemy, input a valid enemy name: " 
                    asking = False
                    break
            else:
                askingmsg = "Not a valid ally. Select an ally to display info:"
    elif comm.upper() == "MOVE":
        asking = True
        askmsg = "Pick ally to move: "
        while asking:
            print("===============================")
            for a in allies:
                print(a.name)
            print("===============================")
            ally = input(askmsg) #ally selected by user
            if ally == "cancel":
                print("Ally movement cancelled")
                asking = False
                break
            for a in allies:
                if (ally.lower() == "me" and a == player) or ally.lower() == a.name.lower():
                    flying = True if a.CLASS in ["Pegasus Knight","Wyvern Rider","Wyvern Lord","Falcoknight"] else False
                    waterproof = True if a.CLASS in ["Pirate","Berserker"] else False
                    move_map = moveDisp(a.x,a.y,a.MOVE+1,a.MOVE+1,reg_map,flying,waterproof)
                    showMap(move_map) 
                    while True:
                        xmove = 0#where user wants to move unit
                        ymove = 0
                        try:
                            xmove = int(input("What's the X co-ord of where you move?\n"))
                            ymove = int(input("What's the Y co-ord of where you move?\n"))
                        except Exception:
                            print("You must enter an integer!")
                            continue
                        if xmove >= len(reg_map[0]):
                            print("X value too large!")
                        elif xmove < 0:
                            print("X value too small!")
                        elif len(reg_map)-ymove-1 >= len(reg_map):
                            print("Y value too large!")
                        elif len(reg_map)-ymove-1 < 0:
                            print("Y value too small!")
                        elif not reg_map[len(reg_map)-ymove-1][xmove] in [str(i) for i in range(1,10)]:
                            print("Not a moveable square!")
                        else:
                            reg_map[len(reg_map)-a.y-1][a.x] = stat_map[len(reg_map)-a.y-1][a.x] #removes ally symbol from place moved from and reverts to normal as found on static map
                            a.x = xmove
                            a.y = ymove
                            reg_map[len(reg_map)-ymove-1][xmove] = a.sym
                            print("Moved",a.name,"to (",xmove,",",ymove,")")
                            asking = False
                            break
    elif comm.upper() == "HELP":
        print("""QUIT - leave the game (why would u do that?)
DISPLAY - display an units name
CALCULATE - calculate an ally against an enemy
MAP - Display map
MOVE (INC) - Move an ally
ATTACK (Movement date INC) - What do you think it does? Heal?
END - Ends your turn, and then enemies can attack you. Be careful when you do this man.""")
    else:
        print("Invalid command")
