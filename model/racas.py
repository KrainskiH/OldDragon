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
        super().__init__(movimento=9, infravisao="Nâo Possui", alinhamento="Qualquer", habilidades=["Versatilidade", "Adaptação"])

class Elfo(Raca):
    def __init__(self):
        super().__init__(movimento=9, infravisao=18, alinhamento="Neutralidade", habilidades=["Percepção Natural", "Imunidades"])

class Anao(Raca):
    def __init__(self):
        super().__init__(movimento=6, infravisao=18, alinhamento="Ordem", habilidades=["Mineradores", "Vigoroso"])