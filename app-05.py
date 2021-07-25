from flask import Flask, request
import sqlite3

app = Flask(__name__)

# Level 5
@app.route("/5/")
def level5():
    return "<form method='POST'>Username: <input name='username'><br>Password: <input type='password' name='password'><br><input type='submit' value='Log in!'></form>"
   

@app.route("/5/", methods=["POST"])
def level5_post():
    con = sqlite3.connect('users.db')
    cur = con.cursor()

    id = request.form['username']
    pw = request.form['password']
    results = list(cur.execute('SELECT * FROM users WHERE id = "' + id + '" AND pw = "' + pw + '"'))
    if len(results) == 0:
        return "User not found", 404
    real_id, real_pw = results[0]
    if pw != real_pw:
        return "Invalid password", 404
    return f"Welcome {id}!"

app.run(port=21726)