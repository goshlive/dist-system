from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

#If you run the web outside Docker, use:
#SERVICE_A_URL = "http://localhost:8081/api/products"
#SERVICE_B_URL = "http://localhost:8082/api/shipping"

#Run the web inside Docker, use:
SERVICE_A_URL = "http://host.docker.internal:8081/api/products"
SERVICE_B_URL = "http://host.docker.internal:8082/api/shipping"

@app.route("/checkout/<int:product_id>")
def checkout(product_id):

    product = requests.get(f"{SERVICE_A_URL}/{product_id}").json()

    shipping = requests.get(
        SERVICE_B_URL,
        params={"weight": product["weight"]}
    ).json()

    total = product["price"] + shipping["cost"]

    return jsonify({
        "product": product["name"],
        "price": product["price"],
        "shipping": shipping["cost"],
        "total": total
    })

app.run(host="0.0.0.0", port=80)