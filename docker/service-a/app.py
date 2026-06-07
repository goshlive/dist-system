from flask import Flask, jsonify

app = Flask(__name__)

products = {
	1: {"name": "Laptop", "price": 1000, "weight": 2},
	2: {"name": "Phone", "price": 500, "weight": 1}
}

@app.route("/api/products/<int:id>")
def get_product(id):
	return jsonify(products.get(id, {}))

@app.route("/api/products")
def list_products():
    return jsonify(products)

app.run(host="0.0.0.0", port=80)

