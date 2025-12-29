from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# ---------- MySQL Connection ----------
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOUR_MYSQL_PASSWORD",
        database="student_db"
    )

# ---------- Home Page ----------
@app.route('/')
def home():
    return render_template('index.html')

# ---------- Form Submit ----------
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    age = request.form['age']
    department = request.form['department']

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO student (name, email, age, department) VALUES (%s, %s, %s, %s)",
        (name, email, age, department)
    )

    conn.commit()
    cursor.close()
    conn.close()

    return "✅ Data inserted into MySQL successfully!"

# ---------- Run App ----------
if __name__ == '__main__':
    app.run(debug=True)
