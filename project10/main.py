'''
Tuoxin Li
Battle Arena
04/20/2022
'''

from character import Character
from weapon import Weapon
import time

def line():
    '''
    Return: a line
    '''
    print("------------------------------------------")

def main():
    flag=True
    while flag: #Game loop, quit when user input no
        #Characters and weapons
        c1=Character("Target",100,1,1)
        c2=Character("Sakiro",75,10,0,50)
        c3=Character("Ancient Spirit",100,5,2,20)
        c4=Character("Dragon Killer",100,2,3,80)
        w1 = Weapon("Knight Spear", 8, 8)
        w2 = Weapon("Sword of Infinity",20,5)
        w3 = Weapon("Bow of Stars",5, 20)
        w4 = Weapon("One punch", 100, 1)

        list1=[]
        list2=[]
        list3=[]
        list4=[]

        def select_weapon(w):
            '''
            Function: give the according object in terms of users' input 
            '''
            if w=="Knight Spear":
                return w1
            elif w=="Sword of Infinity":
                return w2
            elif w=="Bow of Stars":
                return w3
            elif w=="One punch":
                return w4
            else: 
                print("Not the weapon in the list")

        def select_character(c):
            '''
            Function: give the according object in terms of users' input
            '''
            if c== "Target":
                return c1
            elif c=="Sakiro":
                return c2
            elif c=="Ancient Spirit":
                return c3
            elif c=="Dragon Killer":
                return c4
        #creat list and dictionary for characters and weapons
        character_list=[c1,c2,c3,c4]
        character_dic={c1:"Target",c2:"Sakiro",c3:"Ancient Spirit",c4:"Dragon Killer"}
        weapon_list=[w1,w2,w3,w4]
        weapon_dic={w1:"Knight Spear",w2:"Sword of Infinity",w3:"Bow of Stars",w4:"One punch"}
        
        #Build the game frame
        line()
        #Choosing champion
        print("The characters you can choose:")
        for i in character_list: #Avoid user input whatever not in the list
            print(character_dic[i])
            list1.append(character_dic[i])
        champion=input("\nSelect your champion: ")
        while not champion in list1:
            champion=input("\nNot a choice. Select your champion again: ")
        champion=select_character(champion)
        character_list.remove(champion) #remove the character from the list after the character is chosen
        line()
        time.sleep(1.0)
        #Choosing chanllenger
        print("The characters you can choose:")
        for i in character_list:
            print(character_dic[i])
            list2.append(character_dic[i])
        chanllenger=input("\nSelect the chanllenger: ")
        while not chanllenger in list2:
            chanllenger=input("\nNot a choice. Select your chanllenger again: ")
        chanllenger=select_character(chanllenger)
        character_list.remove(chanllenger)
        line()
        time.sleep(1.0)
        #Equit champion with the weapon
        print("For "+champion.name+", which weapon do you assign")
        print("The available weapons are: ")
        for j in weapon_list:
            print(weapon_dic[j])
            list3.append(weapon_dic[j])
        weapon_champ=input("\nChoose the weapon: ")
        while not weapon_champ in list3:
            weapon_champ=input("\nNot a choice. Select the weapon again: ")
        weapon_champ=select_weapon(weapon_champ)
        champion.take_weapon(weapon_champ)
        weapon_list.remove(weapon_champ) #remove the weapon from the list after the weapon is chosen
        line()
        time.sleep(1.0)
        #Equit chanllenger with the weapon
        print("For "+chanllenger.name+", which weapon do you assign")
        print("The available weapons are: ")
        for j in weapon_list:
            print(weapon_dic[j])
            list4.append(weapon_dic[j])
        weapon_chanl=input("\nChoose the weapon: ")
        while not weapon_chanl in list4:
            weapon_chanl=input("\nNot a choice. Select the weapon again: ")
        weapon_chanl=select_weapon(weapon_chanl)
        chanllenger.take_weapon(weapon_chanl)
        weapon_list.remove(weapon_chanl) #remove the weapon from the list after the weapon is chosen
        line()
        time.sleep(1.0)
        print("Ready for the fight!")
        time.sleep(1.0)
        print("Fight!")
        time.sleep(1.0)
        champion.fight(chanllenger)
        line()
        game=input("Do you wanna play again? Enter 'No' to quit, otherwise, continue the game.\nEnter your choice: ")
        if game =="No":#Game Loop
            flag=False
        
main()