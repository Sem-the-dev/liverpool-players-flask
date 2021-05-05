from flask import Flask, jsonify, request
from flask_cors import CORS
from controllers import players

app = Flask(__name__)
CORS(app)

# Add POST, GET, PATCH and DELETE methods


if __name__ == "__main__":
    app.run(debug=True)