#You Zhou
#feweapons.py
#contains weapons for fire emblem game
from random import randint
class Weapon():
    def __init__(self,name,mt,wt,dur,acc,typ,crit=0,rnge=1,mag=False,sup_eff="",maxrnge=1):
        self.name = name
        self.mt = mt
        self.wt = wt
        self.dur = dur
        self.maxdur = dur
        self.acc = acc
        self.crit = crit
        self.rnge = rnge
        self.mag = mag
        self.typ = typ
        self.sup_eff = sup_eff
        self.maxrnge = maxrnge
        self.intact = True
    def use(self):
        self.dur -= 1
        if self.dur <= 0:
            self.intact = False
            print(name,"broke!")
    def damage(self,ally,enemy):
        if enemy.CLASS == self.sup_eff:
            might = self.mt*3
        else:
            might = self.mt
        if self.mag:
            defenses = enemy.resistance
        else:
            defenses = enemy.defense
        dmg = ally.strength + might - defenses
        if ally.dexterity//2 + self.crit - enemy.luck > randint(0,99):
            dmg *= 3
            print("CRITICAL HIT!")
        return dmg
        
