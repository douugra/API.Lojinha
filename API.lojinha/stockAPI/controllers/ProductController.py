from workers.ProductWorker import ProductWorker
from flask import request, jsonify

class ProductController():
    def __init__(self):
        self.productWorker = ProductWorker()

    def getAll(self):
        products = self.productWorker.getAll()
        return jsonify(products), 200

    def create(self):
        productData = request.get_json()
        self.productWorker.create(productData)
        return jsonify({"message": "Produto criado com sucesso"}), 201

    def details(self, id:int):
        product = self.productWorker.details(id)
        return jsonify(product), 200

    def update(self, id:int):
        productData = request.get_json()
        self.productWorker.update(id, productData)
        return jsonify({"message": "Produto atualizado com sucesso"}), 200

    def delete(self, id:int):
        self.productWorker.delete(id)
        return jsonify({"message": "Produto excluído com sucesso"}), 200
