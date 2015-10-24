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
name = input("Enter your name:\n")
name = name.upper()
askingclass = True
askmsg = "Enter your class (mage,knight,myrmidon) or info for more info:\n"
#^msg asked to user in askingclass loop

#----common weapons and items----#
iron_lance = Weapon("Iron Lance",7,8,45,80,"Lance",100)
silver_lance = Weapon("Silver Lance",13,10,20,75,"Lance",100)
fire = Weapon("Fire",5,4,40,95,"Anima",100,0,1,True,"",2)
slim_sword = Weapon("Slim Sword",3,2,35,100,"Sword",200,5)
steel_sword = Weapon("Steel Sword",8,10,30,80,"Sword",200)
iron_sword = Weapon("Iron Sword",5,5,47,90,"Sword",100)
iron_axe = Weapon("Iron Axe",8,10,45,75,"Axe",100)
rapier = Weapon("Rapier",7,5,40,90,"Sword",700,10,1,False,["Cavalier","Paladin","Knight","General"],1,5,"Effective against knights, cavalry","Yoyo")
vulnerary = Item("Vulnerary",3,"Heals for 10 HP")

#--------Common terrain----------#
plain = Terrain("Plain",".")
forest = Terrain("Forest","|",20,1,1)
mountain = Terrain("Mountain","&",40,2,4)
hill = Terrain("Hill","^",30,2,4)
water = Terrain("Water","-",10,0,4)
wall = Terrain("Wall","=",0,0,0)
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
        player = Myrmidon(name,20,5,7,7,4,3,2,5,[copy.deepcopy(slim_sword)],[70,40,60,60,45,20,20])
        askingclass = False
    if playerclass.lower() == "info":
        print("""Mage - A speedy and accurate user of anima magic. Can't really take physical hits, although magical defense is high. Melts enemies with low resistance.

Knight - A tanky but slow lance-wielder. Strong but inaccurate. Low resistance.

Myrmidon - A speedy sword user. Very skillfull with the sword art, but dies easily.""")
        askmsg = "Enter your class (mage,knight,myrmidon) or info for more info:\n"      
    else:
        askmsg = "Your entry is invalid. Please enter mage, knight, myrmidon or info:\n"

