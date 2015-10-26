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
import time
#parent of all units - Person
weaponTriangle = [("Sword","Axe"),("Axe","Lance"),("Lance","Sword"),("Anima","Light"),("Dark","Anima"),("Light","Dark")]
#^list full of wt advantages (adv,disadv)

class Person:
    def __init__(self,name,hp,stren,skl,spd,lck,defen,res=0,con=5,items=[],growths=[50,50,50,50,50,50,50]):
        self.name = name #units name
        self.hp = hp #stats
        self.maxhp = hp
        self.strength = stren
        self.speed = spd
        self.attackspeed = spd #attack speed
        self.skill = skl
        self.defense = defen
        self.luck = lck
        self.resistance = res
        self.constitution = con
        self.equip = Weapon("No weapon",0,0,0,0,"",0)
        self.mounted = False #is unit mounted?
        self.alive = True #is unit alive?
        self.wskl = {"Sword":0,"Lance":0,"Axe":0,"Bow":0,
                     "Anima":0,"Dark":0,"Light":0,"Staff":0}#Weapon skill levels
        self.x = 0 #unit's position
        self.y = 0
        self.items = items
        self.weapons = [w for w in self.items if type(w) == Weapon] #weapons
        if self.weapons == []:
            self.weapons = [Weapon("No weapon",0,0,0,0,"",0)]
        self.growths = growths #growths are in the following format
                          #[hp,str,skl,spd,lck,def,res]
        self.level = 1
        self.canLevel = True #can unit level?
        self.exp = 0 #experience
        self.gift = 0 #amount of exp given when killed, only really matters for allies
        self.CLASS = "Person"
        self.MOVE = 5
        self.promoteC = "Person" #what class promotes to
        self.caps = [40,20,20,20,20,20,20]
        self.sym = "人" #symbol as appeared on map
        self.canAttack = False
        self.canMove = True
        self.flying = False
        self.mountainous = False
        self.waterproof = False
        self.magical = False
        self.maxspace = 5 #maximum item space: default is 5
        self.promoted = False #is unit promoted?
        self.deathQuote = ""
        self.fightQuote = ""
        self.attacked = False
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
        if self.hp > self.maxhp:
            self.hp = self.maxhp
        print(self.name,"healed by",hp,"up to",self.hp)
    def display(self):
        print("Name:",self.name)
        print("Class:",self.CLASS)
        print("Level:",self.level)
        print("HP: ",self.hp,"/",self.maxhp,sep="")
        print("Stength:",self.strength)
        print("Skill:",self.skill)
        print("Speed:",self.speed)
        print("Luck:",self.luck) 
        print("Defense:",self.defense)
        print("Resistance:",self.resistance)
        print("Constitution:",self.constitution)
        print("Equipped weapon:",self.equip.name)
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
                    if not self.skill >= self.caps[i]:
                        self.skill += 1
                        print("Skill increased to",self.skill)
                if i == 3 and self.growths[i] > random_number:
                    if not self.speed >= self.caps[i]:
                        self.speed += 1
                        self.attackspeed += 1
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
            if self.promoted:
                amount = amount//2
            if amount > 100:
                amount = 100
            self.exp += amount
            print(self.name,"gained",amount,"experience")
            if self.exp >= 100:
                self.exp -= 100
                self.levelUp()
            print("Exp:",self.exp,"/100")
    def promote(self):
        if promoteC == "Person":
            promoted = Person(self.name,self.maxhp,self.strength,self.speed,self.skill,self.defense,self.luck,self.resistance,self.constitution,self.growths)
            promoted.wskl = self.wskl
        return promoted
    def add_item(self,item,err=True):
        if len(self.items) >= self.maxspace:
            if err:
                print(self.name,'has a full inventory')
            return 0
        else:
            if err:
                print(self.name,"added",item.name,"to inventory")
            self.items.append(item)
            if type(item) == Weapon:
                if self.equip.name == "No weapon":
                    self.weapons = []
                self.weapons.append(item)
                if self.equip.name == "No weapon":
                    if self.CLASS != "Person":
                        self.equip_w(item,False)
            return 1
    def remove_item(self,item,err=True):
        if len(self.items) > 0:
            self.items.remove(item)
            if err:
                print(self.name,"removed",item.name)
            if type(item) == Weapon:
                self.weapons.remove(item)
                if len(self.weapons) == 0:
                    self.weapons = [Weapon("No weapon",0,0,0,0,"",0)]
            return True
        else:
            if err:
                print("No items to remove")
            return False
            
    def show_items(self,detailed=True):
        print("----------------------")
        for i in self.items:
            if detailed:
                i.display()
            else:
                print(i.name)
            print("----------------------")
    def move(self,x,y):
        self.x = x
        self.y = y
        print("Moved ",self.name," to (",x,",",y,")",sep = "")
        return True
    def calculate(self,enemy,terr=0,terr_def=0,unreal=True,stats=False):
        #persons can't attack
        if not self.canAttack:
            if not stats:
                print(self.name,"can't attack!")
            return False
    def attack(self,enemy,terr=0,terr_def=0):
        #persons can't attack
        print(self.name,"can't fight back!")
        return False
    
