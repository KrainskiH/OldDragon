import random #Importando a biblioteca random para gerar números aleatórios

class EstiloClassico:
    def distribuir_atributos(self, personagem):
        print("\nRolando 3 dados de 6 lados para cada atributo na ordem aleatória...\n")
        ordem = ["Força", "Destreza", "Constituição", "Inteligência", "Sabedoria", "Carisma"]
        for atributo in ordem:
            rolagem = sum(random.randint(1, 6) for _ in range(3)) #Rolando 3 dados de 6 lados
            personagem.atributos[atributo] = rolagem

class EstiloAventureiro:
    def distribuir_atributos(self, personagem):
        print("\nRolando 3 dados de 6 lados seis vezes e distribuindo como desejar...\n")
        resultados = [sum(random.randint(1, 6) for _ in range(3)) for _ in range(6)] #Rolando 3 dados de 6 lados seis vezes
        print(f"Resultados das rolagens: {resultados}") #Exibindo os resultados das rolagens
        atributos = list(personagem.atributos.keys()) #Obtendo os atributos do personagem
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
        print("\nRolando 4 dados de 6 lados (descartando o menor) seis vezes e distribuindo como desejar...\n")
        resultados = []
        for _ in range(6):
            dados = [random.randint(1, 6) for _ in range(4)] #Rolando 4 dados de 6 lados
            dados.remove(min(dados)) #Removendo o menor dado
            resultados.append(sum(dados)) #Somando os valores dos dados restantes
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