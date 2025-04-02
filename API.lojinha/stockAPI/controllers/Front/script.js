const API_URL = "http://127.0.0.1:5000/products";

async function createProduct() {
    const name = document.getElementById('name').value;
    const cost = document.getElementById('cost').value;
    const price = document.getElementById('price').value;

    const response = await fetch(`${API_URL}/create`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, cost, price })
    });
    const data = await response.json();
    document.getElementById('result').innerText = JSON.stringify(data);
}

async function getProducts() {
    const response = await fetch(API_URL);
    const data = await response.json();
    document.getElementById('result').innerText = JSON.stringify(data);
}

async function getProductDetails() {
    const id = document.getElementById('productId').value;
    const response = await fetch(`${API_URL}/details/${id}`);
    const data = await response.json();
    document.getElementById('result').innerText = JSON.stringify(data);
}

async function updateProduct() {
    const id = document.getElementById('updateId').value;
    const name = document.getElementById('updateName').value;
    const cost = document.getElementById('updateCost').value;
    const price = document.getElementById('updatePrice').value;

    const response = await fetch(`${API_URL}/update/${id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, cost, price })
    });
    const data = await response.json();
    document.getElementById('result').innerText = JSON.stringify(data);
}

async function deleteProduct() {
    const id = document.getElementById('deleteId').value;
    const response = await fetch(`${API_URL}/delete/${id}`, {
        method: 'DELETE'
    });
    const data = await response.json();
    document.getElementById('result').innerText = JSON.stringify(data);
}
