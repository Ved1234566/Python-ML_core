from flask import Flask, render_template, request
from db_config import get_connection

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

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

    return "Data inserted successfully!"

if __name__ == '__main__':
    app.run(debug=True)
