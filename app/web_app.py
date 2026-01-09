import os
import sys
from flask import Flask, render_template, request

# Add project root to Python path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from src.model_inference import predict_price

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    price = None
    if request.method == "POST":
        data = {
            "area": int(request.form["area"]),
            "bedrooms": int(request.form["bedrooms"]),
            "bathrooms": int(request.form["bathrooms"]),
            "age": int(request.form["age"]),
            "location": request.form["location"],
            "property_type": request.form["property_type"]
        }
        price = predict_price(data)

    return render_template("index.html", price=price)

if __name__ == "__main__":
    app.run(debug=True)
