#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Item(object):
    def __init__(self, name_item = 'Sans Nom', weight = 0):
        self.name = name_item
        self.weight = weight
        # self.use =

    def use(self,chara):
        #Must be implemented in child classes
        raise

class Spell(Item):
    def __init__(self, name_item, weight, mana_cost, damage ):
        Item.__init__(self, name_item, weight )
        self.cost = mana_cost
        self.damage = damage

    def use(self,chara):
        if chara.mana > 0 :
            chara.mana = chara.mana - self.cost
        elif chara.mana == 0 :
            pass


class Apple(Item):
    def __init__(self, weight, gain ):
        Item.__init__(self, "Apple", weight)
        self.gain = gain

    def use(self,chara):
        chara.health = chara.health + self.gain
