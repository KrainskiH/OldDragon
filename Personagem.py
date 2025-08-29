from atributos import interpretar_atributo

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