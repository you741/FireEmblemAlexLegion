#You Zhou
#feclasses.py
#Fire Emblem Classes

#==============TODO==============#
# 1. Edit all attack values      #
#================================#

from random import randint
from feweapons import *
#parent of all units - Person
class Person:
    def __init__(self,name,hp,stren,spd,dex,defen,lck,res=0,con=5,growths=[50,50,50,50,50,50,50]):
        self.name = name
        self.hp = hp
        self.maxhp = hp
        self.strength = stren
        self.speed = spd
        self.dexterity = dex
        self.defense = defen
        self.luck = lck
        self.resistance = res
        self.constitution = con
        self.mounted = False
        self.alive = True
        self.equip = Weapon("No weapon",0,0,0,0,"")
        self.items = []
        self.growths = growths #growths are in the following format
                          #[hp,str,dex,spd,lck,def,res]
        self.level = 1
        self.CLASS = "Person"
    def losehp(self,damage):
        damage_t = damage - self.defense if not mag else damage - self.resistance
        if damage_t < 0:
            damage_t = 0
        self.hp -= damage_t
        if self.hp <= 0:
            self.hp = 0
            self.alive = False
        if damage_t == 0:
            damage_t = "no"
        return damage_t
    def gainhp(self,hp):
        self.hp += hp
        print(self.name,"healed by",hp,"up to",self.hp)
        if self.hp > self.maxhp:
            self.hp = self.maxhp
    def display(self):
        print("Name:",self.name)
        print("Class:",self.CLASS)
        print("Level:",self.level)
        print("HP: ",self.hp,"/",self.maxhp,sep="")
        print("Stength:",self.strength)
        print("Speed:",self.speed)
        print("Dexterity:",self.dexterity)
        print("Luck:",self.luck) 
        print("Defense:",self.defense)
        print("Resistance:",self.resistance)
        print("Constitution:",self.constitution)
        print("Equipped weapon:",self.equip.name)
    def levelUp(self):
        self.level += 1
        for i in range(len(self.growths)):
            if i == 0 and self.growths[i] > randint(0,99):
                self.maxhp += 1
                print("Maximum HP increased to",self.maxhp)
            if i == 1 and self.growths[i] > randint(0,99):
                self.strength += 1
                print("Strength increased to",self.strength)
            if i == 2 and self.growths[i] > randint(0,99):
                self.dexterity += 1
                print("Dexterity increased to",self.dexterity)
            if i == 3 and self.growths[i] > randint(0,99):
                self.speed += 1
                print("Speed increased to",self.speed)
            if i == 4 and self.growths[i] > randint(0,99):
                self.luck += 1
                print("Luck increased to",self.luck)
            if i == 5 and self.growths[i] > randint(0,99):
                self.defense += 1
                print("Defense increased to",self.defense)
            if i == 6 and self.growths[i] > randint(0,99):
                self.resistance += 1
                print("Resistance increased to",self.resistance)
            
#Murderer Class is basic for all fighting classes
class Murderer(Person):
    def __init__(self,name,hp,stren,spd,dex,defen,lck,res=0,con=5,growths=[50,50,50,50,50,50,50]):
        super(Murderer,self).__init__(name,hp,stren,spd,dex,defen,lck,res,con,growths)
        self.CLASS = "Murderer"
    def losehp(self,damage):
        return super(Murderer,self).losehp(damage)
    def gainhp(self,hp):
        super(Murderer,self).gainhp(hp)
    def attack(self,enemy):
        if self.dex*2 + accuracy - enemy.spd*2 > randint(0,100):
            damage_t = enemy.losehp(self.strength)
            print(self.name,"attacked",enemy.name,"for",damage_t,"damage")
            if enemy.hp <= 0:
                print(enemy.name,"died")
