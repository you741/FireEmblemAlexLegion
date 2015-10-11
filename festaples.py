#festaples.py
#includes all fire emblem stable functions and variables. Includes movement func
from feclasses import *
from feweapons import *
from random import randint
from pprint import pprint
#===============================================================#
#map legend:                                                    #
# + = attackable/healable square with current weapon/staff      #
# 1-9 and # = Moveable square                                         #
# . = field | = forest                                          #
# e = Enemy E = enemy you can attack                            #
# b = Boss B = boss you can attack                              #
# = = wall - = water * = fog                                    #
# Any other character is a playable unit                        #
#===============================================================#

def moveDisp(x,y,move,maxmove,grid,flying=False,waterproof=False):
    #displays movement for specific units
    ym = len(grid) - 1 - y #y position on map
    curr_spot = grid[ym][x] #current spot on map
    if move <= 0:
        return grid
    elif curr_spot.upper() in ["B","E"]:
        #checks if space modified is occupied or insurpassable
        return grid
    elif curr_spot == "." or (flying and curr_spot in ["=","-"]) or (waterproof and curr_spot == "-"):
        #recursive function - passable and standable
        grid[ym][x] = str(maxmove-move+1)
        if not ym-1 < 0:
            grid = moveDisp(x,y+1,move-1,maxmove,grid,flying,waterproof)
        if not ym+1 >= len(grid):
            grid = moveDisp(x,y-1,move-1,maxmove,grid,flying,waterproof)
        if not x-1 < 0:
            grid = moveDisp(x-1,y,move-1,maxmove,grid,flying,waterproof)
        if not x+1 >= len(grid[0]):
            grid = moveDisp(x+1,y,move-1,maxmove,grid,flying,waterproof)
        return grid
    elif curr_spot in [str(i) for i in range(1,10)]:
        #marked square, will replace if smaller
        if int(curr_spot) > maxmove-move+1:
            grid[ym][x] = str(maxmove-move+1)
        if not ym-1 < 0:
            grid = moveDisp(x,y+1,move-1,maxmove,grid,flying,waterproof)
        if not ym+1 >= len(grid):
            grid = moveDisp(x,y-1,move-1,maxmove,grid,flying,waterproof)
        if not x-1 < 0:
            grid = moveDisp(x-1,y,move-1,maxmove,grid,flying,waterproof)
        if not x+1 >= len(grid[0]):
            grid = moveDisp(x+1,y,move-1,maxmove,grid,flying,waterproof)
        return grid
    elif not move == 1:
        #recursive function - passable but not standable
        if not ym-1 < 0:
            grid = moveDisp(x,y+1,move-1,maxmove,grid,flying,waterproof)
        if not ym+1 >= len(grid):
            grid = moveDisp(x,y-1,move-1,maxmove,grid,flying,waterproof)
        if not x-1 < 0:
            grid = moveDisp(x-1,y,move-1,maxmove,grid,flying,waterproof)
        if not x+1 >= len(grid[0]):
            grid = moveDisp(x+1,y,move-1,maxmove,grid,flying,waterproof)
        return grid
    else:
        return grid
def showMap(grid):
    print("  "+" ".join([str(i) for i in range(len(grid[0]))]))
    for y in range(len(grid)):
        horbar = "" #horizontal bar
        for x in grid[y]:
            x_fin = x if not x in [str(i) for i in range(1,10)] else "#"
            horbar += " "+x_fin
        ydisp = len(grid) - y - 1 #y as displayed on grid
        print(ydisp,horbar,sep="")
    return True
    

