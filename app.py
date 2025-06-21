# app.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
    return jsonify(message="hello word")  # Responds with JSON: {"message": "hello word"}

if __name__ == "__main__":
    # Run locally on http://127.0.0.1:5000/
    app.run(debug=True, host="0.0.0.0", port=5000)
