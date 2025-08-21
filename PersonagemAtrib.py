print(f"Escolha a a baixo qual Estilo gostaria de usar: ")
print(f"1 - Estilo Clássico, 2 - Estilo Aventureiro, 3 - Estilo Heróico")

opcao= int(input("Digite a opção desejada: "))
if opcao == 1:
    print("Você escolheu o Estilo Clássico.")
    
class Personagem:
    def Atributos(self, FOR, DES, CON, INT, SAB, CAR):
        self.FOR = FOR
        self.DES = DES
        self.CON = CON
        self.INT = INT
        self.SAB = SAB
        self.CAR = CAR

        
    