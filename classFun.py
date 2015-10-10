#Fire Emblem Alex Legion
#Text based game based on Fire Emblem
#Programmed by You Zhou

from random import randint
from festaples import *
from feclasses import *
from feweapons import *
#from feweapons import *
allies = []
enemies = []
name = input("Enter your name:\n")
name = name.upper()
askingclass = True
askmsg = "Enter your class (mage,knight,myrmidon) or info for more info:\n"
#^msg asked to user in askingclass loop

#----common weapons----#
iron_lance = Weapon("Iron Lance",6,8,45,80,"Lance",100)
fire = Weapon("Fire",5,4,40,95,"Anima",100,0,1,True,"",2)
slim_sword = Weapon("Slim Sword",4,2,35,100,"Sword",200,5,1)
iron_axe = Weapon("Iron Axe",8,8,45,75,"Axe",100)

#asking user for class
while askingclass:
    playerclass = input(askmsg)
    if playerclass.lower() == "mage":
        player = Mage(name,18,5,6,5,5,2,5,4,[60,40,60,55,50,20,50])
        player.equip = fire #edit later
        player.items.append(fire)
        player.wskl["Anima"] = 200
        askingclass = False
    if playerclass.lower() == "knight":
        player = Knight(name,21,6,4,4,3,6,1,10,[80,55,50,35,40,55,20])
        player.equip = iron_lance #edit later
        player.items.append(iron_lance)
        player.wskl["Lance"] = 200
        askingclass = False
    if playerclass.lower() == "myrmidon":
        player = Myrmidon(name,20,5,6,6,4,4,2,5,[70,40,60,60,45,25,30])
        player.equip = slim_sword #edit later more info below
        player.items.append(slim_sword)
        player.wskl["Sword"] = 200
        askingclass = False
    if playerclass.lower() == "info":
        print("""Mage - A speedy and accurate user of anima magic. Ignores defense and melts enemies with low resistance.
Knight - A tanky lance-wielder. Gains a bit of health whenever attacked.
Myrmidon - A speedy sword user. Has chance of getting a critical hit.""")
        askmsg = "Enter your class (mage,knight,myrmidon) or info for more info:\n"      
    else:
        askmsg = "Your entry is invalid. Please enter mage, knight, myrmidon or info:\n"
allies.append(player)
enemy1 = Murderer("Enemy 1-1",20,6,2,2,0,3,0,8)
enemy1.canLevel = False
enemy1.gift = 40
enemy1.equip = iron_axe #edit this syntax - after item add and equip functions are made
enemy1.items.append(iron_axe)
enemies.append(enemy1)
#franny = 
running = True
#main game loop
while running:
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
            for i in allies:
                print(i.name)
            print("===============================")
            ally = input()
            for a in allies:
                if ally.upper() == a.name.upper():
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
                        for e in enemies:
                            if e.name.lower() == enemy.lower():
                                #ATTACK CODE
                                a.attack(e)
                                e.attack(a)
                                if a.speed >= e.speed + 4:
                                    a.attack(e)
                                elif a.speed <= e.speed - 4:
                                    e.attack(a)
                                asking = False
                                break
                        askmsg = "Invalid enemy, input a valid enemy name: " 
                    asking = False
                    break
            else:
                askingmsg = "Not a valid ally. Select an ally to display info:"
    elif comm.upper() == "DISPLAY":
        askingally = True
        askingmsg = "Select an ally to display info:"
        while askingally:
            print(askingmsg)
            print("===============================")
            for i in allies:
                print(i.name)
            print("===============================")
            ally = input()
            for i in allies:
                if ally.upper() == i.name.upper():
                    #action that takes place
                    #displays all stats
                    i.display()
                    askingally = False
                    break
            else:
                askingmsg = "Not a valid ally. Select an ally to display info:"
    else:
        print("Invalid command")
