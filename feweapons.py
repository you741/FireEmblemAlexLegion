#You Zhou
#feweapons.py
#contains weapons for fire emblem game
#also contains items and terrain
from festaples import *
from random import randint
class Item:
    def __init__(self,name,dur,desc=""):
        self.maxdur = dur
        self.dur = dur
        self.name = name
        self.desc = desc
        self.intact=True
    def use(self): #decreases dur of item
        self.dur -= 1
        if self.dur <= 0:
            self.intact = False
            print(self.name,"broke!")
            return True #returns true if broken
        else:
            return False
    def display(self):
        print(self.name)
        print(self.dur,"/",self.maxdur)
        if not self.desc == "":
            print(self.desc)
class Weapon(Item):
    def __init__(self,name,mt,wt,dur,acc,typ,mast,crit=0,rnge=1,mag=False,sup_eff=[],maxrnge=1,wexp=3,desc="",prf=""):
        super(Weapon,self).__init__(name,dur,desc)
        self.mt = mt
        self.wt = wt
        self.wexp = wexp
        self.acc = acc
        self.crit = crit
        self.rnge = rnge
        self.mag = mag
        self.typ = typ
        self.mast = mast
        self.sup_eff = sup_eff
        self.maxrnge = maxrnge
        self.prf = prf

    def damage(self,ally,enemy,calc=False): #damage of weapon when user wields
        if enemy.CLASS in self.sup_eff:
            might = self.mt*3
        else:
            might = self.mt
        if self.mag:
            defenses = enemy.resistance
        else:
            defenses = enemy.defense
        dmg = ally.strength + might - defenses
        if ally.skill//2 + self.crit - enemy.luck > randint(0,99):
            if not calc:
                dmg *= 3
                print("CRITICAL HIT!")
        if dmg <= 0:
            dmg = 0
        return dmg
    def display(self):
        super(Weapon,self).display()
        print("Might:",self.mt)
        print("Weight:",self.wt)
        print("Accuracy:",self.acc)
        print("Critical Chance:",self.crit)
        rnge_tot = self.rnge if self.maxrnge == self.rnge else str(self.rnge)+"-"+str(self.maxrnge)
        #total range found by checking maximum range
        print("Range:",rnge_tot)
        rankL = ["F","E","D","C","B","A","S","Prf"]
        print("Weapon Mastery Required:",self.typ,rankL[self.mast//100])
#--------TERRAIN--------#
class Terrain:
    def __init__(self,name,sym,avo=0,defen=0,hind=0):
        self.name = name
        self.sym = sym
        self.avo = avo
        self.defen = defen
        self.hind = hind
