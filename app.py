from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# instancia a aplicação
app = Flask(__name__)

# define as configurações do banco de dados
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ecommerce.db"
db = SQLAlchemy(app)

# cria a tabela produto
class Product(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(120), nullable=False)
  price = db.Column(db.Float, nullable=False)
  description = db.Column(db.Text, nullable=True)

# define uma rota raiz
@app.route("/")
def helloWorld():
  return "Hello World"

# executa a aplicação
if __name__ == "__main__":
  app.run(debug=True)
