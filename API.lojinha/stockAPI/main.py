from flask import Flask, request, jsonify
from controllers.ProductController import ProductController
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Isso permite todas as origens
productController = ProductController()

@app.route("/products", methods=["GET"])
def list_products():
    return productController.getAll()

@app.route("/products/create", methods=["POST"])
def create_product():
    return productController.create()

@app.route("/products/details/<int:id>", methods=["GET"])
def product_details(id):
    return productController.details(id)

@app.route("/products/update/<int:id>", methods=["PUT"])
def update_product(id):
    return productController.update(id)

@app.route("/products/delete/<int:id>", methods=["DELETE"])
def delete_product(id):
    return productController.delete(id)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
