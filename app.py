from flask import Flask
import os
from controllers.main import personagem_bp 

app = Flask(__name__)
app.secret_key = os.urandom(24)  
app.register_blueprint(personagem_bp)  

if __name__ == "__main__":
    app.run(debug=True)
