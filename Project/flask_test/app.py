from flask import Flask, render_template, request, redirect
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# ---------- MySQL Connection ----------
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="School"
    )

# ---------- Home Page (FETCH DATA) ----------
@app.route('/')
def home():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM student")
    students = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('index.html', students=students)

# ---------- Form Submit ----------
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    age = request.form['age']
    department = request.form['department']

    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO student (name, email, age, department) VALUES (%s, %s, %s, %s)",
            (name, email, age, department)
        )

        conn.commit()

    except Error as e:
        if e.errno == 1062:
            return "❌ This email already exists. Please use a different email."
        else:
            return f"❌ Database error: {e}"

    finally:
        cursor.close()
        conn.close()

    return redirect('/')

# ---------- Run App ----------
if __name__ == '__main__':
    app.run(debug=True)
