#festaples.py
#includes all fire emblem stable functions and variables. Includes movement func
from feclasses import *
from feweapons import *
from random import randint
from pprint import pprint
#===============================================================#
#map legend:                                                    #
# + = attackable/healable square with current weapon/staff      #
# 1-9 and # = Moveable square                                   #
# . = field | = forest ^ = hill 山 = mountain                   #
# e = Enemy E = enemy you can attack                            #
# b = Boss B = boss you can attack                              #
# = = wall - = water * = fog                                    #
# Any other character is a playable unit                        #
#===============================================================#

def moveDisp(x,y,move,maxmove,grid,enemies,ally,all_terr):
    #displays movement for specific units
    ym = len(grid) - 1 - y #y position on map
    curr_spot = grid[ym][x] #current spot on map
    if move <= 0:
        return grid                #special terrain handling
    elif curr_spot in enemies or (ally.mounted and curr_spot == "^") or (not ally.flying and curr_spot in ["^","-","=","山"]) or (not ally.waterproof and curr_spot == "-") or (not ally.mountainous and curr_spot == "山"):
        #checks if space modified is occupied or insurpassable
        return grid                 
    elif curr_spot in [".","|","^","-","山"]:
    #recursive function - passable and standable
        grid[ym][x] = str(maxmove-move)
    elif curr_spot in [str(i) for i in range(1,10)]:
        #marked square, will replace if smaller
        if int(curr_spot) > maxmove-move+1:
            grid[ym][x] = str(maxmove-move)
    elif not move == 1:
        pass
    else:
        return grid
    for t in all_terr:
        if curr_spot == t.sym:
            if move-t.hind > 0 and not ally.flying:
                move -= t.hind
                break#reduces movement by hindrance
    if not ym-1 < 0:
            grid = moveDisp(x,y+1,move-1,maxmove,grid,enemies,ally,all_terr)
    if not ym+1 >= len(grid):
        grid = moveDisp(x,y-1,move-1,maxmove,grid,enemies,ally,all_terr)
    if not x-1 < 0:
        grid = moveDisp(x-1,y,move-1,maxmove,grid,enemies,ally,all_terr)
    if not x+1 >= len(grid[0]):
        grid = moveDisp(x+1,y,move-1,maxmove,grid,enemies,ally,all_terr)
    return grid

def showMap(grid):
    for y in range(len(grid)):
        horbar = "" #horizontal bar
        ydisp = len(grid) - y - 1 #y as displayed on grid
        for x in grid[y]:
            x_fin = x if not x in [str(i) for i in range(1,10)] else "#"
            horbar += "  "+x_fin
        spc = "" if ydisp//10 > 0 else " "
        print(ydisp,spc,horbar,sep="")
    up_bar = "  " #x-axis
    for i in range(len(grid[0])):
        spc = " " if i//10 > 0 else "  "
        up_bar += spc + str(i)
    print(up_bar)
    return True
#loop to ask user things
def askUser(ques,li,player,obj="units",nodisplayer=False,attr=""):
    print("==========",obj.upper(),"==========",sep="=")
    if len(li) < 1:
        #empty list
        return False
    for u in li:
        isplayer = "(enter 'me', not this name)" if u == player else ""
        if attr == "display":
            print(u.display(),isplayer)
            print("----------------------")
        else:
            print(u.name,isplayer)
    print("==========","="*len(obj),"==========",sep="=")
    asking = True
    while asking:
        unit = input(ques)
        if unit.lower() == "cancel":
            print("Cancelled")
            return "cancel"
            asking = False
            break
        if unit.lower() == "me" and not nodisplayer:
            return player
            asking = False
            break
        for u in li:
            if unit.lower() == u.name.lower() and not u == player:
                return u
                asking = False
                break
        if unit.lower() == "info":
            attr = "display" #displays more info upon user entering info
        else:
            print("Invalid",obj)
    
#uses an item
def use(item,unit):
    if item.name == "Vulnerary":
        unit.gainhp(10)
        item.use()
        print(unit.name,"healed to",unit.hp,"with Vulnerary")
        return True
    elif item.name == "Elixir":
        unit.hp = unit.maxhp
        item.use()
        print(unit.name,"healed to",unit.hp,"with Elixir")
        return True
    else:
        #invalid item for usage
        print("Can't use item!")
        return False
#enemy's AI
def enemyAI(enemy,allies,movable,c=0,cna=True):
    weaponTriangle = {"Sword":"Axe",
                          "Axe":"Lance",
                          "Lance":"Sword",
                          "Anima":"Light",
                          "Light":"Dark",
                          "Dark":"Anima"}
    canAllAtk = cna #can all allies attack the enemy?
    best = [] #best allies to attack - try to reduce to one    
    for a in allies:
        #----------Start of enemy's weapon selection---------#
        #enemy try to attack with a weapon that has the mos disadvantage
        disadv = True
        adv = False
        ideal_weap = [(-1,-1,999999,999999,0,0,0,0)] #ideal weapons to use against target
                    #(enemy damage, enemy hit %, ally damage, ally hit %, ally, enemy.x, enemy.y, enemy.weapon)
        for w in enemy.weapons:
            if adv and weaponTriangle(w.typ) != a.equip.typ:
                continue #will not make ideal weapon if not at advantage when another weapon is
            elif weaponTriangle(w.typ) == a.equip.typ and not adv:
                #if enemy has the advantage
                disadv = False
                adv = True
                ideal_weap = [w]
            elif weaponTriangle(a.equip.typ) != w.typ and disadv:
                #if enemy has a weapon that isn't at a disadvantage
                disadv = False
                ideal_weap = [w]
            elif weaponTriangle(a.equip.typ) == w.typ and not disadv:
                continue #if enemy has weapon that is at a disadvantage when enemy has one that isn't
            else:
                ideal_weap.append(w)
        if len(ideal_weap) == 0:
            print("YOU ZHOU SOMETHING IS WRONG!!!!!") #lol error message
        #-----------End of enemy's weapon selection-----------#
        for w in ideal_weap:
            for x,y in movable:
                en = copy.deepcopy(enemy)
                en.x = x
                en.y = y
                en_a = en.calculate(a,0,0,False,True)
                if not en_a:
                    continue
                a_en = a.calculate(en,0,0,False,True)
                if a_en != False and not canAllAtk:
                    continue #will not attack ally if another ally can't fight back
                comparer = (en_a[0],en_a[1],a_en[0],a_en[1],a,x,y,enemy.weapons.index(w)) #stats to compare
                comparison = comparer[c] > best[0][c] if c in [0,1] else comparer < best[0][c]
                if not a_en and canAllAtk:
                    #if an ally cannot attack
                    a_en = (0,0,0)
                    canAllAtk = False
                    best = [comparer]
                    continue
                if comparison:
                    #if comparison (default damage %) is greater than best percentage
                    best = [comparer]
                elif comparer[c] == best[0][c]:
                    #if comparison is equal to the best
                    #ignore this: best_allies = [b[4] for b in best]
                    best.append(comparer)
    if len(best) > 1 and 0 <= c <= 3:
        #if more than one best will run function again testing the other priorities
        best_allies = [] #best allies to attack
        for b in best:
            if not b[4] in best_allies:
                    best_allies.append(b[4]) 
        return enemyAI(enemy,best_allies,movable,c+1,canAllAtk)
    elif len(best) > 1 and c > 3:
        #if unable to reduce lower when all priorities used up, will return first value in best
        return best[0]
    elif len(best) == 0:
        print("SOMETHING'S WRONG")
    elif len(best) == 1:
        return best[0]
    
