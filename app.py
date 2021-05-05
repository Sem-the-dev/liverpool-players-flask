from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from werkzeug import exceptions

app = Flask(__name__)
CORS(app)

# Add POST, GET, PATCH and DELETE methods
players = [
{'id':1, 'name': 'Alisson Becker'},
{'id': 2, 'name': 'Virgil Van Dijk'},
{'id': 3, 'name': 'Joe Gomez'},
{'id': 4, 'name': 'Ozan Kabak'},
{'id': 5, 'name': 'Andy Robertson'},
{'id': 6, 'name': 'Joel Matip'},
{'id': 7, 'name': 'Trent Alexander-Arnold'},
{'id': 8, 'name': 'Fabinho'},
{'id': 9, 'name': 'Georginio Wijnaldum'},
{'id': 10, 'name': 'Thiago'},
{'id': 11, 'name': 'Jordan Henderson'},
{'id': 12,'name': 'Roberto Firmino'},
]
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

@app.route('/players/<int:player_id>', methods=['PUT', 'GET', 'PATCH', 'DELETE'])
def player_handler(player_id):
    fns = {
        'GET': players.show,
        'PATCH': players.update,
        'PUT': players.update,
        'DELETE': players.destroy
    }
    resp, code = fns[request.method](request, player_id)
    return jsonify(resp), code


if __name__ == "__main__":
    app.run(debug=True)
