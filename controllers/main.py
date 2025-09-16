from flask import Blueprint, render_template, request, redirect, url_for, session
from model.Person import Personagem
from model.estilos import EstiloClassico, EstiloAventureiro, EstiloHeroico
import random

personagem_bp = Blueprint("personagem", __name__)

@personagem_bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nome = request.form["nome"]
        estilo_escolhido = request.form["estilo"]
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
        valores_escolhidos = []
        personagem = Personagem(session["personagem"]["nome"])
        personagem.__dict__.update(session["personagem"])
        for atributo in atributos:
            valor = int(request.form[atributo])
            valores_escolhidos.append(valor)
            personagem.atributos[atributo] = valor
        # Valida se todos os valores rolados foram usados uma vez
        if sorted(valores_escolhidos) != sorted(rolagens):
            return "Você deve usar cada valor rolado uma única vez!", 400
        session["personagem"] = personagem.__dict__
        session.pop("rolagens", None)
        return redirect(url_for("personagem.escolher_raca"))
    rolagens = session.get("rolagens", [])
    return render_template("pick_atributos.html", rolagens=rolagens)

@personagem_bp.route("/raca", methods=["GET", "POST"])
def escolher_raca():
    if request.method == "POST":
        personagem = Personagem(session["personagem"]["nome"])
        personagem.__dict__.update(session["personagem"])
        opcao = request.form["raca"]
        if opcao == "humano":
            personagem.raca = "Humano"
        elif opcao == "elfo":
            personagem.raca = "Elfo"
        else:
            personagem.raca = "Anão"

        session["personagem"] = personagem.__dict__
        personagem.__dict__.update(session["personagem"])
        return redirect(url_for("personagem.escolher_classe"))
    return render_template("pick_raca.html")

@personagem_bp.route("/classe", methods=["GET", "POST"])
def escolher_classe():
    if request.method == "POST":
        personagem = Personagem(session["personagem"]["nome"])
        personagem.__dict__.update(session["personagem"])

        opcao = request.form["classe"]
        if opcao == "guerreiro":
            personagem.classe = "Guerreiro"
        elif opcao == "mago":
            personagem.classe = "Mago"
        else:
            personagem.classe = "Ladino"

        session["personagem"] = personagem.__dict__
        personagem.__dict__.update(session["personagem"])
        return redirect(url_for("personagem.resultado"))

    return render_template("pick_classe.html")

@personagem_bp.route("/resultado")
def resultado():
    personagem = session["personagem"]  # já é dict
    return render_template("resultado.html", personagem=personagem)