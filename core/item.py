#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Item(object):
    def __init__(self, name_item = 'Sans Nom', weight = 0):
        self.name = name_item
        self.weight = weight

    def use(self):
        pass

class Spell(Item):
    def __init__(self, name_item, weight, mana_cost, damage ):
        Item.__init__(self, name_item, weight )
        self.cost = mana_cost
        self.damage = damage

    def damage(self):
        pass

    # def spell(self):
    #     pass

    def cost(self):
        pass

class Apple(Item):
    def __init__(self, weight, gain ):
        Item.__init__(self, "Apple", weight)
        self.gain = gain
