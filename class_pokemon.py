class Type():
    def __init__(self, type):
        self._type = type
    
    def test_type(self):
        ...


class Pokemon(Type()):
    def __init__(self, type, name, life, attack, speed):
        super().__init__(type)
        self._name = name 
        self._life = life
        self._attack = attack
        self._speed = speed


# class Grass(Pokemon):
#     def __init__(self, name, life, attack, speed):
#         super().__init__(name, life, attack, speed)
#         self.type = "Grass"

    
# class Fire(Pokemon):
#     def __init__(self, name, life, attack, speed):
#         super().__init__(name, life, attack, speed)
#         self.type = "Fira"


# class Watter(Pokemon):
#     def __init__(self, name, life, attack, speed):
#         super().__init__(name, life, attack, speed)
#         self.type = "Watter"