#-----------MAGE-------------#
class Mage(Murderer):
    def __init__(self,name,hp,stren,spd,dex,defen,lck,res=0,con=5,growths=[50,50,50,50,50,50,50]):
        super(Mage,self).__init__(name,hp,stren,spd,dex,defen,lck,res,con,growths)
        self.CLASS = "Mage"
    def losehp(self,damage):
        return super(Mage,self).losehp(damage)
    def gainhp(self,hp):
        super(Mage,self).gainhp(hp)
    def attack(self,enemy,accuracy=95):
        if self.dex*2 + accuracy - enemy.spd*2 > randint(0,100):
            damage_t = enemy.losehp(self.strength,True)
            print(self.name,"attacked",enemy.name,"for",damage_t,"damage")
            if enemy.hp <= 0:
                print(enemy.name,"died")
        else:
            print(self.name,"attacked",enemy.name,"but",enemy.name,"dodged")
#----------KNIGHT------------#
class Knight(Murderer):
    def __init__(self,name,hp,stren,spd,dex,defen,lck,res=0,con=5,growths=[50,50,50,50,50,50,50]):
        super(Knight,self).__init__(name,hp,stren,spd,dex,defen,lck,res,con,growths)
        self.CLASS = "Knight"
    def losehp(self,damage):
        return super(Knight,self).losehp(damage)
    def gainhp(self,hp):
        super(Knight,self).gainhp(hp)
    def attack(self,enemy,accuracy=80):
        if self.dex*2 + accuracy - enemy.spd*2 > randint(0,100):
            damage_t = enemy.losehp(self.strength,True)
            print(self.name,"attacked",enemy.name,"for",damage_t,"damage")
            if enemy.hp <= 0:
                print(enemy.name,"died")
        else:
            print(self.name,"attacked",enemy.name,"but",enemy.name,"dodged")
#---------MYRMIDON-----------#
class Myrmidon(Murderer):
    def __init__(self,name,hp,stren,spd,dex,defen,lck,res=0,con=5,growths=[50,50,50,50,50,50,50]):
        super(Myrmidon,self).__init__(name,hp,stren,spd,dex,defen,lck,res,con,growths)
        self.CLASS = "Myrmidon"
    def losehp(self,damage):
        return super(Myrmidon,self).losehp(damage)
    def gainhp(self,hp):
        super(Myrmidon,self).gainhp(hp)
    def attack(self,enemy,accuracy=90):
        if self.dex*2 + accuracy - enemy.spd*2 > randint(0,100):
            if self.dex//2 > randint(0,100):
                damage_t = enemy.losehp(self.strength*2,True)
                print(self.name,"attacked",enemy.name,"with a critical hit for",damage_t,"damage")
            else:
                damage_t = enemy.losehp(self.strength,True)
                print(self.name,"attacked",enemy.name,"for",damage_t,"damage")
            if enemy.hp <= 0:
                print(enemy.name,"died")
        else:
            print(self.name,"attacked",enemy.name,"but",enemy.name,"dodged")
#INCOMPLETE BELOW#
class Cavalier(Murderer):
    def __init__(self,name,hp,stren,spd,dex,defen,lck,res=0,con=5,growths=[50,50,50,50,50,50,50]):
        super(Cavalier,self).__init__(name,hp,stren,spd,dex,defen,lck,res,con,growths)
        self.CLASS = "Cavalier"
        self.mounted = True
    def losehp(self,damage):
        return super(Cavalier,self).losehp(damage)
    def gainhp(self,hp):
        super(Cavalier,self).gainhp(hp)
    def attack(self,enemy,accuracy=90):
        if self.dex*2 + accuracy - enemy.spd*2 > randint(0,100):
            if self.dex//2 > randint(0,100):
                damage_t = enemy.losehp(self.strength*2,True)
                print(self.name,"attacked",enemy.name,"with a critical hit for",damage_t,"damage")
            else:
                damage_t = enemy.losehp(self.strength,True)
                print(self.name,"attacked",enemy.name,"for",damage_t,"damage")
            if enemy.hp <= 0:
                print(enemy.name,"died")
        else:
            print(self.name,"attacked",enemy.name,"but",enemy.name,"dodged")
