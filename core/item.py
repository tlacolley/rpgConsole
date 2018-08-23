#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Item(object):
    def __init__(self, name_char = 'Sans Nom', weight = 0):
        self.name = name_char
        self.weight = weight

    def use(self):
        pass

class Spell(Item):
    def __init__(self, name_char = 'Sans Nom', mana_cost = 0, damages = 0):
        Item.__init__(self, name_char)
        self.cost = mana_cost
        self.damages = damages

    def damage(self):
        pass

    # def spell(self):
    #     pass

    def cost(self):
        pass

class Apple(Item):
    def __init__(self, name_char = 'Sans Nom', nb_health = 10):
        Item.__init__(self, name_char)
