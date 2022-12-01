import sqlite3 as sql


def updateUsers(username):
    conn = sql.connect("database.db")
    cur = conn.cursor()

    # query = f"-- UPDATE users SET valid = 1 WHERE username={username};"
    cur.execute(f"UPDATE users SET valid=0 WHERE username='{username}';")
    print("updated")
    conn.close()

def readUser(username):
    conn = sql.connect("database.db")
    cur = conn.cursor()

    query = f"SELECT * FROM users WHERE username='{username}';"

    cur.execute(query)
    users = cur.fetchall()
    print(users)
    conn.close()


if __name__ == "__main__":
    username = 'C-SM0420'
    readUser(username)
    updateUsers(username)
    readUser(username)

# UPDATE users SET valid=1 WHERE username='C-SM0420';
# SELECT * FROM users WHERE username='C-SM0082';