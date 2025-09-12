from flask import Blueprint, render_template, request, redirect, url_for, session 
from model.Person import Personagem
from model.estilos import EstiloClassico, EstiloAventureiro, EstiloHeroico
from model.racas import Humano, Elfo, Anao
from model.classesPerson import Guerreiro, Mago, Ladino 

personagem_bp = Blueprint("personagem", __name__)

@personagem_bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nome = request.form["nome"]
        estilo_escolhido = request.form["estilo"]

        personagem = Personagem(nome)

        if estilo_escolhido == "classico":
            estilo = EstiloClassico()
        elif estilo_escolhido == "aventureiro":
            estilo = EstiloAventureiro()
        else:
            estilo = EstiloHeroico()

        estilo.distribuir_atributos(personagem)

        # salva personagem temporariamente na sessão
        session["personagem"] = personagem.__dict__
        return redirect(url_for("personagem.escolher_raca"))

    return render_template("index.html")


@personagem_bp.route("/raca", methods=["GET", "POST"])
def escolher_raca():
    if request.method == "POST":
        personagem = Personagem(session["personagem"]["nome"])
        personagem.__dict__.update(session["personagem"])

        opcao = request.form["raca"]
        if opcao == "humano":
            personagem.raca = Humano()
        elif opcao == "elfo":
            personagem.raca = Elfo()
        else:
            personagem.raca = Anao()

        session["personagem"] = personagem.__dict__
        return redirect(url_for("personagem.escolher_classe"))

    return render_template("pick_raca.html")


@personagem_bp.route("/classe", methods=["GET", "POST"])
def escolher_classe():
    if request.method == "POST":
        personagem = Personagem(session["personagem"]["nome"])
        personagem.__dict__.update(session["personagem"])

        opcao = request.form["classe"]
        if opcao == "guerreiro":
            personagem.classe = Guerreiro()
        elif opcao == "mago":
            personagem.classe = Mago()
        else:
            personagem.classe = Ladino()

        session["personagem"] = personagem.__dict__
        return redirect(url_for("personagem.resultado"))

    return render_template("pick_classe.html")


@personagem_bp.route("/resultado")
def resultado():
    personagem = session["personagem"]
    return render_template("resultado.html", personagem=personagem)