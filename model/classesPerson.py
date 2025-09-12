class ClassePersonagem:
    def __init__(self, vida, pericias, proficiencias):
        self.vida = vida
        self.pericias = pericias
        self.proficiencias = proficiencias

    def to_dict(self):
        return self.__dict__

    
class Guerreiro(ClassePersonagem):
    def __init__(self):
        super().__init__(vida=10, pericias=["Atletismo", "Intimidação"], proficiencias=["Armaduras", "Armas"])

class Mago(ClassePersonagem):
    def __init__(self):
        super().__init__(vida=4, pericias=["Arcanismo", "História"], proficiencias=["Magias", "Cajados"])

class Ladino(ClassePersonagem):
    def __init__(self):
        super().__init__(vida=6, pericias=["Ataque Furtivo", "Ouvir Ruídos"], proficiencias=["Armas leves", "Ferramentas de ladrão"])