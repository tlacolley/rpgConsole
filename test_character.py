#!/usr/bin/env python
# -- coding: UTF-8 --
from core.character import Character, Wizard, Warrior
from core.item import Item, Apple, Spell
import unittest

class TestCharacter(unittest.TestCase):

    def testCharacterConstructor(self):
        c = Character("Toto", 10, 20, 30, 40)
        self.assertEqual(c.name, "Toto")
        self.assertEqual(c.health, 10)
        self.assertEqual(c.mana, 20)
        self.assertEqual(c.power, 30)
        self.assertEqual(c.xp, 40)
        self.assertListEqual(c.inventory, [])

    def testWizardConstructor(self):
        w = Wizard("Plop")
        self.assertEqual(w.name, "Plop")
        self.assertEqual(w.health, 100)
        self.assertEqual(w.mana, 100)
        self.assertEqual(w.power, 50)
        self.assertEqual(w.xp, 0)
        self.assertListEqual(w.inventory, [])
        self.assertListEqual(w.spells, [])

    def testWarriorConstructor(self):
        w = Warrior("Yup", 50)
        self.assertEqual(w.name, "Yup")
        self.assertEqual(w.health, 200)
        self.assertEqual(w.mana, 0)
        self.assertEqual(w.power, 300)
        self.assertEqual(w.xp, 0)
        self.assertListEqual(w.inventory, [])
        self.assertEqual(w.armor, 50)

    def testAttackEnemy(self):
        plop = Character("Plop", 10, 20, 30, 40)
        yup = Character("Yup", 10, 20, 30, 40)

        plop_xp_before_attack = plop.xp
        yup_health_before_attack = yup.health

        plop.attack(yup)
        self.assertGreater(plop.xp, plop_xp_before_attack)
        self.assertLess(yup.health, yup_health_before_attack)

    def testPickItem(self):
        plop = Character("Plop", 10, 20, 30, 40)
        item = Item("Poo", 50)
        item2 = Item("Yak", 50)
        item3 = Item("Prout", 50)

        plop.pick(item)
        self.assertListEqual(plop.inventory, [item])

        plop.pick(item2)
        plop.pick(item3)
        self.assertListEqual(plop.inventory, [item, item2, item3])

    def testDropItem(self):
        plop = Character("Plop", 10, 20, 30, 40)
        item = Item("Poo", 50)
        item2 = Item("Yak", 50)
        item3 = Item("Prout", 50)

        plop.pick(item)
        self.assertListEqual(plop.inventory, [item])

        plop.drop(item)
        self.assertListEqual(plop.inventory, [])

        plop.pick(item)
        plop.pick(item2)
        plop.pick(item3)

        plop.drop(item2)
        self.assertListEqual(plop.inventory, [item, item3])

    def testUseItem(self):
        w = Warrior("Yup", 50)
        a = Apple(1, 30)

        yup_health_before_apple_use = w.health
        #item must be in the inventory, else an Exception is raised
        with self.assertRaises(Exception):
            w.use(a)

        w.pick(a)
        w.use(a)

        #After a item was used, it must be removed from the inventory
        self.assertTrue(a not in w.inventory)

        #A apple use will add its gain to the character health
        self.assertEquals(w.health, yup_health_before_apple_use + a.gain)

        #A spell use will decrease the amount of mana of the character if > 0
        yup_mana_before_spell_use = w.mana
        s = Spell("Fire", 1, 10, 30)
        w.pick(s)
        w.use(s)

        self.assertEquals(w.mana, yup_mana_before_spell_use) # because a Warrior has no mana


        w = Wizard("Plop")
        plop_mana_before_spell_use = w.mana
        s = Spell("Fire", 1, 10, 30)
        w.pick(s)
        w.use(s)
        self.assertEquals(w.mana, plop_mana_before_spell_use - s.cost)


    def testWizardInvocation(self):
        w = Wizard("Plop")
        enemy = Warrior("Yup", 50)

        yup_health_before_apple_use = enemy.health
        plop_mana_before_spell_use = w.mana

        s = Spell("Fire", 1, 10, 30)

        with self.assertRaises(Exception):
            w.invoke(s, enemy)

        w.pick(s)
        w.invoke(s, enemy)

        self.assertTrue(s not in w.inventory)
        self.assertEquals(w.mana, plop_mana_before_spell_use - s.cost)
        self.assertEquals(enemy.health, yup_health_before_apple_use - s.damage)

if __name__ == '__main__':
    unittest.main()
