from flask import Flask, jsonify, render_template, request, g
from flask_cors import CORS
import sqlite3
# from controllers import players

app = Flask(__name__)
CORS(app)

players = [{"name": 'Player1'}]


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('database.db')
        db.execute('CREATE TABLE IF NOT EXISTS users (name TEXT)')
        print(db)
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
    users = query_db('select * from users')
    return jsonify({'message': users}), 200


@app.route('/players', methods=['POST', 'GET'])
def result():
    if request.method == 'GET':
        return render_template("template.html")
    if request.method == 'POST':
        result = request.form
        print(result)
        db = get_db()
        db.execute(f'''INSERT INTO users (name) values ('{result["name"]}')''')
        db.commit()
        return jsonify({'message': f'Added player!'}), 200


if __name__ == "__main__":
    app.run(debug=True)
