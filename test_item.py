#!/usr/bin/env python
# -- coding: UTF-8 --
from core.item import Item, Apple, Spell

import unittest

class TestItems(unittest.TestCase):

    def testItemConstructor(self):
        i = Item("Poo", 50)
        self.assertEqual(i.name, "Poo")
        self.assertEqual(i.weight, 50)

    def testSpellConstructor(self):
        i = Spell("Fire", 1, 10, 30)
        self.assertEqual(i.name, "Fire")
        self.assertEqual(i.weight, 1)
        self.assertEqual(i.cost, 10)
        self.assertEqual(i.damage, 30)

    def testAppleConstructor(self):
        i = Apple(1, 30)
        self.assertEqual(i.name, "Apple")
        self.assertEqual(i.weight, 1)
        self.assertEqual(i.gain, 30)


if __name__ == '__main__':
    unittest.main()
