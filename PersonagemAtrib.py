import random #Importando a biblioteca random para gerar números aleatórios

class Personagem:
    def __init__ (self, nome): # Método construtor da classe Personagem
        """Inicializa o personagem com um nome e atributos padrão."""
        self.nome = nome
        self.atributos = {
            "Força": 0,
            "Destreza": 0,
            "Constituição": 0,
            "Inteligência": 0,
            "Sabedoria": 0,
            "Carisma": 0,
        }

    def exibir_atributos(self):
        print(f"\nOs atributos {self.nome}:")
        for chave, valor in self.atributos.items():
            print(f"{chave}: {valor}")

class EstiloClassico:
    def distribuir_atributos(self, personagem):
        print("\nRolando 3 dados de 6 lados para cada atributo na ordem clássica...")
        ordem = ["Força", "Destreza", "Constituição", "Inteligência", "Sabedoria", "Carisma"]
        for atributo in ordem:
            rolagem = sum(random.randint(1, 6) for _ in range(3))
            personagem.atributos[atributo] = rolagem

class EstiloAventureiro:
    def distribuir_atributos(self, personagem):
        print("\nRolando 3 dados de 6 lados seis vezes e distribuindo como desejar...")
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
        print("\nRolando 4 dados de 6 lados (descartando o menor) seis vezes e distribuindo como desejar...")
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
    print(f"\nBem-Vindo à OldDragon. Vamos começar com a sua escolha de estilo de jogo, Caro Aventureiro!\nEscolha abaixo qual estilo gostaria de usar:")
    print(f"1 - Estilo Clássico (Este estilo também é conhecido por fazer a escolha aleatória das classes, já que você praticamente escolhe com qual classe vai jogar após determinar os atributos do seu personagem)\n2 - Estilo Aventureiro (Esse estilo de rolagem é idêntico ao estilo clássico, mas um pouco mais maleável porque você distribui dentre os atributos desejados.)\n3 - Estilo Heróico (O estilo heroico gerará personagens levemente superiores aos do estilo aventureiro. Você rolará 4 dados de 6 lados e descartará o menor resultado, distribuindo os valores como desejar.)\n")

    opcao = int(input("Digite o número para escolha do estilo desejado: "))
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

if __name__ == "__main__": # Ponto de entrada do programa
    main() # Chama a função main para iniciar o programa
    print("\nObrigado por jogar OldDragon! Boa sorte em suas aventuras!")

