from flask import Flask
import os
import time
import random

app = Flask(__name__)

WORKER = os.environ["WORKER_NAME"]

@app.route("/processImage")
def process_image():
    duration = random.randint(3, 5)
    time.sleep(duration)
    msg = f"{WORKER} finished image processing ({duration}s)"
    print(msg, flush=True)
    return msg

@app.route("/generateReport")
def generate_report():
    duration = random.randint(3, 5)
    time.sleep(duration)
    msg = f"{WORKER} finished report generation ({duration}s)"
    print(msg, flush=True)
    return msg

app.run(host="0.0.0.0", port=7000, threaded=True)