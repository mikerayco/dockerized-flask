from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello():
    return "Hello! This is a Flask app running in a container!", 200


@app.route("/aloha", methods=["GET"])
def aloha():
    return "Aloha World!", 200


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
