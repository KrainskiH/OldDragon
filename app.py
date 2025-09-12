from flask import Flask
from controllers.main import personagem_bp

app = Flask(__name__)
app.secret_key = "old_dragon_secret"

app.register_blueprint(personagem_bp)   # <-- registra as rotas

if __name__ == "__main__":
    app.run(debug=True)
