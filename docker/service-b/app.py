from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/shipping")
def calculate_shipping():
	weight = float(request.args.get("weight",0))
	cost = weight * 5
	return jsonify({"cost":cost})

app.run(host="0.0.0.0", port=80)

