class Raca:
    def __init__(self, movimento, infravisao, alinhamento, habilidades):
        self.movimento = movimento
        self.infravisao = infravisao
        self.alinhamento = alinhamento
        self.habilidades = habilidades

    def to_dict(self):
        return self.__dict__
class Humano(Raca):
    def __init__(self):
        super().__init__(movimento=9, infravisao="Não Possui", alinhamento="Qualquer", habilidades=["Versatilidade", "Adaptação"])

    def to_dict(self):
        result = super().to_dict()
        result["tipo"] = "Humano"
        return result

    @staticmethod
    def from_dict(data):
        return Humano()

class Elfo(Raca):
    def __init__(self):
        super().__init__(movimento=9, infravisao=18, alinhamento="Neutralidade", habilidades=["Percepção Natural", "Imunidades"])

    def to_dict(self):
        result = super().to_dict()
        result["tipo"] = "Elfo"
        return result
        
    @staticmethod
    def from_dict(data):
        return Elfo()

class Anao(Raca):
    def __init__(self):
        super().__init__(movimento=6, infravisao=18, alinhamento="Ordem", habilidades=["Mineradores", "Vigoroso"])

    def to_dict(self):
        result = super().to_dict()
        result["tipo"] = "Anão"
        return result

    @staticmethod
    def from_dict(data):
        return Anao()