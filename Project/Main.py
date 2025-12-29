import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",          # or root if it works
        password="root",   # your password
        database="school"   # database with student table
    )
