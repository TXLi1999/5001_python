'''
CS5001
Battle -- Character class
Tuoxin Li
'''
import random
import time
from weapon import Weapon


class Character:
    '''
    This class is used to create characters
    '''
    def __init__(self,name="", hitPoints=1,strength=1, defense=1,critic=0):
        self.name= name 
        self.hitPoints=hitPoints #Character hitpoint or healthpoint
        self.max_health=hitPoints #Character max hp, for the convenience to build health bar
        self.strength=strength 
        self.defense=defense #related to the taken damage
        self.critic=critic #chance to cause dounble damage
        self.weapon=Weapon() #The default weapon is dagger
        self.alive=True

    def __str__(self):
        '''
        print character's status
        '''
        return self.name+"  HP:"+str(self.hitPoints)+"  AD:"+str(self.strength)+"  DF:"+str(self.defense)

    def health_bar(self):
        '''
        show character's health with a bar, '#' presents the current health
        '''
        total=20
        count=int(self.hitPoints/self.max_health*total)
        if (count==0 and self.alive):
            count=1 #When count is 0 but character is alive, we should show the health bar
        print(self.name +" health: "+"["+"#"*count+" "*(total-count)+"]")

    def take_weapon(self,weapon=Weapon()):
        '''
        equip the character with a weapon, so he can deal more damage
        '''
        self.weapon=weapon
        print(self.name+" takes "+self.weapon.name)

    def take_damage(self,damage):
        self.hitPoints-=damage
        if self.hitPoints<0: self.hitPoints=0
        if self.hitPoints<=0: self.alive=False

    def attack(self,victim,type=1):
        '''
        method: the character deal tamage to victim.
        type: 1 or 2 to get defferent printing message
        '''
        damage= random.randint(1,self.strength)+self.weapon.attack() #damage equals to character's strength plus the damage of the weapon he takes 
        n=random.randint(1,100) #To randomly deal the crit
        if self.critic>=n:
            damage=damage*2
            print(self.name+" crits!")
            time.sleep(1.0)
        if damage<=victim.defense:
            damage=0
            victim.take_damage(damage)
        elif damage>victim.defense:
            damage=damage-victim.defense
            victim.take_damage(damage)
        if type ==1:    
            print(self.name+" strikes "+victim.name+" for "+ str(damage)+" damage")
        elif type==2:
            if damage!=0:
                print(victim.name+ " defends against the attack but still lost "+str(damage)+" HP")
            elif damage == 0:
                print(victim.name +" blocks the attack")

    def fight(self,challenger):
        '''
        method:showing the information that character fight with chanllenger until the health of one of them drops 0  
        '''
        while self.alive and challenger.alive:
            time.sleep(1.0)
            self.health_bar()
            challenger.health_bar()
            time.sleep(1.0)
            self.attack(challenger,1)
            time.sleep(1.0)
            if not challenger.alive: 
                print("---------------------------------------------")            
                break
            challenger.attack(self,2)
            time.sleep(1.0)
            print("--------------------------------------------")
        self.health_bar()
        challenger.health_bar()
        time.sleep(1.0)
        if self.alive: print (self.name+ " won")
        else: print(challenger.name+" won")
    
#Test information
#c1=Character("TX",10,5,2)
#c2=Character("Monster",20,3,0)
#weapon1=Weapon("sword",20,2)
#c1.take_weapon(weapon1)
#c1.attack(c2)
#print(c1)
#c1.take_damage(10)
#c1.health_bar()
#c1.fight(c2)
#print(c1.hitPoints)