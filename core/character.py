#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Character(object):
    def __init__(self, name_char = 'Sans Nom', health = 20, mana = 10,  power = 5, xp = 0, inventory = []  ):
        self.name = name_char
        self.health = health
        self.mana = mana
        self.power = power
        self.xp = xp
        self.inventory = inventory

    # def display_chara(self):
    #     print('Il reste '+str(self.health)+' points de vie a '+self.name)
    #
    # def death(self):
    #     self.display_chara()
    #     print(self.name+ ' succombe suite a ces blessure. Sniff')
    #
    # def dammage(self):
    #     print(self.name+'   subit une attaque, il perd une vie.')
    #     self.health = self.health -1
    #
    #     if self.health == 0 :
    #         self.Death()

    def move(self):
        pass

    def attack(self):
        pass
        # print(self.name+' lance une attaque basique.')

    def pick(self):
        pass

    def throw(self):
        pass

    def use(self):
        pass


class Wizard(Character):
    def __init__(self, name_char):
        Character.__init__(self, name_char, 100, 100, 50, 0, [])
        self.spells = []
    def use_spells(self):
        pass
        # print(self.name+ ' fait de la magie.')
        # self.magic = self.magic -1
        # print('Il rest '+str(self.magic)+' points de magie a '+self.name+'.')


class Warrior(Character):
        def __init__(self, name_char, armor):
            Character.__init__(self, name_char, 200, 0, 300, 0, [])
            self.armor = armor
