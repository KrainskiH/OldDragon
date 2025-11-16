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

    def to_dict(self):
        result = super().to_dict()
        result["tipo"] = "Guerreiro"
        return result

    @staticmethod
    def from_dict(data):
        return Guerreiro()

class Mago(ClassePersonagem):
    def __init__(self):
        super().__init__(vida=4, pericias=["Arcanismo", "História"], proficiencias=["Magias", "Cajados"])

    def to_dict(self):
        result = super().to_dict()
        result["tipo"] = "Mago"
        return result
        
    @staticmethod
    def from_dict(data):
        return Mago()

class Ladino(ClassePersonagem):
    def __init__(self):
        super().__init__(vida=6, pericias=["Ataque Furtivo", "Ouvir Ruídos"], proficiencias=["Armas leves", "Ferramentas de ladrão"])

    def to_dict(self):
        result = super().to_dict()
        result["tipo"] = "Ladino"
        return result
        
    @staticmethod
    def from_dict(data):
        return Ladino()