from flask import Flask, jsonify, render_template, request
from flask_mysqldb import MySQL
import MySQLdb

app = Flask(__name__)
app.secret_key = ""

app.config["MYSQL_HOST"] ="localhost"
app.config["MYSQL_SERVER"] ="root"
app.config["MYSQL_PASSWORD"] ="1974091"
app.config["MYSQL_DB"] ="gauravdb"

db =MySQL(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/app/api/courses', methods=['GET'])
def show():
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursors)
    cursor.execute('SELECT * FROM COURSES')
    info =cursor.fetchall()

    return jsonify(info)




