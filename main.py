#Fire Emblem Alex Legion
#Text based game based on Fire Emblem
#Programmed by You Zhou

from random import randint
from festaples import *
from feclasses import *
from feweapons import *
from festory import *
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
rapier = Weapon("Rapier",7,5,40,90,"Sword",700,10,1,False,["Cavalier","Paladin","Knight","General"],1,5,"Effective against knights, cavalry","Yoyo")
vulnerary = Item("Vulnerary",3,"Heals for 10 HP")

#--------Common terrain----------#
plain = Terrain("Plain",".")
forest = Terrain("Forest","|",20,1,1)
#asking user for class
#creating player's class
while askingclass:
    playerclass = input(askmsg)
    if playerclass.lower() == "mage":
        player = Mage(name,18,5,6,6,6,2,5,4,[60,40,60,55,50,20,50])
        player.add_item(copy.deepcopy(fire),False)
        player.wskl["Anima"] = 200
        askingclass = False
    if playerclass.lower() == "knight":
        player = Knight(name,21,7,4,4,3,6,1,10,[80,55,45,35,40,55,20])
        player.add_item(copy.deepcopy(iron_lance),False)
        player.wskl["Lance"] = 200
        askingclass = False
    if playerclass.lower() == "myrmidon":
        player = Myrmidon(name,20,5,6,7,4,4,2,5,[70,40,60,60,45,25,30])
        player.add_item(copy.deepcopy(slim_sword),False)
        player.wskl["Sword"] = 200
        askingclass = False
    if playerclass.lower() == "info":
        print("""Mage - A speedy and accurate user of anima magic. Can't really take physical hits, although magical defense is high. Melts enemies with low resistance.
Knight - A tanky but slow lance-wielder. Strong but inaccurate. Low resistance.
Myrmidon - A speedy sword user. Very skillfull with the sword art, but dies easily.""")
        askmsg = "Enter your class (mage,knight,myrmidon) or info for more info:\n"      
    else:
        askmsg = "Your entry is invalid. Please enter mage, knight, myrmidon or info:\n"
player.equip_w(player.items[0],False)
player.sym = "P"
player.x = 3
player.y = 2
allies.append(player)

