from flask import Flask, request, jsonify
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

# rota para criar um produto
@app.route("/products/add", methods=["POST"])
def addProduct():
  data = request.json

  if "name" in data and "price" in data:
    product = Product(
      name=data["name"],
      price=data["price"],
      description=data.get("description", "")
    )

    db.session.add(product)
    db.session.commit()

    return jsonify({"message": "Product added successfully"}), 201
  return jsonify({ "message": "Invalid product data" }), 422

# define uma rota raiz
@app.route("/")
def helloWorld():
  return "Hello World"

# executa a aplicação
if __name__ == "__main__":
  app.run(debug=True)
