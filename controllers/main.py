from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify, flash
from model.Person import Personagem
from model.estilos import EstiloClassico, EstiloAventureiro, EstiloHeroico
from model.racas import Humano, Elfo, Anao
from model.classesPerson import Guerreiro, Mago, Ladino
import random
import json
import os

personagem_bp = Blueprint("personagem", __name__)

@personagem_bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        estilo_escolhido = request.form.get("estilo")
        
        # Validações de entrada
        if not nome:
            flash("Por favor, digite um nome para o personagem!", "error")
            return render_template("index.html")
            
        if len(nome) > 50:
            flash("Nome muito longo! Máximo 50 caracteres.", "error")
            return render_template("index.html")
            
        if not estilo_escolhido or estilo_escolhido not in ["classico", "aventureiro", "heroico"]:
            flash("Por favor, selecione um estilo válido!", "error")
            return render_template("index.html")
        
        # Limpar sessão anterior
        session.clear()
        
        personagem = Personagem(nome)
        session["personagem"] = personagem.__dict__
        session["estilo_escolhido"] = estilo_escolhido

        if estilo_escolhido == "classico":
            estilo = EstiloClassico()
            estilo.distribuir_atributos(personagem)
            session["personagem"] = personagem.__dict__
            return redirect(url_for("personagem.escolher_raca"))
        elif estilo_escolhido == "aventureiro":
            # Gera 6 valores de 3d6
            resultados = [sum(random.randint(1, 6) for _ in range(3)) for _ in range(6)]
            session["rolagens"] = resultados
            return redirect(url_for("personagem.escolher_atributos"))
        elif estilo_escolhido == "heroico":
            # Gera 6 valores de 4d6 descartando o menor
            resultados = []
            for _ in range(6):
                dados = [random.randint(1, 6) for _ in range(4)]
                dados.remove(min(dados))
                resultados.append(sum(dados))
            session["rolagens"] = resultados
            return redirect(url_for("personagem.escolher_atributos"))
            
    return render_template("index.html")

@personagem_bp.route("/atributos", methods=["GET", "POST"])
def escolher_atributos():
    atributos = ["Força", "Destreza", "Constituição", "Inteligência", "Sabedoria", "Carisma"]
    if request.method == "POST":
        rolagens = session.get("rolagens", [])
        if not rolagens:
            flash("Erro: valores de atributos não encontrados!", "error")
            return redirect(url_for("personagem.index"))
            
        valores_escolhidos = []
        personagem = Personagem(session["personagem"]["nome"])
        personagem.__dict__.update(session["personagem"])
        
        try:
            for atributo in atributos:
                valor_str = request.form.get(atributo)
                if not valor_str:
                    flash(f"Por favor, selecione um valor para {atributo}!", "error")
                    return render_template("pick_atributos.html", rolagens=rolagens)
                    
                valor = int(valor_str)
                if valor not in rolagens:
                    flash(f"Valor {valor} não está disponível para distribuição!", "error")
                    return render_template("pick_atributos.html", rolagens=rolagens)
                    
                valores_escolhidos.append(valor)
                personagem.atributos[atributo] = valor
                
        except ValueError:
            flash("Erro: valores de atributos inválidos!", "error")
            return render_template("pick_atributos.html", rolagens=rolagens)
            
        # Valida se todos os valores rolados foram usados uma vez
        if sorted(valores_escolhidos) != sorted(rolagens):
            flash("Você deve usar cada valor rolado uma única vez!", "error")
            return render_template("pick_atributos.html", rolagens=rolagens)
            
        session["personagem"] = personagem.__dict__
        session.pop("rolagens", None)
        return redirect(url_for("personagem.escolher_raca"))
        
    rolagens = session.get("rolagens", [])
    if not rolagens:
        flash("Erro: você precisa escolher um estilo primeiro!", "error")
        return redirect(url_for("personagem.index"))
        
    return render_template("pick_atributos.html", rolagens=rolagens)

@personagem_bp.route("/raca", methods=["GET", "POST"])
def escolher_raca():
    if request.method == "POST":
        personagem = Personagem(session["personagem"]["nome"])
        personagem.__dict__.update(session["personagem"])
        opcao = request.form.get("raca")
        
        # Validação da entrada
        if not opcao or opcao not in ["humano", "elfo", "anao"]:
            flash("Por favor, selecione uma raça válida!", "error")
            return render_template("pick_raca.html")
            
        # Criar objeto da raça ao invés de string
        if opcao == "humano":
            personagem.raca = Humano()
        elif opcao == "elfo":
            personagem.raca = Elfo()
        else:
            personagem.raca = Anao()

        # Salvar como string na sessão para compatibilidade
        personagem_dict = personagem.__dict__.copy()
        personagem_dict["raca"] = type(personagem.raca).__name__
        session["personagem"] = personagem_dict
        return redirect(url_for("personagem.escolher_classe"))
    
    # Buscar informações das raças para exibir
    racas_info = {
        "Humano": Humano(),
        "Elfo": Elfo(),
        "Anão": Anao()
    }
    return render_template("pick_raca.html", racas_info=racas_info)

