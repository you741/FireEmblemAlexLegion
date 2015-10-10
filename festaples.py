#festaples.py
#includes all fire emblem stable functions and variables. Includes movement func
from feclasses import *
from feweapons import *
from classFun import *
from random import randint
class festaples():
    def __init__(self):
        self.weaponTriangle = [("Sword","Axe"),("Axe","Lance"),("Lance","Sword"),("Anima","Light"),("Dark","Anima"),("Light","Dark")]
#^list full of wt advantages (adv,disadv)
