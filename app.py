from flask import Flask, render_template, redirect, request, Response
import sqlite3 as sql

app = Flask(__name__)


def retrieveUsers(username, password):
    conn = sql.connect("database.db")
    cur = conn.cursor()

    cur.execute(f"SELECT * FROM users WHERE username='{username}' and password='{password}'")
    users = cur.fetchall()
    print(users)
    conn.close()
    return users


def updateUsers(username):
    conn = sql.connect("database.db")
    cur = conn.cursor()

    query = f"UPDATE users SET valid = 0 WHERE username='{username}';"

    cur.execute(query)
    conn.close()


def validate(username, passwd):
    users = retrieveUsers(username, passwd)
    if users is not None and len(users) == 1:
        return True
    else:
        return False


@app.route('/action', methods=['GET', 'POST'])
def action():
    if request.method == 'POST':
        username = request.form.get('username')
        passwd = request.form.get('passwd')

        if validate(username, passwd):

            return redirect('https://calendar.google.com/calendar/u/0?cid=c3RlZWxtb3VudGFpbnYxLjFAZ21haWwuY29t')
        else:
            return redirect('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    else:
        return redirect('/')


@app.route('/accept', methods=['POST'])
def accept():
    content = request.json
    account = content['account']
    teamID = content['teamID']
    password = content['password']
    if password == "macr0hardBot":
        with open("wallet.csv", "a") as f:
            f.write(f"{account}, {teamID}\n")
        return Response("{'a':'b'}", status=201, mimetype='application/json')
    else:
        return Response("{'a':'b'}", status=401, mimetype='application/json')


@app.route('/')
def auth():  # put application's code here
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
