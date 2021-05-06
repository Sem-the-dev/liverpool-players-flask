from flask import Flask, jsonify, render_template, request, g
from flask_cors import CORS
import sqlite3
# from controllers import players

app = Flask(__name__)
CORS(app)


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('database.db')
        db.execute(
            'CREATE TABLE IF NOT EXISTS users (name TEXT, goals INT, id INTEGER PRIMARY KEY AUTOINCREMENT)')
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


@app.route('/')
def index():
    db = get_db()
    players = db.execute('select * from users')
    return render_template('players.html', players=players)


@app.route('/players', methods=['POST', 'GET'])
def result():
    if request.method == 'GET':
        return render_template("template.html")
    if request.method == 'POST':
        result = request.form
        db = get_db()
        db.execute(
            f'''INSERT INTO users (name, goals) values ('{result["name"]}', 0)''')
        db.commit()
        return jsonify({'message': f'Added player!'}), 200


@app.route('/players/<int:player_id>', methods=['PUT', 'POST', 'GET', 'PATCH', 'DELETE'])
def player_handler(player_id):
    if request.method == 'GET':
        db = get_db()
        players = db.execute(f'''select * from users WHERE id={player_id}''')
        return render_template('players_edit.html', players=players)
    if request.method == 'POST':
        result = request.form
        if result["goals"]:
            db = get_db()
            db.execute(
                f'''UPDATE users SET goals={result["goals"]}
                WHERE id={player_id}''')
            db.commit()
            return jsonify({'message': f'Added goals!'}), 200
        # if result["delete"]:
        #     db.execute(f'''DELETE FROM users WHERE id={player_id}''')
        #     db.commit()
        #     return jsonify({'message': f'Deleted player!'}), 200


if __name__ == "__main__":
    app.run(debug=True)
