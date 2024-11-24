from flask import Flask, request, jsonify
from flask_cors import CORS
from llm import process_user_input

import subprocess

app = Flask(__name__)
app.debug = False
CORS(app)
subprocess('')

@app.route("/chat", methods=["POST"])
def chat():

    user_input = request.json.get("message", "")
    response = process_user_input(user_input)
    return jsonify({"response": response})

# @app.route("/food-banks", methods=["GET"])
# def food_banks():
#     school = request.args.get("school", "")
#     data = get_food_banks(school)
#     return jsonify(data)

if __name__ == "__main__":
    app.run()
