from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

# instancia a aplicação
app = Flask(__name__)

# define as configurações do banco de dados
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ecommerce.db"
db = SQLAlchemy(app)

# instancia o cors
CORS(app)

# cria a tabela produto
class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  userName = db.Column(db.String(80), nullable=False, unique=True)
  password = db.Column(db.String(80), nullable=False)

# cria a tabela produto
class Product(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(120), nullable=False)
  price = db.Column(db.Float, nullable=False)
  description = db.Column(db.Text, nullable=True)

# rota para criar o login do usuário
@app.route("/login", methods=["POST"])
def login():
  data = request.json

  user = User.query.filter_by(userName=data.get("userName")).first()

  if user and data.get("password") == user.password:
      return jsonify({ "message": "Logged in successfully" }), 200

  return jsonify({ "message": "Unauthorized, invalid credentials" }), 401

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

    return jsonify({ "message": "Product added successfully" }), 201

  return jsonify({ "message": "Invalid product data" }), 422

# rota para buscar todos os produtos
@app.route("/products", methods=["GET"])
def getProducts():
  products = Product.query.all()

  productList = []

  for product in products:
    productList.append({
      "id": product.id,
      "name": product.name,
      "price": product.price,
      "description": product.description,
    })

  return jsonify(productList), 200

# rota para buscar um produto
@app.route("/products/<int:id>", methods=["GET"])
def getProduct(id):
  product = Product.query.get(id)

  if product:
    return jsonify({
      "id": product.id,
      "name": product.name,
      "price": product.price,
      "description": product.description,
    }), 200

  return jsonify({ "message": "Product not found" }), 404

# rota para alterar um produto
@app.route("/products/update/<int:id>", methods=["PUT"])
def updateProduct(id):
  product = Product.query.get(id)

  if not product:
    return jsonify({ "message": "Product not found" }), 404

  data = request.json

  if "name" in data:
    product.name = data["name"]

  if "price" in data:
    product.price = data["price"]

  if "description" in data:
    product.description = data["description"]

  db.session.commit()

  return jsonify({ "message": "Product updated successfully" }), 205

# rota para excluir um produto
@app.route("/products/delete/<int:id>", methods=["DELETE"])
def deleteProduct(id):
  product = Product.query.get(id)

  if product:
    db.session.delete(product)
    db.session.commit()

    return jsonify({ "message": "Product deleted successfully" }), 205

  return jsonify({ "message": "Product not found" }), 404

# define uma rota raiz
@app.route("/")
def index():
  return jsonify({ "message": "Hello World" })

# executa a aplicação
if __name__ == "__main__":
  app.run(debug=True)
