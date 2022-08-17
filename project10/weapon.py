'''
CS5001
Battle -- Weapon class
Tuoxin Li
'''
import random
class Weapon:
    '''
    This class is used to create weapons
    '''
    def __init__(self,name="Generic dagger",strength=1,durability=1):
        self.name=name
        self.strength=strength
        self.durability=durability
    def __str__(self) -> str:
        return self.name+"  Strength:"+str(self.strength)+"  Durability:"+str(self.durability)

    def attack(self):
        '''
        method: deal the damage between 1 and the weapon's strength, and durability decreases 1 after attack. Deal 0 damage when durability drops 0
        '''
        if self.durability>0:
            self.durability-=1
            return random.randint(1,self.strength)
        if self.durability==0:
            return 0

'''
TEST:
sword=Weapon("sword",10,2)
print(sword.attack())
print(sword.attack())
print(sword.attack())
print(sword)
'''
'''
weapon2 = Weapon("Sword of infinity",50,3)
for i in range(2,0,-1):
    damage1=weapon2.attack()
    print(i)
    print(damage1)
    print(weapon2)
damage1=weapon2.attack()
print(damage1)
print(weapon2)
'''
