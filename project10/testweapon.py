'''
CS5001
Battle -- Weapon class test
Tuoxin Li
'''
from weapon import Weapon
import unittest

class TestWeapon(unittest.TestCase):

    # Testing the constructor
    def test_init_1(self):
        weapon1 = Weapon()
        #assertEquals, assertTrue, assertAlmostEqual, assertFalse
        self.assertEqual("Generic dagger", weapon1.name)
        self.assertEqual(1, weapon1.strength)
        self.assertEqual(1, weapon1.durability)

    def test_init_2(self):
        weapon2 = Weapon("Sword of infinity",50,3)
        #assertEquals, assertTrue, assertAlmostEqual, assertFalse
        self.assertEqual("Sword of infinity", weapon2.name)
        self.assertEqual(50, weapon2.strength)
        self.assertEqual(3, weapon2.durability)

    def test_attack_method(self):
        weapon1 = Weapon("Sword of infinity",50,3)
        for i in range(2,-1,-1):
            damage1=weapon1.attack()
            self.assertTrue(damage1>=1 and damage1<=50)
            self.assertEqual(i,weapon1.durability)
        damage1=weapon1.attack()
        self.assertEqual(0,damage1) #test when durability is 0, attack returns 0


def main():
    unittest.main()
main()
