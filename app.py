from flask import Flask, render_template, request, redirect, session, jsonify
import sqlite3
from model import predict

app = Flask(__name__)
app.secret_key = "curabot_ai"

# Initialize DB
def init_db():
    conn = sqlite3.connect("users.db")
    conn.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        username TEXT UNIQUE,
        password TEXT)
    """)
    conn.close()

init_db()

# Login
@app.route("/", methods=["GET","POST"])
def login():
    if request.method == "POST":
        user = request.form["username"]
        pw = request.form["password"]
        conn = sqlite3.connect("users.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username=? AND password=?", (user,pw))
        data = cur.fetchone()
        conn.close()
        if data:
            session["user"] = user
            return redirect("/chat")
        else:
            return render_template("login.html", error="Invalid credentials")
    return render_template("login.html")

# Register
@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        user = request.form["username"]
        pw = request.form["password"]
        conn = sqlite3.connect("users.db")
        try:
            conn.execute("INSERT INTO users(username,password) VALUES (?,?)",(user,pw))
            conn.commit()
        except sqlite3.IntegrityError:
            conn.close()
            return render_template("register.html", error="Username already exists")
        conn.close()
        return redirect("/")
    return render_template("register.html")

# Logout
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/")

# Chat
@app.route("/chat")
def chat():
    if "user" not in session:
        return redirect("/")
    return render_template("index.html")

# Bot API
@app.route("/get", methods=["POST"])
def bot():
    msg = request.json.get("message")
    disease, medicine = predict(msg)
    reply = f"Possible illness: {disease}\nSuggested medicine: {', '.join(medicine)}\n⚠️ This is not a medical diagnosis."
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)