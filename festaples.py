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
    #INC. ADD TERRAIN HANDLEMENT. NEW PARAM NEEDED (all_terr)
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
        grid[ym][x] = str(maxmove-move+1)
    elif curr_spot in [str(i) for i in range(1,10)]:
        #marked square, will replace if smaller
        if int(curr_spot) > maxmove-move+1:
            grid[ym][x] = str(maxmove-move+1)
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
