from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
import sqlite3
# from controllers import players

app = Flask(__name__)
CORS(app)

players = [{"name": 'Player1'}]


@app.route("/")
def template_test():
    return render_template('players.html', players=players)


@app.route('/database/')
def database():
    """Returns webpage containing query results from database
    Returns
    -------
    template : obj
        The ``database.html`` webpage.
    """

    # Connect to database
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    # Execute query
    sql_command = 'SELECT * FROM main_table;'
    cursor.execute(sql_command)

    # Parse results
    results_dict = {}
    results = cursor.fetchall()
    for result in results:
        results_dict[result[1]] = result[2]

    return render_template('database.html', results_dict=results_dict)


@app.route('/players', methods=['POST', 'GET'])
def result():
    if request.method == 'GET':
        return render_template("template.html")
    if request.method == 'POST':
        result = request.form
        print(result)
        players.append(result)
        return jsonify({'message': f'Added player!'}), 200


if __name__ == "__main__":
    app.run(debug=True)
