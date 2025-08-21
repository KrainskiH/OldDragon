import random

class Personagem:
    def __init__ (self, nome):
        self.nome = nome
        self.atributos = {
            "FOR": 0,
            "DES": 0,
            "CON": 0,
            "INT": 0,
            "SAB": 0,
            "CAR": 0,
        }

    def exibir_atributos(self):
        print(f"\nAtributos de {self.nome}:")
        for chave, valor in self.atributos.items():
            print(f"{chave}: {valor}")

class EstiloClassico:
    def distribuir_atributos(self, personagem):
        print("\nRolando 3d6 para cada atributo na ordem clássica...")
        ordem = ["FOR", "DES", "CON", "INT", "SAB", "CAR"]
        for atributo in ordem:
            rolagem = sum(random.randint(1, 6) for _ in range(3))
            personagem.atributos[atributo] = rolagem

class EstiloAventureiro:
    def distribuir_atributos(self, personagem):
        print("\nRolando 3d6 seis vezes e distribuindo como desejar...")
        resultados = [sum(random.randint(1, 6) for _ in range(3)) for _ in range(6)]
        print(f"Resultados das rolagens: {resultados}")
        atributos = list(personagem.atributos.keys())
        for atributo in atributos:
            while True:
                try:
                    valor = int(input(f"Escolha um valor para {atributo} entre {resultados}: "))
                    if valor in resultados:
                        personagem.atributos[atributo] = valor
                        resultados.remove(valor)
                        break
                    else:
                        print("Valor inválido, escolha um dos resultados disponíveis.")
                except ValueError:
                    print("Digite um número válido.")

class EstiloHeroico:
    def distribuir_atributos(self, personagem):
        print("\nRolando 4d6 (descartando o menor) seis vezes e distribuindo como desejar...")
        resultados = []
        for _ in range(6):
            dados = [random.randint(1, 6) for _ in range(4)]
            dados.remove(min(dados))
            resultados.append(sum(dados))
        print(f"Resultados das rolagens: {resultados}")
        atributos = list(personagem.atributos.keys())
        for atributo in atributos:
            while True:
                try:
                    valor = int(input(f"Escolha um valor para {atributo} entre {resultados}: "))
                    if valor in resultados:
                        personagem.atributos[atributo] = valor
                        resultados.remove(valor)
                        break
                    else:
                        print("Valor inválido, escolha um dos resultados disponíveis.")
                except ValueError:
                    print("Digite um número válido.")

def main():
    print("Escolha abaixo qual estilo gostaria de usar:")
    print(f"1 - Estilo Clássico\n2 - Estilo Aventureiro\n3 - Estilo Heróico")
    opcao = int(input("Digite a opção desejada: "))
    nome = input("Digite o nome do personagem: ")
    personagem = Personagem(nome)
    if opcao == 1:
        print(f"Você escolheu o Estilo Clássico.")
        estilo = EstiloClassico()
    elif opcao == 2:
        print(f"Você escolheu o Estilo Aventureiro.")
        estilo = EstiloAventureiro()
    elif opcao == 3:
        print(f"Você escolheu o Estilo Heróico.")
        estilo = EstiloHeroico()
    else:
        print(f"Opção inválida. Tente novamente.")
        return main()
    estilo.distribuir_atributos(personagem)
    personagem.exibir_atributos()

if __name__ == "__main__":
    main()