chapter = 0
turn = 1
start = True
running = True
allies = [] #allies in current chapter
attackers = [] #allies that can attack
movers = [] #allies that can move
enemies = [] #enemies
all_allies = []#all allies
all_terr = [] #all terrain
reg_map = [] #regular map
stat_map = [] #static terrain map
#main game loop
while running:
    #---------Prologue initialization-------#
    if chapter == 0 and start:
        #chapter 0 initialization
        player.sym = "P"
        player.x = 3
        player.y = 2
        player.deathQuote = "I was forced into this world... yet I feel as if I could've avoided this..."
        allies.append(player)
        lvl1map = [["." for i in range(15)]for i in range(12)] #chapter 1 map
        lvl1map[5][5],lvl1map[5][6],lvl1map[4][6] = "|","|","|"
        lvl1_elem = [copy.deepcopy(plain),copy.deepcopy(forest)] #all types of terrain in chapter 1
        chapter = 0 #chapter we're on
        turn = 1
        #creating You Zhou
        yoyo = Lord("Yoyo",18,5,7,5,7,4,4,5,[copy.deepcopy(rapier),copy.deepcopy(fire),copy.deepcopy(vulnerary)],[60,40,65,40,70,20,45])
        yoyo.sym = "Y"
        yoyo.x = 3
        yoyo.y = 3
        yoyo.deathQuote = "I'm sorry... Every...one... I'm so useless..."
        allies.append(yoyo)
        attackers.append(player)
        attackers.append(yoyo)
        movers.append(player)
        movers.append(yoyo)
        prologueStory(player.name) #story for prologue
        #all terrain list
        all_terr = copy.deepcopy(lvl1_elem)
        #creating enemy1
        enemy1 = Brigand("Bandit 1",20,5,2,2,0,3,0,8,[copy.deepcopy(iron_axe)])
        enemy1.canLevel = False
        enemy1.gift = 50
        enemy1.sym = "E"
        enemy1.x = 2
        enemy1.y = 2
        enemies.append(enemy1)
        #creating enemies 2 and 3
        enemy2 = copy.deepcopy(enemy1)
        enemy2.name = "Bandit 2"
        enemy2.x = 12
        enemy2.y = 1
        enemy2.sym = "€"
        enemy3 = copy.deepcopy(enemy1)
        enemy3.name = "Bandit 3"
        enemy3.x,enemy3.y,enemy3.sym = 11,7,"ε"
        enemies.append(enemy2)
        enemies.append(enemy3)
        #creates boss
        boss = Brigand("Bandit 1",28,8,4,4,0,5,1,8,[copy.deepcopy(iron_axe)])
        boss.fightQuote = "I serve the mighty Alex Legion! You won't stop me!\nYoyo: You will pay for your iniquities!"
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
        all_allies = [u for u in allies] #sets all allies that should be here this chapter
    #----------------CHAPTER 1 INITIALIZATION----------------#
    if chapter == 1 and start:
        allies = [u for u in all_allies] #all allies take part in this chapter
        for a in allies:
            a.hp = a.maxhp
            a.alive = True
        lvl2map =[
         "&&&&...||...---..|||",#14
         "&&&....|||....-...||",#13
         "&&.......|..........",#12
         "&........^^^........",#11
         ".........^&^........",#10
         ".........&&&........",#9
         ".........&&&&.......",#8
         "........&&&&&.......",#7
         "........&&&&&.......",#6
         ".......&&&&&&.....||",#5
         ".........&&&&.......",#4
         ".......^^&&^......--",#3
         "......^^^^^......---",#2
         "........||......----",#1
         "..............------"]#0
         #0123456789ABCDEFGHIJ
        lvl2map = [list(l) for l in lvl2map]
        lvl2_elem = [copy.deepcopy(plain),copy.deepcopy(forest),copy.deepcopy(mountain),copy.deepcopy(water),copy.deepcopy(hill)] #all types of terrain in chapter 1
        all_terr = copy.deepcopy(lvl2_elem)
        chapter = 1 #chapter we're on
        turn = 1
        #creating franny
        franny = Cavalier("Franny",22,6,8,8,5,5,3,8,[copy.deepcopy(iron_lance),copy.deepcopy(iron_sword),copy.deepcopy(vulnerary)],[85,35,55,55,40,35,25])
        franny.level = 3
        franny.sym = "F"
        franny.x = 3
        franny.y = 7
        allies.append(franny)
        #creating albert
        albert = Paladin("Albert",32,12,15,13,6,12,10,10,[copy.deepcopy(steel_sword),copy.deepcopy(silver_lance),copy.deepcopy(vulnerary)],[45,30,35,35,20,25,15])
        albert.sym = "A"
        albert.x = 4
        albert.y = 7
        allies.append(albert)
        #creating gary
        gary = Fighter("Gary",28,8,6,5,3,5,0,13,[copy.deepcopy(iron_axe),copy.deepcopy(vulnerary)],[90,60,45,35,30,45,10])
        gary.level = 3
        gary.sym = "G"
        gary.x = 3
        gary.y = 6
        allies.append(gary)
        #creating henning
        henning = Transporter("Henning",25,1,13,13,10,8,8,25,[],[100,100,100,100,0,100,90])
        henning.sym = "H"
        henning.x = 3
        henning.y = 5
        allies.append(henning)
        player.x = 4
        player.y = 5
        yoyo.x = 4
        yoyo.y = 6
        chapter1Story(player.name)
        #creating enemy1
        enemy1 = Brigand("Bandit 1",24,6,3,2,0,4,0,10,[copy.deepcopy(iron_axe)])
        enemy1.sym = "E"
        enemy1.x = 10
        enemy1.y = 5
        enemies.append(enemy1)
        reg_map = copy.deepcopy(lvl2map)
        stat_map = copy.deepcopy(lvl2map)
        movers = [u for u in allies]
        attackers = [u for u in allies]
        all_allies = [u for u in allies] #all allies that should be alive
        #incomplete
    for a in allies:
        reg_map[len(reg_map)-1-a.y][a.x] = a.sym
    for e in enemies:
        reg_map[len(reg_map)-1-e.y][e.x] = e.sym
    if start:
        showMap(reg_map)
        print("==================LEGEND==================")
        line = 0
        for u in allies+enemies+all_terr:
            line += 1
            print(u.sym,"=",u.name,end=" | ")
            if line % 5 == 0:
                print("\n")#creates new line whenever 5 is reached in a line
        print("\n")
        start = False        
    comm = input("Enter a command:\n")
    #-----------CHEAT FOR PASSING LEVELS---------#
    if comm.upper() == "GOUP":
        chapter += 1
        start = True
        enemies = []
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
            if a.attackspeed >= e.attackspeed + 4 and e.alive:
                a.attack(e)
            elif a.attackspeed <= e.attackspeed - 4 and a.alive:
                e.attack(a)
                asking = False
            if not a.alive:
                allies.remove(a)
                reg_map[len(reg_map)-1-a.y][a.x] = stat_map[len(stat_map)-1-a.y][a.x]
            if not e.alive:
                enemies.remove(e)
                reg_map[len(reg_map)-1-e.y][e.x] = stat_map[len(stat_map)-1-e.y][e.x]
            attackers.remove(a) #makes sure each unit can only attack once per turn
            print(a.name,"can no longer make an action until you end the turn")
            if a in movers:
                movers.remove(a)
    #------------------DISPLAY---------------------#
    elif comm.upper() == "DISPLAY":
        #print enemy or ally info
        a = askUser("Select unit to display info: ",allies+enemies,player)
        userwants = True #does user want to proceed?
        if a == "cancel":
            userwants = False
        if not a:
            print("No units")
            userwants = False
        if userwants:
            a.display()
    #---------------------MAP----------------------#
    elif comm.upper() == "MAP":
        #print map
        showMap(reg_map)
        print("==================LEGEND==================")
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
        if not a:
            print("No allies")
            userwants = False
        if userwants:
            e = askUser("Select enemy to calculate with: ",enemies,player,"enemies",True)
        if e == "cancel":
            userwants = False
        if not e:
            print("No enemies")
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
            print("No allies that can move! End your turn if you want them to!")
        if userwants:
            e_sym = [en.sym for en in enemies]
            movement = a.MOVE
            if a.mounted:
                movement = a.movesLeft
            move_map = moveDisp(a.x,a.y,movement,movement,copy.deepcopy(reg_map),e_sym,a,all_terr)
            print("==================LEGEND==================")
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
                if xmove.lower() == "cancel":
                    print("Cancelled")
                    break
                ymove = input("What's the Y co-ord of where you move?\n")
                if ymove.lower() == "cancel":
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
                    #HANDLE MOUNTED UNITS
                    if not a.mounted:
                        movers.remove(a) #makes sure each ally can only move once
                    else:
                        a.movesLeft -= int(move_map[len(move_map)-ymove-1][xmove])
                        if a.movesLeft < 0:
                            a.movesLeft = 0
                        if a.movesLeft == 0:
                            movers.remove(a)
                    break
    #-------------------ITEM---------------------#
    elif comm.upper() == "ITEM":
        u = askUser("Pick unit to view items of: ",allies+enemies,player,"units")
        userwants = True #does user want to continue with action
        if u == "cancel":
            userwants = False
        if not u:
            print("No units")
            userwants = False
        if userwants:
            print(u.name+"'s items")
            u.show_items()
    #-------------------EQUIP--------------------#
    elif comm.upper() == "EQUIP":
        a = askUser("Pick ally to equip a weapon to: ",attackers,player,"allies")
        userwants = True
        if a == "cancel":
            userwants = False
        if not a:
            print("No allies that can equip! End your turn!")
            userwants = False
        if userwants:
            print(a.name+"'s items")
            eq = askUser("Pick weapon to equip to: ",a.weapons,player,"items",True)
            if not eq:
                print("No weapons to equip!")
            if not eq == "cancel" and not (not eq):
                a.equip_w(eq)
    #------------------TRADE---------------------#
    elif comm.upper() == "TRADE":
        a = askUser("Pick first ally to trade with: ",attackers,player,"allies")
        userwants = True
        if a == "cancel":
            userwants = False
        if not a:
            userwants = False
            print("No allies that can trade! End your turn!")
        if userwants:
            tradable_allies = [al for al in allies if al != a and (abs(a.x - al.x) + abs(a.y - al.y)) <= 1 and al.CLASS != "Transporter"]
            a2 = askUser("Pick 2nd ally to trade with: ",tradable_allies,player,"allies")
        if not a2:
            print("No allies to trade with",a.name,"!")
            userwants = False
        if a2 == "cancel":
            userwants = False
        if userwants:
            #fdispitem refers to the full display of an item
            #trading loop
            while True:
                fdispitem_a = []
                fdispitem_a2 = []
                for i in range(a.maxspace):
                    if len(a.items) > i:
                        fdispitem_a.append(a.items[i])
                    else:
                        fdispitem_a.append(Item("No item",0))
                for i in range(a.maxspace):
                    if len(a2.items) > i:
                        fdispitem_a2.append(a2.items[i])
                    else:
                        fdispitem_a2.append(Item("No item",0))
                print("Will now enable item trading, type 'cancel' to exit anytime")
                i1 = askUser("Select item from "+a.name+" (select 'no item' to take): ",fdispitem_a,player,"items",True)
                if i1 == "cancel":
                    break
                if not i1:
                    print("No items to trade!")
                    break
                i2 = askUser("Select item from "+a2.name+" (select 'no item' to give): ",fdispitem_a2,player,"items",True)
                if i2 == "cancel":
                    break
                if not i1:
                    print("No items to trade!")
                    break
                #trading items
                if i1.name == "No item" and i2.name == "No item":
                    print("Um you can't trade no item with another guys no item.")
                    continue
                if not i1.name == "No item" and not i2.name == "No item":
                    a.items[a.items.index(i1)],a2.items[a2.items.index(i2)] = a2.items[a2.items.index(i2)],a.items[a.items.index(i1)]
                elif i1.name == "No item":
                    a2.remove_item(i2,False)
                    a.add_item(i2,False)
                elif i2.name == "No item":
                    a2.add_item(i1,False)
                    a.remove_item(i1,False)
                print("Traded",a.name,"'s",i1.name,"with",a2.name,"'s",i2.name)
                if i1 == a.equip:
                    a.equip = Weapon("No weapon",0,0,0,0,"",0)
                    #If item selected is equipped item
                    if type(i2) == Weapon:
                        #if 2nd item selected is a weapon
                        if a.wskl[i2.typ] >= i2.mast or a.name == i2.prf:
                            #if user can use given weapon
                            a.equip_w(i2,False)
                if a.equip.name == "No weapon":
                    #equips closest weapon or none at all if none
                    for i in range(len(a.weapons)):
                        if type(a.weapons[i]) == Weapon:
                            if a.equip_w(a.weapons[i],False):
                                #tries to equip every item in list.
                                #won't print error
                                break
                if i2 == a2.equip:
                    a2.equip = Weapon("No weapon",0,0,0,0,"",0)
                    #If 2nd item selected is equipped item
                    if type(i1) == Weapon:
                        #if 1st item selected is a weapon
                        if a2.wskl[i1.typ] >= i1.mast or a2.name == i1.prf:
                            #if user can use given weapon
                            a2.equip_w(i1,False)
                if a2.equip.name == "No weapon":
                    #equips closest weapon or none at all if none
                    for i in range(len(a2.weapons)):
                        if type(a2.weapons[i]) == Weapon:
                            if a2.equip_w(a2.weapons[i],False):
                                #tries to equip every item in list.
                                #won't print error
                                break
                cont = input("Do another trade amongst these two? [Y to confirm, any other key to reject]\n")
                if cont.lower() in ["yes","y","ok","sure","affirmative"]:
                    pass
                else:
                    print("Ended trading")
                    break
    #----------------USE------------------#
    elif comm.upper() == "USE":
        a = askUser("Pick ally to use item of: ",attackers,player,"allies")
        userwants = True
        if a == "cancel":
            userwants = False
        if not a:
            print("No allies that can use an item! End your turn!")
            userwants = False
        if userwants:
            i = askUser("Pick item: ",a.items,player,"items",True)
            if not i:
                print("No items!")
                userwants = False
            if i == "cancel":
                userwants = False
        if userwants:
            if use(i,a) == -1:
                a.remove_item(i,False) #removes users item
            attackers.remove(a)
            print(a.name,"cannot perform an action until you end your turn!")
    #----------------TERRAIN-----------------#
    elif comm.upper() == "TERRAIN":
        u = askUser("Pick unit to view terrain of: ",allies+enemies,player,"units")
        userwants = True #does user want to continue with action
        if u == "cancel":
            userwants = False
        if not u:
            print("No units")
            userwants = False
        if userwants:
            for t in all_terr:
                if t.sym == stat_map[len(stat_map) - 1 - u.y][u.x]:
                    print(u.name,"is standing on a",t.name,"terrain")
                    break
    #------------------HELP------------------#
    elif comm.upper() == "HELP":
        print("""QUIT - leave the game (why would u do that?)
DISPLAY - display an units name
CALCULATE - calculate an ally against an enemy
MAP - Display map
MOVE - Move an ally
ATTACK - What do you think it does? Heal?
ITEM - Views items
EQUIP - Selects weapon to equip
USE - Selects item to use
TRADE - Trades items amongst allies
TERRAIN - Display terrain unit is on
END - Ends your turn, and then enemies can attack you. Be careful when you do this man.""")
    #------------------END----------------#
    elif comm.upper() == "END":
        print("You have ended your turn!")
        turn += 1
        #enemy's AI
        print("===============ENEMY PHASE================")
        for e in enemies:
            print(e.name,"has started")
            canEnAttack = False #can enemy attack?
            allies_sym = [a.sym for a in allies]
            e_movemap = moveDisp(e.x,e.y,e.MOVE,e.MOVE,copy.deepcopy(reg_map),allies_sym,e,all_terr)
            moveable = [] #enemies movable squares
            attackableAllies = [] #attackable Allies
            for y in range(len(e_movemap)):
                for x in range(len(e_movemap[0])):
                    if e_movemap[len(e_movemap) - 1 - y][x] in [str(i) for i in range(0,12)]:
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
                        miniXs.append(x)
                        miniYs.append(y)
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
            if canEnAttack:
                ally_data = enemyAI(e,attackableAllies,moveable,stat_map)
                a = ally_data[4]
                if a == 0:
                    print(e.name,"has finished turn")
                    time.sleep(1)
                    continue
                reg_map[len(reg_map)-e.y-1][e.x] = stat_map[len(reg_map)-e.y-1][e.x] #removes enemy symbol from place moved from and reverts to normal as found on static map
                e.move(ally_data[5],ally_data[6])
                reg_map[len(reg_map)-e.y-1][e.x] = e.sym
                e.equip_w(ally_data[6],False)
                e.attack(a)
                a.attack(e)
                if a.attackspeed - 4 >= e.attackspeed:
                    a.attack(e)
                elif e.attackspeed -4 >= a.attackspeed:
                    e.attack(a)
                if not e.alive:
                    reg_map[len(reg_map) - e.y - 1][e.x] = stat_map[len(stat_map) - 1 - e.y][e.x]
                if not a.alive:
                    allies.remove(a)
                    reg_map[len(reg_map) - a.y - 1][a.x] = stat_map[len(stat_map) - 1 - a.y][a.x]
            if e.alive:
                print(e.name,"has finished turn")
            time.sleep(1)
        enemies = [e for e in enemies if e.alive] #removes all enemies that are dead
        for a in allies:
            if a.alive:
                if a.canAttack and not a in attackers:
                    attackers.append(a)
                    #difference between attackers list and attribute
                    #can attack is can attack is when unit
                    #cannot attack due to a condition and attackers
                    #is when unit used attack for this turn
                if a.canMove and not a in movers:
                    movers.append(a)
                if a.mounted:
                    a.movesLeft = a.MOVE
        print("==============PLAYER PHASE================")
    #----------------INVALIDE-------------#
    else:
        print("Invalid command. Type HELP for help.")
    #---------Whether user beats chapter or not--------#
    if chapter == 0 and len(enemies) == 0:
        print("You beat the Prologue!")
        print("CHAPTER COMPLETE!")
        enemies = [] #gets rid of enemies
        all_allies = [u for u in allies] #seeds out dead allies
        start = True
        chapter += 1
    #---------IF player or Yoyo dies you lose---------#
    if not player.alive or not yoyo.alive:
        print("GAME OVER")
        player.alive = True
        yoyo.alive = True
        enemies = []
        allies = []
        attackers = []
        movers = []
        print("Restarting chapter...")
        time.sleep(1)
        print(".....................")
        time.sleep(1)
        print(".....................")
        chapter = 0
        start = True
        turn = 1
