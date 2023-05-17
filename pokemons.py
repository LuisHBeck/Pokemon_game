from class_pokemon import Fire, Grass, Water, Pokemon
from random import choice

blastoise = Water("Blastoise", 79, 57, 78)
charizard = Fire("Charizard", 78, 53, 100)
venusaur = Grass("Venusaur", 78, 76, 80)

pokemons = [blastoise, charizard, venusaur]

Pokemon.attacking(charizard, blastoise)