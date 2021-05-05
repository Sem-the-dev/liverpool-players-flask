from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
# from controllers import players

app = Flask(__name__)
CORS(app)

# Add POST, GET, PATCH and DELETE methods

players = [{"name": 'Player1'}]


@app.route("/")
def template_test():
    return render_template('players.html', players=players)


@app.route('/players', methods=['POST', 'GET'])
def result():
    if request.method == 'GET':
        return render_template("template.html")
    if request.method == 'POST':
        result = request.form
        print(result)
        players.append(result)
        return jsonify({'message': f'Added player!'}), 200

# @app.route('/players/id/:id', methods=['POST', 'GET'])
# def result():
#     if request.method == 'POST':
#         result = request.form
#         players.find(id).goals + 1
#         return jsonify({'message': f'Added player!'}), 200


if __name__ == "__main__":
    app.run(debug=True)
