from random import randint
from feclasses import *
from feweapons import *
allies = []
enemies = []
name = input("Enter your name:\n")
name = name.upper()
askingclass = True
askmsg = "Enter your class (mage,knight,myrmidon) or info for more info:\n"
#common weapons
iron_lance = Weapon("Iron Lance",6,8,45,80,"Lance")
fire = Weapon("Fire",5,4,40,95,"Anima",0,1,True,"",2)
slim_sword = Weapon("Slim Sword",4,2,35,100,"Sword",5,1)
#asking user for class
while askingclass:
    playerclass = input(askmsg)
    if playerclass.lower() == "mage":
        player = Mage(name,18,5,5,6,2,5,4,4)
        player.equip = fire
        player.items.append(fire)
        askingclass = False
    if playerclass.lower() == "knight":
        player = Knight(name,21,6,3,4,8,3,1,10)
        player.equip = iron_lance
        player.items.append(iron_lance)
        askingclass = False
    if playerclass.lower() == "myrmidon":
        player = Myrmidon(name,20,5,6,6,4,4,2,6)
        player.equip = slim_sword
        player.items.append(slim_sword)
        askingclass = False
    if playerclass.lower() == "info":
        print("""Mage - A speedy and accurate user of anima magic. Ignores defense and melts enemies with low resistance.
Knight - A tanky lance-wielder. Gains a bit of health whenever attacked.
Myrmidon - A speedy sword user. Has chance of getting a critical hit.""")
        askmsg = "Enter your class (mage,knight,myrmidon) or info for more info:\n"      
    else:
        askmsg = "Your entry is invalid. Please enter mage, knight, myrmidon or info:\n"
allies.append(player)
#franny = 
running = True
#main game loop
while running:
    comm = input("Enter a command:\n")
    if comm.upper() == "QUIT":
        running = False
        print("You have quit and lost all progress")
    if comm.upper() == "ATTACK":
        pass
    if comm.upper() == "DISPLAY":
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
        
