from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS items (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    place TEXT
                )""")
    conn.commit()
    conn.close()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        name = request.form["name"]
        place = request.form["place"]
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("INSERT INTO items (name, place) VALUES (?,?)", (name, place))
        conn.commit()
        conn.close()
        return redirect("/list")
    return render_template("add.html")

@app.route("/list.html")
def list_items():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM items")
    items = c.fetchall()
    conn.close()
    return render_template("list.html.html", items=items)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
