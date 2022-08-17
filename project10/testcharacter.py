
'''
CS5001
Battle -- Character class test
Tuoxin Li
'''
from character import Character
from weapon import Weapon
import unittest
import random 

class TestCharacter(unittest.TestCase):

    # Testing the constructor
    def test_init(self):
        #test character's status
        c1 = Character("Peter", 30, 15, 2, 50)
        #assertEquals, assertTrue, assertAlmostEqual, assertFalse
        self.assertEqual("Peter", c1.name)
        self.assertEqual(30, c1.hitPoints)
        self.assertEqual(15, c1.strength)
        self.assertEqual(2, c1.defense)
        self.assertEqual(50,c1.critic)

    def test_take_damage_method(self):
        c1 = Character("Nick", 30, 15,1,0)
        c1.take_damage(5)
        self.assertEqual(25, c1.hitPoints) #Test take tamage method, it's 25 because the defense is applied in attack method

        c2 = Character("Briggs", 20, 10)
        c2.take_damage(100)
        self.assertEqual(0, c2.hitPoints)
        self.assertFalse(c2.alive)

    def test_attack_method(self):
        #test attack method
        c1 = Character("Hero", 20, 10, 1, 0)
        c2 = Character("Monster", 20, 10, 1, 0)
        damage = random.randint(1,c1.strength)

        self.assertTrue(damage >= 1 and damage <= 20)
        c1.attack(c2)

        self.assertTrue(c2.hitPoints <= 20) #here defense could work so it can equal to 20

    def test_take_weapon_method(self):
        c1 = Character("Hero", 20, 1, 0, 0)
        c2 = Character("Monster", 20, 10, 0, 0)
        w1 = Weapon("Generic sword", 5, 1)
        c1.take_weapon(w1)
        c1.attack(c2)
        self.assertTrue(c2.hitPoints<19 and c2.hitPoints>=14)
        c1.attack(c2)
        self.assertTrue(c2.hitPoints>=14)#Test if weapon deal damage when the durability drops 0

def main():
    unittest.main()
main()