#Murderer Class is basis for all fighting classes
class Murderer(Person):
    def __init__(self,name,hp,stren,skl,spd,lck,defen,res=0,con=5,items=[],growths=[50,50,50,50,50,50,50]):
        super(Murderer,self).__init__(name,hp,stren,skl,spd,lck,defen,res,con,items,growths)
        self.CLASS = "Murderer"
        self.canAttack = True
        self.caps = [40,20,20,20,30,20,20]
        self.equip = self.weapons[0] if len(self.weapons) > 0 else Weapon("No weapon",0,0,0,0,"",0)
        if self.equip.wt > self.constitution:
            self.attackspeed += self.constitution - self.equip.wt
            if self.attackspeed < 0:
                self.attackspeed = 0
    def canAtk(self,enemy,otherweap=False,weap=Weapon("No weapon",0,0,0,0,"",0)):
        dist = abs(self.x - enemy.x) + abs(self.y - enemy.y)
        if otherweap:
            weapon = weap
        else:
            weapon = self.equip
        if not self.canAttack:
            return False
        elif weapon.rnge <= dist <= weapon.maxrnge:
            return True
        else:
            return False
    def calculate(self,enemy,terr=0,terr_def=0,unreal=True,stats=False):
        if not self.alive:
            return False
        global weaponTriangle
        mod = 0
        exdam = 0
        disoradv = ""
        for a,d in weaponTriangle:
            if self.equip.typ == a:
                if enemy.equip.typ == d:
                    mod = 20 #modifier for accuracy based on weapon triangle
                    exdam = 1 #extra damage
                    disoradv = "(Advantage)"
                    break
            if self.equip.typ == d:
                if enemy.equip.typ == a:
                    mod = -20
                    exdam = -1
                    disoradv = "(Disadvantage)"
                    break
        hit = self.skill*2 + self.equip.acc + self.luck//2 + mod - terr - enemy.attackspeed*2 - enemy.luck
        if hit < 0:
            hit = 0
        dam = self.equip.damage(self,enemy,True)+exdam-terr_def
        if dam < 0:
            dam = 0
        spdam = "x 2" if self.attackspeed - 4 >= enemy.attackspeed else ""
        crit = self.skill//2 - enemy.luck + self.equip.crit
        if crit < 0:
            crit = 0
        distx = abs(self.x - enemy.x)
        disty = abs(self.y - enemy.y)
        dist = distx + disty #enemy distance
        if not self.equip.rnge <= dist <= self.equip.maxrnge and not unreal:
            hit = "--"
            dam = "--"
            crit = "--"
            #displays no values if not in range
        if not stats:
            print(self.name)
            print("Weapon:",self.equip.name,disoradv)
            print("HP:",self.hp,"/",self.maxhp)
            print("Hit:",hit)
            print("Dam:",dam,spdam)
            print("Crit:",crit)
        if stats:
            if "--" in [hit,dam,crit]:
                return False #returns (damahe,hit,crit)
            else:
                return((dam,hit,crit))
    def attack(self,enemy,terr=0,terr_def=0):
        if not self.canAttack:
            return False
        if not self.alive or not enemy.alive:
            return False
        distx = abs(enemy.x - self.x)
        disty = abs(enemy.y - self.y)
        dist = distx + disty
        if not self.attacked and self.fightQuote != "":
            time.sleep(1)
            print(self.name,self.fightQuote,sep=": ")
        self.attacked = True
        if not enemy.attacked and enemy.fightQuote != "":
            time.sleep(1)
            print(enemy.name,enemy.fightQuote,sep=": ")
        enemy.attacked = True
        #distance of enemy to ally
        if not self.equip.rnge <= dist <= self.equip.maxrnge:
            #will not attack if not in range
            return -1
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
        if self.skill*2 + self.luck//2 + self.equip.acc - enemy.attackspeed*2 - enemy.luck - terr + mod > randint(0,99):
            self.strength += exdam - terr_def
            damage = self.equip.damage(self,enemy) #damage done to enemy
            self.strength -= exdam - terr_def
            expgain = damage-self.level+enemy.level #increasing exp
            if expgain > 30:
                expgain = 30 #caps exp gain at 30
            elif expgain <= 0:
                expgain = 1 #caps exp gain at 1
            if enemy.promoted:
                expgain += 20
            print(self.name,"attacked",enemy.name,"with",self.equip.name,"for",damage,"damage") #prints damage
            enemy.losehp(damage)#enemy loses hp
            if enemy.hp <= 0:
                if enemy.deathQuote != "":
                    print(enemy.name,enemy.deathQuote,sep=": ")
                time.sleep(1)
                print(enemy.name,"died")#if enemy dies it will print
                expgain += enemy.gift - self.level #adds more exp when en dies
            self.gainExp(expgain) #increasing exp
            self.w_experience(self.equip.wexp,self.equip.typ) #increasing wexp
            #if weapon breaks
            if self.equip.use():
                eq_newItem = False
                for i in range(1,len(self.items)):
                    if type(self.items[i]) == Weapon:
                        if self.equip_w(self.items[i],False):
                            #tries to equip every item in list.
                            #won't print error
                            eq_newItem = True
                            del self.weapons[self.weapons.index(self.items[i])]
                            del self.items[i]
                            break
                if not eq_newItem:
                    self.items.remove(self.equip)
                    self.weapons.remove(self.equip)
                    self.equip = Weapon("No weapon",0,0,0,0,"",0)
                    self.canAttack = False
            return 1
        else:
            print(self.name,"attacked",enemy.name,"but",enemy.name,"dodged")
            return 2
    def equip_w(self,weapon,err=True):
        #equips weapon
        if not type(weapon) == Weapon:
            if err:
               print("Not a weapon! Can't equip!") 
            return 0
        if not weapon in self.items:
            if err:
                print("Unit does not have this weapon!")
            return 0
        no_weapon = self.equip.name.lower() == "no weapon"
        if (not no_weapon and self.wskl[weapon.typ] >= weapon.mast) or (not no_weapon and self.name == weapon.prf):
            e_index = self.items.index(self.equip)
            w_index = self.items.index(weapon)
            self.items[e_index],self.items[w_index] = weapon,self.equip
        if self.wskl[weapon.typ] >= weapon.mast or self.name == weapon.prf:
            if err:
                print(self.name,"equipped",weapon.name)
            self.equip = weapon
            self.canAttack = True
            #changes attackspeed based on weapon
            if self.equip.wt > self.constitution:
                self.attackspeed = self.speed - self.equip.wt + self.constitution
                if self.attackspeed < 0:
                    self.attackspeed = 0
            else:
                self.attackspeed = self.speed
            return 1
        else:
            if err:
                print(self.name,"has not enough",weapon.typ,"mastery level to use",weapon.name)
            return 0
    def w_experience(self,wexp_g,typ):
        if (self.wskl[typ]+wexp_g)//100 > self.wskl[typ]//100:
            print(typ,"mastery level increased")
        self.wskl[typ] += wexp_g
        if self.wskl[typ] > 600:
            self.wskl[typ] = 600
    def display(self):
        super(Murderer,self).display()
        extrng = ""
        if not self.equip.rnge == self.equip.maxrnge:
            extrng = "- "+str(self.equip.maxrnge)
        print("Range:",self.equip.rnge,extrng)
        print("Experience:",self.exp,"/100")
        rankL = ["F","E","D","C","B","A","S"]
        for k,t in enumerate(self.wskl):
            if self.wskl[t] >= 100:
                print(t,rankL[self.wskl[t]//100])
#-----------LORD-------------#
class Lord(Murderer):
    def __init__(self,name,hp,stren,skl,spd,lck,defen,res=0,con=5,items=[],growths=[50,50,50,50,50,50,50]):
        super(Lord,self).__init__(name,hp,stren,skl,spd,lck,defen,res,con,items,growths)
        self.CLASS = "Lord"
        self.promoteC = "Nerd Lord"
        self.magical = True
        self.wskl["Sword"] = 200
        self.wskl["Anima"] = 100
#-----------MAGE-------------#
class Mage(Murderer):
    def __init__(self,name,hp,stren,skl,spd,lck,defen,res=0,con=5,items=[],growths=[50,50,50,50,50,50,50]):
        super(Mage,self).__init__(name,hp,stren,skl,spd,lck,defen,res,con,items,growths)
        self.CLASS = "Mage"
        self.promoteC = "Sage"
        self.magical = True
        self.wskl["Anima"] = 200
#----------KNIGHT------------#
class Knight(Murderer):
    def __init__(self,name,hp,stren,skl,spd,lck,defen,res=0,con=5,items=[],growths=[50,50,50,50,50,50,50]):
        super(Knight,self).__init__(name,hp,stren,skl,spd,lck,defen,res,con,items,growths)
        self.CLASS = "Knight"
        self.promoteC = "General"
        self.wskl["Lance"] = 200
        self.MOVE = 4
#---------MYRMIDON-----------#
class Myrmidon(Murderer):
    def __init__(self,name,hp,stren,skl,spd,lck,defen,res=0,con=5,items=[],growths=[50,50,50,50,50,50,50]):
        super(Myrmidon,self).__init__(name,hp,stren,skl,spd,lck,defen,res,con,items,growths)
        self.CLASS = "Myrmidon"
        self.promoteC = "Swordmaster"
        self.wskl["Sword"] = 200
#---------CAVALIER-----------#
class Cavalier(Murderer):
    def __init__(self,name,hp,stren,skl,spd,lck,defen,res=0,con=5,items=[],growths=[50,50,50,50,50,50,50]):
        super(Cavalier,self).__init__(name,hp,stren,skl,spd,lck,defen,res,con,items,growths)
        self.CLASS = "Cavalier"
        self.MOVE = 7
        self.mounted = True
        self.movesLeft = self.MOVE
        self.promoteC = "Paladin"
        self.wskl["Lance"] = 200
        self.wskl["Sword"] = 100
#---------FIGHTER-----------#
class Fighter(Murderer):
    def __init__(self,name,hp,stren,skl,spd,lck,defen,res=0,con=5,items=[],growths=[50,50,50,50,50,50,50]):
        super(Fighter,self).__init__(name,hp,stren,skl,spd,lck,defen,res,con,items,growths)
        self.CLASS = "Fighter"
        self.MOVE = 5
        self.wskl["Axe"] = 200
#-----------BRIGAND----------#
class Brigand(Murderer):
     def __init__(self,name,hp,stren,skl,spd,lck,defen,res=0,con=5,items=[],growths=[50,50,50,50,50,50,50]):
        super(Brigand,self).__init__(name,hp,stren,skl,spd,lck,defen,res,con,items,growths)
        self.CLASS = "Brigand"
        self.mountainous = True
        self.wskl["Axe"] = 200
#--------TRANSPORTER---------#
class Transporter(Person):
    def __init__(self,name,hp,stren,skl,spd,lck,defen,res=0,con=5,items=[],growths=[50,50,50,50,50,50,50]):
        super(Transporter,self).__init__(name,hp,stren,skl,spd,lck,defen,res,con,items,growths)
        self.mounted = True
        self.convoy = []
        self.CLASS = "Transporter"
    def transfer(self,item,take=False):
        if not take:
            if item not in self.convoy:
                print(self.name,"does not have this item in supply!")
                return False
            else:
                self.convoy.remove(item)
                return item
        else:
            if len(self.convoy) < 100:
                self.convoy.append(item)
                return True
            else:
                print(self.name,"'s storage is full!")
                return False
    def convoyLen(self):
        return len(self.convoy)
#----------PALADIN---------------#
class Paladin(Cavalier):
    def __init__(self,name,hp,stren,skl,spd,lck,defen,res=0,con=5,items=[],growths=[50,50,50,50,50,50,50]):
        super(Paladin,self).__init__(name,hp,stren,skl,spd,lck,defen,res,con,items,growths)
        self.CLASS = "Paladin"
        self.MOVE = 8
        self.movesLeft = self.MOVE
        self.wskl["Lance"] = 500
        self.wskl["Sword"] = 500
        self.wskl["Axe"] = 100
        self.promoted = True
