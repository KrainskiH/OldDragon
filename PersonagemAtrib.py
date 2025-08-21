import random #Importando a biblioteca random para gerar números aleatórios

def interpretar_atributo(nome, valor):
    tabelas = {
        "Força": [
            (3, 8, "Fraco: você é franzino e tem dificuldade para tarefas físicas."),
            (9, 12, "Mediano: realiza tarefas comuns sem problemas, mas não se destaca."),
            (13, 16, "Forte: claramente forte, requisitado para trabalhos braçais."),
            (17, 18, "Muito Forte: um colosso, faz o impossível para pessoas comuns."),
        ],
        "Destreza": [
            (3, 8, "Letárgico: movimentos lentos e desajeitados."),
            (9, 12, "Mediano: coordenação aceitável, realiza tarefas simples."),
            (13, 16, "Ágil: movimentos graciosos e precisos."),
            (17, 18, "Preciso: movimentos fluidos, quase mágicos."),
        ],
        "Constituição": [
            (3, 8, "Frágil: aparência debilitada, saúde fraca."),
            (9, 12, "Mediano: saudável, tolera esforços e doenças leves."),
            (13, 16, "Resistente: aguenta impactos e esforços acima da média."),
            (17, 18, "Vigoroso: quase imune a doenças e fadiga."),
        ],
        "Inteligência": [
            (3, 8, "Inepto: dificuldade para aprender e memorizar."),
            (9, 12, "Mediano: aprende normalmente, memória razoável."),
            (13, 16, "Inteligente: aprende rápido, memória invejável."),
            (17, 18, "Gênio: raciocínio brilhante, memória quase perfeita."),
        ],
        "Sabedoria": [
            (3, 8, "Tolo: age por impulso, distraído e desatento."),
            (9, 12, "Mediano: bom senso e intuição normais."),
            (13, 16, "Intuitivo: percebe nuances e dá bons conselhos."),
            (17, 18, "Presciente: intuição certeira, quase sobrenatural."),
        ],
        "Carisma": [
            (3, 8, "Descortês: dificuldade de empatia, presença desconfortável."),
            (9, 12, "Mediano: sociável, educado e amigável."),
            (13, 16, "Influente: popular, sabe convencer e liderar."),
            (17, 18, "Ídolo: presença marcante, influência extrema."),
        ],
    }
    for minimo, maximo, descricao in tabelas[nome]: #Percorre a tabela de atributos para encontrar o intervalo correspondente
        if minimo <= valor <= maximo: #Verifica se o valor do atributo está dentro do intervalo definido
            return descricao #Retorna a descrição correspondente ao valor do atributo
    return "Valor fora da escala." #Se o valor não estiver dentro de nenhum intervalo, retorna uma mensagem padrão

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

    def exibir_atributos(self):
        print("\n==--=== Atributos do Personagem ==--==")
        print(f"\nOlá {self.nome}, segue abaixo seu descritivo:")
        for chave, valor in self.atributos.items(): #Percorre o dicionário de atributos do personagem
            print(f"{chave}: {valor} - {interpretar_atributo(chave, valor)}") # Exibe o nome do atributo, seu valor e a interpretação correspondente
        print("\n==--=== Fim dos Atributos ==--==\n")

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
        atributos = list(personagem.atributos.keys()) # Obtendo os atributos do personagem
        for atributo in atributos: #
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

def main():
    print(f"\nBem-Vindo à OldDragon. Vamos começar com a sua escolha de estilo de jogo, Caro Aventureiro!\nEscolha abaixo qual estilo gostaria de usar:")
    print("1 - Estilo Clássico (Este estilo também é conhecido por fazer a escolha aleatória das classes e atributos)\n"
          "2 - Estilo Aventureiro (Esse estilo é um pouco mais maleável, porque você distribui dentre os atributos desejados.)\n"
          "3 - Estilo Heróico (O estilo heróico gerará personagens levemente superiores aos do estilo aventureiro.)\n")

    opcao = int(input("Digite o número para escolha do estilo desejado: "))
    nome = input("Digite o nome do personagem: ")
    personagem = Personagem(nome)
    if opcao == 1:
        print(f"\nVocê escolheu o Estilo Clássico.")
        estilo = EstiloClassico()
    elif opcao == 2:
        print(f"\nVocê escolheu o Estilo Aventureiro.")
        estilo = EstiloAventureiro()
    elif opcao == 3:
        print(f"\nVocê escolheu o Estilo Heróico.")
        estilo = EstiloHeroico()
    else:
        print(f"\nOpção inválida. Tente novamente.")
        return main()
    estilo.distribuir_atributos(personagem)
    personagem.exibir_atributos()

if __name__ == "__main__": # Ponto de entrada do programa
    main() # Chama a função main para iniciar o programa
    print("\nObrigado por jogar OldDragon! Boa sorte em suas aventuras!")

