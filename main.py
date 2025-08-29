from Personagem import Personagem
from estilos import EstiloClassico, EstiloAventureiro, EstiloHeroico
from racas import Humano, Elfo, Anao
from classesPerson import Guerreiro, Mago, Ladino 

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

     # Escolha de Raça
    print("\nEscolha a raça do personagem:")
    print("1 - Humano\n2 - Elfo\n3 - Anão")
    opcao_raca = int(input("Digite sua escolha: "))
    if   opcao_raca == 1: personagem.raca = Humano()
    elif opcao_raca == 2: personagem.raca = Elfo()
    elif opcao_raca == 3: personagem.raca = Anao()

    # Escolha de Classe
    print("\nEscolha a classe do personagem:")
    print("1 - Guerreiro\n2 - Mago\n3 - Ladino")
    opcao_classe = int(input("Digite sua escolha: "))
    if   opcao_classe == 1: personagem.classe = Guerreiro()
    elif opcao_classe == 2: personagem.classe = Mago()
    elif opcao_classe == 3: personagem.classe = Ladino()

    personagem.exibir_atributos()


if __name__ == "__main__": # Ponto de entrada do programa
    main() # Chama a função main para iniciar o programa
    print("\nObrigado por jogar OldDragon! Boa sorte em suas aventuras!")