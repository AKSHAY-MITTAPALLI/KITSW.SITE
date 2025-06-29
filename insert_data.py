import mysql.connector
from flask import Flask, request, jsonify

from flask import jsonify

app = Flask(__name__)

@app.route('/api/student-data', methods=['GET'])
def get_student_data():
    # Sample student data
    student_data = {
        'rollNumber': '12345',
        'name': 'John Doe',
        'branch': 'Computer Science',
        'semester': '5',
        'cgpa': '8.5'
    }
    return jsonify(student_data)


def validate_login(roll_number, password):
    # Connect to the MySQL database
    connection = mysql.connector.connect(
        host='localhost',
        user='your_username',
        password='your_password',
        database='your_database'
    )
    cursor = connection.cursor()

    # Query to check if the credentials are valid
    query = "SELECT * FROM students WHERE roll_number = %s AND password = %s"
    cursor.execute(query, (roll_number, password))
    result = cursor.fetchone()

    cursor.close()
    connection.close()

    # Return success if a record is found
    if result:
        return True
    else:
        return False

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    roll_number = data.get('rollNumber')
    password = data.get('password')

    if validate_login(roll_number, password):
        return jsonify(success=True)
    else:
        return jsonify(success=False)

if __name__ == '__main__':
    app.run(debug=True)
