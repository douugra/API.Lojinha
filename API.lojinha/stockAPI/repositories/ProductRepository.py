from repositories.BaseRepository import BaseRepository

class ProductRepository(BaseRepository):
    
    def __init__(self):
        super().__init__()

    def getAll(self):
        query = "SELECT * FROM products"
        return self.executeQuery(query)

    def create(self, productData):
        command = f"INSERT INTO products (name, cost, price) VALUES ('{productData['name']}', {productData['cost']}, {productData['price']})"
        self.execute(command)

    def details(self, id:int):
        query = f"SELECT * FROM products WHERE id = {id}"
        return self.executeQuery(query)

    def update(self, id:int, productData):
        command = f"UPDATE products SET name='{productData['name']}', cost={productData['cost']}, price={productData['price']} WHERE id = {id}"
        self.execute(command)

    def delete(self, id:int):
        command = f"DELETE FROM products WHERE id = {id}"
        self.execute(command)