lvl1map = [["." for i in range(15)]for i in range(12)] #chapter 1 map
lvl1map[5][5],lvl1map[5][6],lvl1map[4][6] = "|","|","|"
lvl1_elem = [copy.deepcopy(plain),copy.deepcopy(forest)] #all types of terrain in chapter 1
reg_map = [] #regular map
stat_map = copy.deepcopy(reg_map) #static map - never changes
chapter = 0 #chapter we're on
turn = 1
#creating franny
franny = Cavalier("Franny",22,6,8,7,5,5,3,8,[85,45,55,55,40,35,25])
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
#allies.append(franny)
#creating You Zhou
yoyo = Lord("Yoyo",18,5,7,5,7,2,4,5,[60,40,65,40,70,20,45])
yoyo.add_item(copy.deepcopy(rapier),False)
yoyo.wskl["Sword"] = 200
yoyo.wskl["Anima"] = 100
yoyo.equip_w(yoyo.items[0],False)
yoyo.add_item(copy.deepcopy(fire),False)
yoyo.sym = "Y"
yoyo.add_item(copy.deepcopy(vulnerary),False)
yoyo.x = 3
yoyo.y = 3
allies.append(yoyo)
attackers = [] #units that can attack this turn
attackers.append(player)
attackers.append(yoyo)
movers = [] #units that can move this turn
movers.append(player)
movers.append(yoyo)
running = True
prologueStory(player.name) #story for prologue
start = True
#main game loop
while running:
    #---------Prologue initialization-------#
    if chapter == 0 and start:
        #chapter 1 initialization
        #all terrain list
        all_terr = copy.deepcopy(lvl1_elem)
        #creating enemy1
        enemy1 = Brigand("Bandit 1",20,6,2,2,0,3,0,8)
        enemy1.canLevel = False
        enemy1.gift = 40
        enemy1.add_item(copy.deepcopy(iron_axe),False)
        enemy1.equip_w(enemy1.items[0],False)
        enemy1.sym = "E"
        enemy1.x = 2
        enemy1.y = 2
        enemies.append(enemy1)
        #initializing dynamic map (units) and static map (terrain)
        reg_map = copy.deepcopy(lvl1map)
        stat_map = copy.deepcopy(lvl1map)
        start = False
    for a in allies:
        reg_map[len(reg_map)-1-a.y][a.x] = a.sym
    for e in enemies:
        reg_map[len(reg_map)-1-e.y][e.x] = e.sym
    comm = input("Enter a command:\n")
    #--------------QUIT----------------#
    if comm.upper() == "QUIT":
        running = False
        print("You have quit and lost all progress")
    #--------------ATTACK--------------#
    elif comm.upper() == "ATTACK":
        #attack function
        a = askUser("Select ally to attack with: ",attackers,player,"allies that can attack")
        userwants = True
        if a == "cancel":
            userwants = False
        if userwants:
            attackable = []
            for en in enemies:
                distx = abs(en.x - a.x)
                disty = abs(en.y - a.y)
                dist = distx + disty
                #distance from enemy to ally
                if a.equip.rnge <= dist <= a.equip.maxrnge:
                    attackable.append(en)
            e = askUser("Select enemy to attack: ",attackable,player,"attackable enemies",True)
            if e == "cancel":
                userwants = False
        if userwants:
        #ATTACK CODE
            eter_avo = 0 #enemy terrain avoid and defense
            eter_def = 0
            ater_avo = 0 #ally terrain avoid and defense
            ater_def = 0
            #determining which terrain unit is standing on
            for t in all_terr:
                if stat_map[len(stat_map)-1-e.y][e.x] == t.sym:
                    eter_avo = t.avo
                    eter_def = t.defen
                if stat_map[len(stat_map)-1-a.y][a.x] == t.sym:
                    ater_avo = t.avo
                    ater_def = t.defen
            a.attack(e,ater_avo,ater_def)
            e.attack(a,eter_avo,eter_def)
            if a.speed >= e.speed + 4 and e.alive:
                a.attack(e)
            elif a.speed <= e.speed - 4 and a.alive:
                e.attack(a)
                asking = False
            if not a.alive:
                allies.remove(a)
                reg_map[len(reg_map)-1-a.y][a.x] = stat_map[len(stat_map)-1-a.y][a.x]
            if not e.alive:
                enemies.remove(e)
                reg_map[len(reg_map)-1-e.y][e.x] = stat_map[len(stat_map)-1-e.y][e.x]
            if not player.alive:
                print("GAME OVER")
                running = False #gonna change this to level restart, for now it kills the program
            attackers.remove(a) #makes sure each unit can only attack once per turn
            if a in movers:
                movers.remove(a)
    #----------DISPLAY----------#
    elif comm.upper() == "DISPLAY":
        #print enemy or ally info
        a = askUser("Select unit to display info: ",allies+enemies,player)
        userwants = True #does user want to proceed?
        if a == "cancel":
            userwants = False
        if userwants:
            a.display()
    #-----------MAP-----------#
    elif comm.upper() == "MAP":
        #print map
        showMap(reg_map)
        print("====LEGEND====")
        for u in allies+enemies+all_terr:
            print(u.sym,"=",u.name,end=" | ")
        print("\n")
    #-----------CALCULATE-------------#
    elif comm.upper() in ["CALC","CALCULATE"]:
        #calculates damage between 2 units (ally and enemy)
        a = askUser("Select ally to calculate with: ",allies,player,"allies")
        userwants = True
        if a == "cancel":
            userwants = False
        if userwants:
            e = askUser("Select enemy to calculate with: ",enemies,player,"enemies",True)
        if e == "cancel":
            userwants = False
        if userwants:
            eter_avo = 0 #enemy terrain avoid and defense
            eter_def = 0
            ater_avo = 0 #ally terrain avoid and defense
            ater_def = 0
            #determining which terrain unit is standing on
            for t in all_terr:
                if stat_map[len(stat_map)-1-e.y][e.x] == t.sym:
                    eter_avo = t.avo
                    eter_def = t.defen
                if stat_map[len(stat_map)-1-a.y][a.x] == t.sym:
                    ater_avo = t.avo
                    ater_def = t.defen
            a.calculate(e,eter_avo,eter_def)
            print("--------------------------------")
            e.calculate(a,ater_avo,ater_def)
    #----------------MOVE--------------#
    elif comm.upper() == "MOVE":
        a = askUser("Select ally to move: ",movers,player,"moveable allies")
        userwants = True #does user want to proceed?
        if a == "cancel":
            userwants = False
        if userwants:
            e_sym = [en.sym for en in enemies]
            move_map = moveDisp(a.x,a.y,a.MOVE+1,a.MOVE+1,copy.deepcopy(reg_map),e_sym,a,all_terr)
            showMap(move_map)
            #printing legend
            print("=========LEGEND=========")
            for u in allies+enemies+all_terr:
                print(u.sym,"=",u.name,end=" | ")
            print("\n")
            while True:
                xmove = input("What's the X co-ord of where you move?\n") #where user wants to move unit
                ymove = input("What's the Y co-ord of where you move?\n")
                if xmove.lower() == "cancel" or ymove.lower() == "cancel":
                    print("Cancelled")
                    break
                try:
                    xmove = int(xmove)
                    ymove = int(ymove)
                except Exception:
                    print("You must enter an integer!")
                    continue
                if xmove >= len(reg_map[0]):
                    print("X value too large!")
                elif xmove < 0:
                    print("X value too small!")
                elif len(reg_map)-ymove-1 >= len(reg_map):
                    print("Y value too small!")
                elif len(reg_map)-ymove-1 < 0:
                    print("Y value too large!")
                elif not move_map[len(reg_map)-ymove-1][xmove] in [str(i) for i in range(1,10)]:
                    print("Not a moveable square!")
                else:
                    reg_map[len(reg_map)-a.y-1][a.x] = stat_map[len(reg_map)-a.y-1][a.x] #removes ally symbol from place moved from and reverts to normal as found on static map
                    a.move(xmove,ymove)
                    reg_map[len(reg_map)-a.y-1][a.x] = a.sym
                    movers.remove(a) #makes sure each ally can only move once
                    break
    #-------------------ITEM---------------------#
    elif comm.upper() == "ITEM":
        u = askUser("Pick unit to view items of: ",allies+enemies,player,"units")
        userwants = True #does user want to continue with action
        if u == "cancel":
            userwants = False
        if userwants:
            print(u.name+"'s items")
            u.show_items()
    #-------------------EQUIP--------------------#
    elif comm.upper() == "EQUIP":
        a = askUser("Pick ally to equip a weapon to: ",allies,player,"allies")
        userwants = True
        if a == "cancel":
            userwants = False
        if userwants:
            print(a.name+"'s items")
            eq = askUser("Pick weapon to equip to: ",a.items,player,"items",True)
            if not eq == "cancel":
                a.equip_w(eq)
    #------------------HELP------------------#
    elif comm.upper() == "HELP":
        print("""QUIT - leave the game (why would u do that?)
DISPLAY - display an units name
CALCULATE - calculate an ally against an enemy
MAP - Display map
MOVE (INC) - Move an ally
ATTACK (Movement data INC) - What do you think it does? Heal?
ITEM - Views items
EQUIP - Selects weapon to equip
USE - Selects item to use
END - Ends your turn, and then enemies can attack you. Be careful when you do this man.""")
    #------------------END----------------#
    elif comm.upper() == "END":
        for a in allies:
            if a.canAttack and not a in attackers:
                attackers.append(a)
                #difference between attackers list and attribute
                #can attack is can attack is when unit
                #cannot attack due to a condition and attackers
                #is when unit used attack for this turn
            if a.canMove and not a in movers:
                movers.append(a)
        turn += 1 #add enemy's turn here
        #incomplete
    #----------------USE------------------#
    elif comm.upper() == "USE":
        a = askUser("Pick ally to use item of: ",allies,player,"allies")
        userwants = True
        if a == "cancel":
            userwants = False
        if userwants:
            i = askUser("Pick item: ",a.items,player,"items",True)
            if i == "cancel":
                userwants = False
        if userwants:
            use(i,a)
    #----------------INVALIDE-------------#
    else:
        print("Invalid command. Type HELP for help.")