@personagem_bp.route("/classe", methods=["GET", "POST"])
def escolher_classe():
    if request.method == "POST":
        personagem = Personagem(session["personagem"]["nome"])
        personagem.__dict__.update(session["personagem"])

        opcao = request.form.get("classe")
        
        # Validação da entrada
        if not opcao or opcao not in ["guerreiro", "mago", "ladino"]:
            flash("Por favor, selecione uma classe válida!", "error")
            return render_template("pick_classe.html")
            
        # Criar objeto da classe ao invés de string
        if opcao == "guerreiro":
            personagem.classe = Guerreiro()
        elif opcao == "mago":
            personagem.classe = Mago()
        else:
            personagem.classe = Ladino()

        # Salvar como string na sessão para compatibilidade
        personagem_dict = personagem.__dict__.copy()
        personagem_dict["classe"] = type(personagem.classe).__name__
        session["personagem"] = personagem_dict
        return redirect(url_for("personagem.resultado"))

    # Buscar informações das classes para exibir
    classes_info = {
        "Guerreiro": Guerreiro(),
        "Mago": Mago(),
        "Ladino": Ladino()
    }
    return render_template("pick_classe.html", classes_info=classes_info)

@personagem_bp.route("/resultado")
def resultado():
    personagem = session.get("personagem")
    if not personagem:
        flash("Nenhum personagem encontrado! Crie um novo personagem.", "error")
        return redirect(url_for("personagem.index"))
    return render_template("resultado.html", personagem=personagem)

@personagem_bp.route("/carregar_personagens", endpoint='listar_personagens_salvos')
def listar_personagens_salvos():
    """Lista todos os personagens salvos em JSON"""
    saves_dir = "saves"
    personagens = []
    
    if os.path.exists(saves_dir):
        for arquivo in os.listdir(saves_dir):
            if arquivo.endswith('_personagem.json'):
                caminho = os.path.join(saves_dir, arquivo)
                try:
                    with open(caminho, 'r', encoding='utf-8') as f:
                        dados = json.load(f)
                    personagens.append({
                        'arquivo': arquivo,
                        'nome': dados.get('nome', 'Desconhecido'),
                        'raca': dados.get('raca', {}).get('tipo', 'Desconhecida'),
                        'classe': dados.get('classe', {}).get('tipo', 'Desconhecida'),
                        'caminho': caminho
                    })
                except Exception as e:
                    print(f"Erro ao ler {arquivo}: {e}")
    
    return render_template("personagens_salvos.html", personagens=personagens)

@personagem_bp.route("/salvar_json", methods=["POST"], endpoint='salvar_personagem_json')
def salvar_personagem_json():
    try:
        # Recupera os dados do personagem da sessão
        personagem_data = session.get("personagem")
        if not personagem_data:
            flash("Nenhum personagem encontrado para salvar!", "error")
            return redirect(url_for("personagem.resultado"))
        
        # Reconstrói o objeto Personagem completo
        personagem = Personagem(personagem_data["nome"])
        personagem.atributos = personagem_data.get("atributos", {})
        
        # Reconstrói a raça como objeto
        if personagem_data.get("raca"):
            raca_nome = personagem_data["raca"]
            if raca_nome == "Humano":
                personagem.raca = Humano()
            elif raca_nome == "Elfo":
                personagem.raca = Elfo()
            elif raca_nome == "Anão":
                personagem.raca = Anao()
        
        # Reconstrói a classe como objeto
        if personagem_data.get("classe"):
            classe_nome = personagem_data["classe"]
            if classe_nome == "Guerreiro":
                personagem.classe = Guerreiro()
            elif classe_nome == "Mago":
                personagem.classe = Mago()
            elif classe_nome == "Ladino":
                personagem.classe = Ladino()
        
        # Converte o objeto para dicionário usando __dict__
        personagem_dict = personagem.__dict__.copy()
        if personagem.raca:
            personagem_dict["raca"] = personagem.raca.__dict__.copy()
            personagem_dict["raca"]["tipo"] = type(personagem.raca).__name__
        if personagem.classe:
            personagem_dict["classe"] = personagem.classe.__dict__.copy()
            personagem_dict["classe"]["tipo"] = type(personagem.classe).__name__
        
        # Cria o diretório saves se não existir
        saves_dir = "saves"
        if not os.path.exists(saves_dir):
            os.makedirs(saves_dir)
        
        # Define o nome do arquivo
        nome_arquivo = f"{personagem.nome.replace(' ', '_')}_personagem.json"
        caminho_arquivo = os.path.join(saves_dir, nome_arquivo)
        
        # Salva o arquivo JSON
        with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
            json.dump(personagem_dict, arquivo, indent=4, ensure_ascii=False)
        
        flash(f"Personagem salvo com sucesso em: {caminho_arquivo}", "success")
        return redirect(url_for("personagem.resultado"))
        
    except Exception as e:
        flash(f"Erro ao salvar personagem: {str(e)}", "error")
        return redirect(url_for("personagem.resultado"))