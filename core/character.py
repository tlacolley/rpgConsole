#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Chara(object):
    def __init__(self,nb_health = 20 ,name_char = 'Sans Nom',mana = 10, xp = 0 , power = 5,inventory = []  ):
        self.health = nb_health
        self.name = name_char
        self.mana = mana
        self.xp = xp
        self.power = power
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

class Wizard(Chara):
    def __init__(self,nb_health = 20 ,name_char = 'Sans Nom',mana = 20, xp = 0 , power = 5,inventory = [], spell = []):
        Chara.__init__(self, name_char)


    def use_spell(self):
        pass
        # print(self.name+ ' fait de la magie.')
        # self.magic = self.magic -1
        # print('Il rest '+str(self.magic)+' points de magie a '+self.name+'.')


class Warrior(Chara):
        def __init__(self,nb_health = 20 ,name_char = 'Sans Nom',mana = 10, xp = 0 , power = 5,inventory = [], armor = 10):
            Chara.__init__(self, name_char)
            self.armor = armor
