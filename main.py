#Fire Emblem Alex Legion
#Text based game based on Fire Emblem
#Programmed by You Zhou

from random import randint
from festaples import *
from feclasses import *
from feweapons import *
from festory import *
import copy
import time
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
mountain = Terrain("Mountain","山",40,2,4)
hill = Terrain("Hill","^",40,2,4)
#asking user for class
#creating player's class
while askingclass:
    playerclass = input(askmsg)
    if playerclass.lower() == "mage":
        player = Mage(name,18,5,6,6,6,2,5,4,[copy.deepcopy(fire)],[60,40,55,55,55,15,50])
        askingclass = False
    if playerclass.lower() == "knight":
        player = Knight(name,21,7,4,4,3,7,1,10,[copy.deepcopy(iron_lance)],[80,55,40,30,30,60,15])
        askingclass = False
    if playerclass.lower() == "myrmidon":
        player = Myrmidon(name,20,5,6,7,4,3,2,5,[copy.deepcopy(slim_sword)],[70,40,60,60,45,20,20])
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

lvl1map = [["." for i in range(15)]for i in range(12)] #chapter 1 map
lvl1map[5][5],lvl1map[5][6],lvl1map[4][6] = "|","|","|"
lvl1_elem = [copy.deepcopy(plain),copy.deepcopy(forest)] #all types of terrain in chapter 1
reg_map = [] #regular map
stat_map = copy.deepcopy(reg_map) #static map - never changes
chapter = 0 #chapter we're on
turn = 1
#creating franny
franny = Cavalier("Franny",22,6,9,9,5,5,3,8,[copy.deepcopy(iron_lance),copy.deepcopy(iron_sword),copy.deepcopy(vulnerary)],[85,35,55,55,40,35,25])
franny.level = 3
franny.sym = "F"
franny.x = 3
franny.y = 7
#allies.append(franny)
#creating You Zhou
yoyo = Lord("Yoyo",18,5,7,5,7,4,4,5,[copy.deepcopy(rapier),copy.deepcopy(fire),copy.deepcopy(vulnerary)],[60,40,65,40,70,20,45])
yoyo.sym = "Y"
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
        enemy1 = Brigand("Bandit 1",20,6,2,2,0,3,0,8,[copy.deepcopy(iron_axe)])
        enemy1.canLevel = False
        enemy1.gift = 50
        enemy1.sym = "E"
        enemy1.x = 2
        enemy1.y = 2
        enemies.append(enemy1)
        #creating enemies 2 and 3
        enemy2 = copy.deepcopy(enemy1)
        enemy2.name = "Bandit 2"
        enemy2.x = 1
        enemy2.y = 5
        enemy2.sym = "€"
        enemy3 = copy.deepcopy(enemy1)
        enemy3.name = "Bandit 3"
        enemy3.x = 3
        enemy3.y = 7
        enemy3.sym = "ε"
        enemies.append(enemy2)
        enemies.append(enemy3)
        #creates boss
        boss = Brigand("Bandit 1",28,8,4,4,0,5,1,8,[copy.deepcopy(iron_axe)])
        boss.name = "Alex the Bandit"
        boss.canLevel = False
        boss.canMove = False
        boss.sym = "B"
        boss.gift = 80
        boss.x = 12
        boss.y = 10
        enemies.append(boss)
        #initializing dynamic map (units) and static map (terrain)
        reg_map = copy.deepcopy(lvl1map)
        stat_map = copy.deepcopy(lvl1map)
    for a in allies:
        reg_map[len(reg_map)-1-a.y][a.x] = a.sym
    for e in enemies:
        reg_map[len(reg_map)-1-e.y][e.x] = e.sym
    if start:
        showMap(reg_map)
        print("======LEGEND======")
        line = 0
        for u in allies+enemies+all_terr:
            line += 1
            print(u.sym,"=",u.name,end=" | ")
            if line % 5 == 0:
                print("\n")#creates new line whenever 5 is reached in a line
        print("\n")
        start = False        
    comm = input("Enter a command:\n")
    #----------------------QUIT-----------------------#
    if comm.upper() == "QUIT":
        running = False
        print("You have quit and lost all progress")
    #---------------------ATTACK----------------------#
    elif comm.upper() == "ATTACK":
        #attack function
        a = askUser("Select ally to attack with: ",attackers,player,"allies that can attack")
        userwants = True #does user want to proceed?
        if a == "cancel":
            userwants = False
        if not a:
            print("No allies that can attack!")
            userwants = False
        if userwants:
            weapons = [w for w in a.items if type(w) == Weapon] #creates weapons, let's user equip
            weapon = askUser("Select weapon to attack with: ",weapons,player,"weapons",True)
            if weapon == "cancel":
                userwants = False
            if not weapon:
                print("This unit has no weapon!")
                userwants = False
        if userwants:
            a.equip_w(weapon)
            attackable = [] #attackable enemies
            for en in enemies:
                if a.canAtk(en): #if ally can attack enemy appends enemy to list
                    attackable.append(en)
            e = askUser("Select enemy to attack: ",attackable,player,"attackable enemies",True)
            if e == "cancel":
                userwants = False
            if not e:
                userwants = False
                print("No enemies in range of this unit's weapon! Move closer!")
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
            if not player.alive or not yoyo.alive:
                print("GAME OVER")
                running = False #gonna change this to level restart, for now it kills the program
            attackers.remove(a) #makes sure each unit can only attack once per turn
            if a in movers:
                movers.remove(a)
    #------------------DISPLAY---------------------#
    elif comm.upper() == "DISPLAY":
        #print enemy or ally info
        a = askUser("Select unit to display info: ",allies+enemies,player)
        userwants = True #does user want to proceed?
        if a == "cancel":
            userwants = False
        if userwants:
            a.display()
    #---------------------MAP----------------------#
    elif comm.upper() == "MAP":
        #print map
        showMap(reg_map)
        print("======LEGEND======")
        line = 0
        for u in allies+enemies+all_terr:
            line += 1
            print(u.sym,"=",u.name,end=" | ")
            if line % 5 == 0:
                print("\n")#creates new line whenever 5 is reached in a line
        print("\n")
    #-----------------CALCULATE---------------------#
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
    #----------------MOVE------------------#
    elif comm.upper() == "MOVE":
        a = askUser("Select ally to move: ",movers,player,"moveable allies")
        userwants = True #does user want to proceed?
        if a == "cancel":
            userwants = False
        if not a:
            userwants = False
            print("No allies that can move!")
        if userwants:
            e_sym = [en.sym for en in enemies]
            move_map = moveDisp(a.x,a.y,a.MOVE+1,a.MOVE+1,copy.deepcopy(reg_map),e_sym,a,all_terr)
            print("======LEGEND======")
            showMap(move_map)
            line = 0
            for u in allies+enemies+all_terr:
                line += 1
                print(u.sym,"=",u.name,end=" | ")
                if line % 5 == 0:
                    print("\n")#creates new line whenever 5 is reached in a line
            print("# = movable square")
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
            weapons = [w for w in a.items if type(w) == Weapon]
            eq = askUser("Pick weapon to equip to: ",weapons,player,"items",True)
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
        turn += 1
        #enemy's AI
        print("==========ENEMY PHASE=============")
        for e in enemies:
            canEnAttack = False #can enemy attack?
            allies_sym = [a.sym for a in allies]
            e_movemap = moveDisp(e.x,e.y,e.MOVE+1,e.MOVE+1,copy.deepcopy(reg_map),allies_sym,e,all_terr)
            moveable = [] #enemies movable squares
            attackableAllies = [] #attackable Allies
            for y in range(len(e_movemap)):
                for x in range(len(e_movemap[0])):
                    if e_movemap[y][x] in [str(i) for i in range(0,12)]:
                        moveable.append((x,y))        
                        en = copy.deepcopy(e)
                        en.x = x
                        en.y = y
                        for a in allies:
                            if en.canAtk(a) or e.canAtk(a):
                                canEnAttack = True
                                attackableAllies.append(a)
            if not canEnAttack:
                dist = []#distances from ally
                xs = [] #x co-ords that co-respond to the distances
                ys = [] #y co-ords that co-respond to the distances
                for x,y in moveable:
                    miniDist = []
                    miniXs = []
                    miniYs = []
                    for a in allies:
                        distA = abs(x - a.x) + abs(y - a.y)
                        miniDist.append(distA)
                        miniXs.append(a.x)
                        miniYs.append(a.y)
                    dist.append(min(miniDist))
                    xs.append(miniXs[miniDist.index(min(miniDist))])
                    ys.append(miniYs[miniDist.index(min(miniDist))])
                smallDist = min(dist) #smallest distance
                movex = xs[dist.index(smallDist)]
                movey = ys[dist.index(smallDist)]
                if e.canMove:
                    reg_map[len(reg_map)-e.y-1][e.x] = stat_map[len(reg_map)-e.y-1][e.x] #removes enemy symbol from place moved from and reverts to normal as found on static map
                    e.move(movex,movey)
                    reg_map[len(reg_map)-e.y-1][e.x] = e.sym
            if not e.canMove:
                moveable = [(e.x,e.y)]
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
    #---------Whether user beats chapter or not--------#
    if chapter == 0 and len(enemies) == 0:
        print("You beat the Prologue!")
        start = True
        chapter += 1
