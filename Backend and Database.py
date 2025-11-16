from flask import Flask,render_template
import sqlite3
import os
app = Flask(__name__)
DB_NAME = " lost_and_found.db"
def init_db():
    if not os.path.exists(DB_NAME):
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute("""
        CREATE TABLE items (
            id INTEGER PRIMARY KEY AUTOINCREMANT,
            name TEXT NOT NULL,
            location TEXT NOT NULL,
            description TEXT, 
            contact TEXT NOT NULL,   
        )
        """)
    conn.commit()
    conn.close()
    print("Database created")
def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row = sqlite3.Row
    return conn
@app.route("/")
def index():
    conn = get_db()
    items = conn.execute("SELECT * FROM items").fetchall()
    conn.close()
    return render_template("index.html",items=items)
