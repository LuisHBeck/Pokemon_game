from pokemons import pokemons
from time import sleep
from class_pokemon import Pokemon
from random import choice
import inquirer

collors = {
    'X': '\33[32m',
    'Y': '\33[4;35m',
    'Z': '\33[31m',
    'N': '\33[7;31m',
    'C': '\33[m'
}

def select_poke():
    pokemon = [
                inquirer.List('choice',
                                message="Select:",
                                choices=[pokemons[0].name, pokemons[1].name, pokemons[2].name]
                                ),
                ]
    user_choice = inquirer.prompt(pokemon)
    
    if user_choice['choice'] == "Blastoise":
        return pokemons[0]
    elif user_choice['choice'] == "Charizard":
        return pokemons[1]
    elif user_choice['choice'] == "Venusaur":
        return pokemons[2]


def play():
    print(f"{collors['N']}Welcome to Pokemon Game{collors['C']}")    
    print()
    poke_user = select_poke()
    sleep(2)
    print("You choose your Pokemon, now it's pc's turn")
    poke_pc = choice(pokemons)
    sleep(3)
    print()
    print("Both chose, now it's battle time")
    print(f'''
    {collors['X']}Your pokemon traits:{collors['C']} 
    Name = {poke_user.name}
    Life = {poke_user.life}
    Attack = {poke_user.attack}
    Speed = {poke_user.speed}''')
    print()
    print(f'''
    {collors['Z']}Pc's pokemon traits:{collors['C']}
    Name = {poke_pc.name}
    Life = {poke_pc.life}
    Attack = {poke_pc.attack}
    Speed = {poke_pc.speed}''')
    sleep(2)
    print()

    Pokemon.attacking(poke_user, poke_pc)