#!/usr/bin/env python
# -- coding: UTF-8 --
from core.character import Character, Wizard, Warrior

import unittest

class TestCharacter(unittest.TestCase):

    def testCharacterConstructor(self):
        c = Character("Toto", 10, 20, 30, 40)
        self.assertEqual(c.name, "Toto")
        self.assertEqual(c.health, 10)
        self.assertEqual(c.mana, 20)
        self.assertEqual(c.power, 30)
        self.assertEqual(c.xp, 40)
        self.assertEqual(c.inventory, [])
    
    def testWizardConstructor(self):
        w = Wizard("Plop")
        self.assertEqual(w.name, "Plop")
        self.assertEqual(w.health, 100)
        self.assertEqual(w.mana, 100)
        self.assertEqual(w.power, 50)
        self.assertEqual(w.xp, 0)
        self.assertEqual(w.inventory, [])
        self.assertEqual(w.spells, [])

    def testWarriorConstructor(self):
        w = Warrior("Yup", 50)
        self.assertEqual(w.name, "Yup")
        self.assertEqual(w.health, 200)
        self.assertEqual(w.mana, 0)
        self.assertEqual(w.power, 300)
        self.assertEqual(w.xp, 0)
        self.assertEqual(w.inventory, [])
        self.assertEqual(w.armor, 50)

if __name__ == '__main__':
    unittest.main()
