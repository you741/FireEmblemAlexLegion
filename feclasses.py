#You Zhou
#feclasses.py
#Fire Emblem Classes

#==============TODO==============#
#                                #
#================================#

#=========Recent Updates=========#
# Finalized attack methods       #
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
        self.mast1 = 0 #sword mastery
        self.mast2 = 0 #axe mastery
        self.mast3 = 0 #lance mastery
        self.mast4 = 0 #bow mastery
        self.mast5 = 0 #anima mastery
        self.mast6 = 0 #dark mastery
        self.mast7 = 0 #light mastery
        self.mast8 = 0 #staff mastery
        self.x = 0
        self.y = 0
        self.items = []
        self.growths = growths #growths are in the following format
                          #[hp,str,dex,spd,lck,def,res]
        self.level = 1
        self.CLASS = "Person"
    def losehp(self,damage):
        damage_t = damage
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
            
#Murderer Class is basis for all fighting classes
class Murderer(Person):
    def __init__(self,name,hp,stren,spd,dex,defen,lck,res=0,con=5,growths=[50,50,50,50,50,50,50]):
        super(Murderer,self).__init__(name,hp,stren,spd,dex,defen,lck,res,con,growths)
        self.CLASS = "Murderer"
    def attack(self,enemy,terr=0):
        if self.dexterity*2 + self.luck//2 + self.equip.acc - enemy.speed*2 - enemy.luck + terr > randint(0,99):
            damage_t = enemy.losehp(self.equip.damage(self,enemy))
            print(self.name,"attacked",enemy.name,"for",damage_t,"damage")
            if enemy.hp <= 0:
                print(enemy.name,"died")
        else:
            print(self.name,"attacked",enemy.name,"but",enemy.name,"dodged")
#-----------MAGE-------------#
class Mage(Murderer):
    def __init__(self,name,hp,stren,spd,dex,defen,lck,res=0,con=5,growths=[50,50,50,50,50,50,50]):
        super(Mage,self).__init__(name,hp,stren,spd,dex,defen,lck,res,con,growths)
        self.CLASS = "Mage"
        self.mast5 = 2
#----------KNIGHT------------#
class Knight(Murderer):
    def __init__(self,name,hp,stren,spd,dex,defen,lck,res=0,con=5,growths=[50,50,50,50,50,50,50]):
        super(Knight,self).__init__(name,hp,stren,spd,dex,defen,lck,res,con,growths)
        self.CLASS = "Knight"
        self.mast2 = 2
#---------MYRMIDON-----------#
class Myrmidon(Murderer):
    def __init__(self,name,hp,stren,spd,dex,defen,lck,res=0,con=5,growths=[50,50,50,50,50,50,50]):
        super(Myrmidon,self).__init__(name,hp,stren,spd,dex,defen,lck,res,con,growths)
        self.CLASS = "Myrmidon"
    def losehp(self,damage):
        return super(Myrmidon,self).losehp(damage)
    def gainhp(self,hp):
        super(Myrmidon,self).gainhp(hp)
#INCOMPLETE BELOW#
class Cavalier(Murderer):
    def __init__(self,name,hp,stren,spd,dex,defen,lck,res=0,con=5,growths=[50,50,50,50,50,50,50]):
        super(Cavalier,self).__init__(name,hp,stren,spd,dex,defen,lck,res,con,growths)
        self.CLASS = "Cavalier"
        self.mounted = True
