from flask import Flask
import os
from controllers.main import personagem_bp  # importa o blueprint

app = Flask(__name__)
app.secret_key = os.urandom(24)  # gera uma chave secreta aleatória
app.register_blueprint(personagem_bp)   # <-- registra as rotas

if __name__ == "__main__":
    app.run(debug=True)
