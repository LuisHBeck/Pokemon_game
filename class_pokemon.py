from abc import ABC, abstractmethod
from random import random
import inquirer
from time import sleep

collors = {
    'X': '\33[7;32m',
    'Y': '\33[4;35m',
    'Z': '\33[7;34m',
    'N': '\33[7;31m',
    'C': '\33[m'
}

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


    # def power(poke_user, poke_pc):
    #     if poke_user.type == "Watter" and poke_pc == "Fire":
    #         poke_user.attack(2)
    #     elif poke_user.type == "Fire" and poke_pc == "Grass":
    #         poke_user.attack(2)
    #     elif poke_user.type == "Grass" and poke_pc.type == "Watter":
    #         poke_user.attack(2)
    #     else:
    #         poke_user.attack(0.5)

    #     if poke_pc.type == "Watter" and poke_user == "Fire":
    #         poke_pc.attack(2)
    #     elif poke_pc.type == "Fire" and poke_user == "Grass":
    #         poke_pc.attack(2)
    #     elif poke_pc.type == "Grass" and poke_user.type == "Watter":
    #         poke_pc.attack(2)
    #     else:
    #         poke_pc.attack(0.5)


    def attacking(poke_user, poke_pc):
        percentage = round(random(), 2)

        Water.benefits(poke_user, poke_pc)
        Fire.benefits(poke_user, poke_pc)
        Grass.benefits(poke_user, poke_pc)

        print(poke_user.attack)
        print(poke_pc.attack)
        

        if poke_user.speed > poke_pc.speed:
            print(f"{collors['X']}{poke_user.name} {collors['C']} starts attacking!")
            sleep(1)
            attack = poke_user.attack * percentage
            poke_pc.remove_life(attack)
            print(f"{collors['X']}{poke_user.name} {collors['C']} attack = {attack:.2f}")
            sleep(1)
            print(f'{collors["Z"]}{poke_pc.name}{collors["C"]} life = {poke_pc.life:.2f}')
            sleep(1)
            print()
            print(f"Now its {poke_pc.name} turn!")
            sleep(1)
            attack = poke_pc.attack * percentage
            poke_user.remove_life(attack)
            print(f'{collors["Z"]}{poke_pc.name} {collors["C"]} attack = {attack:.2f}')
            sleep(1)
            print(f"{collors['X']}{poke_user.name} {collors['C']} life = {poke_user.life:.2f}")
            sleep(1)


        else: 
            print(f'{collors["Z"]}{poke_pc.name} {collors["C"]} starts attacking!')
            sleep(1)
            attack = poke_pc.attack * percentage
            poke_user.remove_life(attack)
            print(f'{collors["Z"]}{poke_pc.name} {collors["C"]} attack = {attack:.2f}')
            sleep(1)
            print(f"{collors['X']}{poke_user.name} {collors['C']} life = {poke_user.life:.2f}")
            sleep(1)
            

        while poke_user.life > 0 or poke_pc.life > 0:
            print()
            game_resume = [
            inquirer.List('choice',
                            message="Select:",
                            choices=['Attack', 'Run']
                            ),
            ]
            answers = inquirer.prompt(game_resume)

            if answers['choice'] == 'Run':
                print(f'{collors["Z"]}{poke_pc.name} {collors["C"]} won! You ran!!')
                sleep(1)
                quit()
            else:
                percentage = round(random(), 2)
                print(f"Its {collors['X']}{poke_user.name} {collors['C']} turn")
                sleep(1)
                attack = poke_user.attack * percentage
                poke_pc.remove_life(attack)
                print(f"{collors['X']}{poke_user.name} {collors['C']} attack = {attack:.2f}")
                sleep(1)
                if poke_pc.life < 0:
                    print(f'{collors["Z"]}{poke_pc.name} {collors["C"]} died')
                    sleep(1)
                    print(f"{collors['X']}{poke_user.name} {collors['C']} won! Congrats!")
                    sleep(1)
                    quit()
                print(f'{collors["Z"]}{poke_pc.name} {collors["C"]} life = {poke_pc.life:.2f}')
                sleep(1)
                print()
                
                percentage = round(random(), 2)
                print(f'Now its {collors["Z"]}{poke_pc.name} {collors["C"]} turn!')
                sleep(1)
                attack = poke_pc.attack * percentage
                poke_user.remove_life(attack)
                print(f'{collors["Z"]}{poke_pc.name} {collors["C"]} attack = {attack:.2f}')
                sleep(1)
                if poke_user.life < 0:
                    print(f"{collors['X']}{poke_user.name} {collors['C']} died")
                    sleep(1)
                    print()
                    print(f'{collors["Z"]}{poke_pc.name} {collors["C"]} won! Congrats!')
                    sleep(1)
                    quit()
                print(f"{collors['X']}{poke_user.name} {collors['C']} life = {poke_user.life:.2f}")
                sleep(1)


class Grass(Pokemon):
    def __init__(self, name, life, attack, speed):
        super().__init__(name, life, attack, speed)
        self.type = "Grass"

    @staticmethod
    def benefits(self, poke_pc):
        if poke_pc.type == "Water":
            self.attack /= 2

    
class Fire(Pokemon):
    def __init__(self, name, life, attack, speed):
        super().__init__(name, life, attack, speed)
        self.type = "Fire"

    @staticmethod
    def benefits(self, poke_pc):
        if poke_pc.type == "Grass":
            self.attack /= 2


class Water(Pokemon):
    def __init__(self, name, life, attack, speed):
        super().__init__(name, life, attack, speed)
        self.type = "Water"

    @staticmethod
    def benefits(self, poke_pc):
        if poke_pc.type == "Fire":
            self.attack /= 2
