from model.atributos import interpretar_atributo

class Personagem:
    def __init__ (self, nome): #Método construtor da classe Personagem

        self.nome = nome
        self.atributos = {
            "Força": 0,
            "Destreza": 0,
            "Constituição": 0,
            "Inteligência": 0,
            "Sabedoria": 0,
            "Carisma": 0,
        }
        self.raca = None
        self.classe = None

    def to_dict(self):
        return {
            "nome": self.nome,
            "atributos": self.atributos,
            "raca": self.raca.to_dict() if self.raca else None,
            "classe": self.classe.to_dict() if self.classe else None
        }

    @staticmethod
    def from_dict(data):
        p = Personagem(data["nome"])
        p.atributos = data["atributos"]

        # reconstrói raça
        if data["raca"]:
            if data["raca"]["tipo"] == "Humano":
                from model.racas import Humano
                p.raca = Humano.from_dict(data["raca"])
            elif data["raca"]["tipo"] == "Elfo":
                from model.racas import Elfo
                p.raca = Elfo.from_dict(data["raca"])
            elif data["raca"]["tipo"] == "Anão":
                from model.racas import Anao
                p.raca = Anao.from_dict(data["raca"])

        # reconstrói classe
        if data["classe"]:
            if data["classe"]["tipo"] == "Guerreiro":
                from model.classesPerson import Guerreiro
                p.classe = Guerreiro.from_dict(data["classe"])
            elif data["classe"]["tipo"] == "Mago":
                from model.classesPerson import Mago
                p.classe = Mago.from_dict(data["classe"])
            elif data["classe"]["tipo"] == "Ladino":
                from model.classesPerson import Ladino
                p.classe = Ladino.from_dict(data["classe"])

        return p
    def exibir_atributos(self):
        print("\n==--=== Atributos do Personagem ==--==")
        print(f"\nOlá {self.nome}, segue abaixo seu descritivo:")
        for chave, valor in self.atributos.items(): #Percorre o dicionário de atributos do personagem
            print(f"{chave}: {valor} - {interpretar_atributo(chave, valor)}") # Exibe o nome do atributo, seu valor e a interpretação correspondente

        if self.raca:
           print(f"\nRaça: {type(self.raca).__name__}")
           print(f"Movimento: {self.raca.movimento}")
           print(f"Infravisão: {self.raca.infravisao}")
           print(f"Alinhamento: {self.raca.alinhamento}")
           print(f"Habilidades raciais: {', '.join(self.raca.habilidades)}")

        if self.classe:
            print(f"\nClasse: {type(self.classe).__name__}")
            print(f"Vida inicial: {self.classe.vida}")
            print(f"Perícias: {', '.join(self.classe.pericias)}")
            print(f"Proficiencias: {', '.join(self.classe.proficiencias)}")

        print("\n==--=== Fim dos Atributos ==--==\n")