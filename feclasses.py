#You Zhou
#feclasses.py
#Fire Emblem Classes

#==============TODO==============#
#   1. Finalize weapon exp func  #
#   (In feweapons, say when rank #
#   up)                          # 
#   2. Finish equip functions and#
#  the check if unit has enough  #
#  weapon mastery to use a weapon#
#================================#

#=========Recent Updates===========#
# Finalized experience gain through#
# attacks and kills                #
# Finished in class weapon rank    #
# display                          #
# Made calculation function,       #
# calculates damage and hit rate   #
#==================================#
from random import randint
from festaples import *
from feweapons import *
#parent of all units - Person
weaponTriangle = [("Sword","Axe"),("Axe","Lance"),("Lance","Sword"),("Anima","Light"),("Dark","Anima"),("Light","Dark")]
#^list full of wt advantages (adv,disadv)

class Person:
    def __init__(self,name,hp,stren,dex,spd,lck,defen,res=0,con=5,growths=[50,50,50,50,50,50,50]):
        self.name = name #units name
        self.hp = hp #stats
        self.maxhp = hp
        self.strength = stren
        self.speed = spd
        self.dexterity = dex
        self.defense = defen
        self.luck = lck
        self.resistance = res
        self.constitution = con
        self.mounted = False #is unit mounted?
        self.alive = True #is unit alive?
        self.equip = Weapon("No weapon",0,0,0,0,"",0)
        self.wskl = {"Sword":0,"Lance":0,"Axe":0,"Bow":0,
                     "Anima":0,"Dark":0,"Light":0,"Staff":0}#Weapon skill levels
        self.x = 0 #unit's position
        self.y = 0
        self.items = []
        self.growths = growths #growths are in the following format
                          #[hp,str,dex,spd,lck,def,res]
        self.level = 1
        self.canLevel = True #can unit level?
        self.exp = 0 #experience
        self.gift = 0 #amount of exp given when killed, only really matters for allies
        self.CLASS = "Person"
        self.MOVE = 5
        self.promoteC = "Person" #what class promotes to
        self.caps = [40,20,20,20,20,20,20]
        self.sym = "人" #symbol as appeared on map
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
        print(self.name,"has",self.hp,"HP")
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
        print("Dexterity:",self.dexterity)
        print("Speed:",self.speed)
        print("Luck:",self.luck) 
        print("Defense:",self.defense)
        print("Resistance:",self.resistance)
        print("Constitution:",self.constitution)
        print("Equipped weapon:",self.equip.name)
        rankL = ["F","E","D","C","B","A","S"]
        for k,t in enumerate(self.wskl):
            if self.wskl[t] >= 100:
                print(t,rankL[self.wskl[t]//100])
    def levelUp(self):
        if self.canLevel:            
            self.level += 1
            if self.level >= 20:
                self.canLevel = False #makes user unable to level past 20
                self.exp = 0
            print(self.name,"leveled up!")
            print(self.CLASS,"level",self.level)
            for i in range(len(self.growths)):
                random_number = randint(0,99)
                if i == 0 and self.growths[i] > random_number:
                    if not self.maxhp >= self.caps[i]:
                        self.maxhp += 1
                        print("Maximum HP increased to",self.maxhp)
                if i == 1 and self.growths[i] > random_number:
                    if not self.strength >= self.caps[i]:
                        self.strength += 1
                        print("Strength increased to",self.strength)
                if i == 2 and self.growths[i] > random_number:
                    if not self.dexterity >= self.caps[i]:
                        self.dexterity += 1
                        print("Dexterity increased to",self.dexterity)
                if i == 3 and self.growths[i] > random_number:
                    if not self.speed >= self.caps[i]:
                        self.speed += 1
                        print("Speed increased to",self.speed)
                if i == 4 and self.growths[i] > random_number:
                    if not self.luck >= self.caps[i]:
                        self.luck += 1
                        print("Luck increased to",self.luck)
                if i == 5 and self.growths[i] > random_number:
                    if not self.defense >= self.caps[i]:    
                        self.defense += 1
                        print("Defense increased to",self.defense)
                if i == 6 and self.growths[i] > random_number:
                    if not self.resistance >= self.caps[i]:
                        self.resistance += 1
                        print("Resistance increased to",self.resistance)
    def gainExp(self,amount=1):
        if self.canLevel:
            self.exp += amount
            if amount > 100:
                amount = 100
            print(self.name,"gained",amount,"experience")
            if self.exp >= 100:
                self.exp -= 100
                self.levelUp()
            print("Exp:",self.exp,"/100")
    def promote(self):
        if promoteC == "Person":
            promoted = Person(self.name,self.maxhp,self.strength,self.speed,self.dexterity,self.defense,self.luck,self.resistance,self.constitution,self.growths)
            promoted.wskl = self.wskl
        return promoted
    def add_item(self,item):
        if len(self.items) >= 5:
            print(self.name,'has a full inventory')
            return 0
        else:
            print(self.name,"added",item.name,"to inventory")
            self.items.append(item)
            return 1 
    
#Murderer Class is basis for all fighting classes
class Murderer(Person):
    def __init__(self,name,hp,stren,dex,spd,lck,defen,res=0,con=5,growths=[50,50,50,50,50,50,50]):
        super(Murderer,self).__init__(name,hp,stren,dex,spd,lck,defen,res,con,growths)
        self.CLASS = "Murderer"
    def calculate(self,enemy,terr=0):
        if not self.alive:
            return False
        global weaponTriangle
        mod = 0
        exdam = 0
        for a,d in weaponTriangle:
            if self.equip.typ == a:
                if enemy.equip.typ == d:
                    mod = 20 #modifier for accuracy based on weapon triangle
                    exdam = 1 #extra damage
                    break
            if self.equip.typ == d:
                if enemy.equip.typ == a:
                    mod = -20
                    exdam = -1
                    break
        print(self.name)
        print("HP:",self.hp,"/",self.maxhp)
        print("Hit:",self.dexterity*2 + self.equip.acc + self.luck//2 + mod + terr - enemy.speed*2 - enemy.luck)
        spdam = "x2" if self.speed - 4 >= enemy.speed else ""
        print("Dam:",self.equip.damage(self,enemy)+exdam,spdam)
        print("Crit:",self.dexterity//2 - enemy.luck + self.equip.crit)
    def attack(self,enemy,terr=0):
        if not self.alive:
            return False
        global weaponTriangle
        mod = 0
        exdam = 0
        for a,d in weaponTriangle:
            if self.equip.typ == a:
                if enemy.equip.typ == d:
                    mod = 20 #modifier for accuracy based on weapon triangle
                    exdam = 1 #extra damage
                    break
            if self.equip.typ == d:
                if enemy.equip.typ == a:
                    mod = -20
                    exdam = -1
                    break
        #calculates if enemy was hit   
        if self.dexterity*2 + self.luck//2 + self.equip.acc - enemy.speed*2 - enemy.luck + terr + mod > randint(0,99):
            damage = self.equip.damage(self,enemy)+exdam #damage done to enemy
            self.wskl[self.equip.typ] += self.equip.wexp #increasing wexp
            expgain = damage-self.level #increasing exp
            if expgain > 20:
                expgain = 20 #caps exp gain at 20
            elif expgain <= 0:
                expgain = 1 #caps exp gain at 1
            print(self.name,"attacked",enemy.name,"for",damage,"damage") #prints damage
            enemy.losehp(damage)#enemy loses hp
            if enemy.hp <= 0:
                print(enemy.name,"died") #if enemy dies it will print
                expgain += enemy.gift - self.level #adds more exp when en dies
            self.gainExp(expgain)
            if self.equip.use():
                self.items.remove(self.equip)
                eq_newItem = False
                for i in items:
                    if type(i) == Weapon:
                        if self.equip_w(i,False):
                            #tries to equip every item in list.
                            #won't print error
                            eq_newItem = True
                            break
                if not eq_newItem:
                    self.equip_w(Weapon("No weapon",0,0,0,0,"",0))
            return 1
        else:
            print(self.name,"attacked",enemy.name,"but",enemy.name,"dodged")
            return 0
    def equip_w(self,weapon,err=True):
        #equips weapon
        if self.items.index(weapon) == -1:
            print("Unit does not have this weapon!")
            return 0
        if self.equip.name.lower() != "no weapon" and self.wskl[weapon.typ] >= weapon.mast:
            e_index = self.items.index(self.equip)
            w_index = self.items.index(weapon)
            self.items[e_index],self.items[w_index] = weapon,self.equip
        if self.wskl[weapon.typ] >= weapon.mast:
            print(self.name,"equipped",weapon.name)
            self.equip = weapon
            return 1
        else:
            if not err:
                print(self.name,"has not enough",weapon.typ,"mastery level to use",weapon.name)
            return 0
#-----------MAGE-------------#
class Mage(Murderer):
    def __init__(self,name,hp,stren,dex,spd,lck,defen,res=0,con=5,growths=[50,50,50,50,50,50,50]):
        super(Mage,self).__init__(name,hp,stren,dex,spd,lck,defen,res,con,growths)
        self.CLASS = "Mage"
        self.promoteC = "Sage"
#----------KNIGHT------------#
class Knight(Murderer):
    def __init__(self,name,hp,stren,dex,spd,lck,defen,res=0,con=5,growths=[50,50,50,50,50,50,50]):
        super(Knight,self).__init__(name,hp,stren,dex,spd,lck,defen,res,con,growths)
        self.CLASS = "Knight"
        self.promoteC = "General"
        self.MOVE = 4
#---------MYRMIDON-----------#
class Myrmidon(Murderer):
    def __init__(self,name,hp,stren,dex,spd,lck,defen,res=0,con=5,growths=[50,50,50,50,50,50,50]):
        super(Myrmidon,self).__init__(name,hp,stren,dex,spd,lck,defen,res,con,growths)
        self.CLASS = "Myrmidon"
        self.promoteC = "Swordmaster"
#---------CAVALIER-----------#
class Cavalier(Murderer):
    def __init__(self,name,hp,stren,dex,spd,lck,defen,res=0,con=5,growths=[50,50,50,50,50,50,50]):
        super(Cavalier,self).__init__(name,hp,stren,dex,spd,lck,defen,res,con,growths)
        self.CLASS = "Cavalier"
        self.mounted = True
        self.promoteC = "Paladin"
        self.MOVE = 7
