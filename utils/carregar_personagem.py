import json
from model.Person import Personagem
from model.racas import Humano, Elfo, Anao
from model.classesPerson import Guerreiro, Mago, Ladino

def carregar_personagem_do_json(caminho_arquivo):

    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
        
       
        personagem = Personagem(dados["nome"])
        personagem.atributos = dados.get("atributos", {})
        
       
        if dados.get("raca"):
            tipo_raca = dados["raca"]["tipo"]
            if tipo_raca == "Humano":
                personagem.raca = Humano()
            elif tipo_raca == "Elfo":
                personagem.raca = Elfo()
            elif tipo_raca == "Anao":
                personagem.raca = Anao()
        
        # Reconstrói a classe
        if dados.get("classe"):
            tipo_classe = dados["classe"]["tipo"]
            if tipo_classe == "Guerreiro":
                personagem.classe = Guerreiro()
            elif tipo_classe == "Mago":
                personagem.classe = Mago()
            elif tipo_classe == "Ladino":
                personagem.classe = Ladino()
        
        return personagem
        
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {caminho_arquivo}")
        return None
    except json.JSONDecodeError:
        print(f"Erro ao decodificar JSON: {caminho_arquivo}")
        return None
    except Exception as e:
        print(f"Erro ao carregar personagem: {e}")
        return None

# Exemplo de uso
if __name__ == "__main__":
    # Exemplo de como carregar um personagem
    personagem = carregar_personagem_do_json("saves/exemplo_personagem.json")
    if personagem:
        print("Personagem carregado com sucesso!")
        personagem.exibir_atributos()
    else:
        print("Erro ao carregar personagem.")