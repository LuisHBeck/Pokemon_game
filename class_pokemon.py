from abc import ABC, abstractmethod
from random import random

class Pokemon():
    def __init__(self, name, life, attack, speed):
        self._name = name 
        self._life = life
        self._attack = attack
        self._speed = speed


    @property
    def name(self):
        return self._name
    

    @property
    def life(self):
        return self._life
    

    @property
    def attack(self):
        return self._attack
    

    @property
    def speed(self):
        return self._speed
    

    def remove_life(self, value):
        self._life -= value
    

    @attack.setter
    def attack(self, multiplicator):
        return self._life * multiplicator


    @abstractmethod
    def benefits(self):
        pass


    def power(poke_user, poke_pc):
        if poke_user.type == "Watter" and poke_pc == "Fire":
            poke_user.attack(2)
        elif poke_user.type == "Fire" and poke_pc == "Grass":
            poke_user.attack(2)
        elif poke_user.type == "Grass" and poke_pc.type == "Watter":
            poke_user.attack(2)
        else:
            poke_user.attack(0.5)

        if poke_pc.type == "Watter" and poke_user == "Fire":
            poke_pc.attack(2)
        elif poke_pc.type == "Fire" and poke_user == "Grass":
            poke_pc.attack(2)
        elif poke_pc.type == "Grass" and poke_user.type == "Watter":
            poke_pc.attack(2)
        else:
            poke_pc.attack(0.5)


    def attacking(poke_user, poke_pc):
        percentage = round(random(), 2)

        if poke_user.speed > poke_pc.speed:
            print(f"{poke_user.name} starts attacking!")
            attack = poke_user.attack * percentage
            poke_pc.remove_life(attack)
            print(f'{poke_user.name} attack = {attack:.2f}')
            print(f'{poke_pc.name} life = {poke_pc.life:.2f}')
        else: 
            print(f"{poke_pc.name} starts attacking!")
            attack = poke_pc.attack * percentage
            poke_user.remove_life(attack)
            print(f'{poke_pc.name} attack = {attack:.2f}')
            print(f'{poke_user.name} life = {poke_user.life:.2f}')

        # while 
            



class Grass(Pokemon):
    def __init__(self, name, life, attack, speed):
        super().__init__(name, life, attack, speed)
        self.type = "Grass"

    def benefits(self, poke_pc):
        if poke_pc == "pce":
            self._attack /= 2

    
class Fire(Pokemon):
    def __init__(self, name, life, attack, speed):
        super().__init__(name, life, attack, speed)
        self.type = "Fire"

    def benefits(self, poke_pc):
        if poke_pc == "pcter":
            self._attack /= 2


class Water(Pokemon):
    def __init__(self, name, life, attack, speed):
        super().__init__(name, life, attack, speed)
        self.type = "Water"

    def benefits(self, poke_pc):
        if poke_pc == "Grass":
            self._attack /= 2
