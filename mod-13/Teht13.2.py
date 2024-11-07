from flask import Flask, jsonify, abort
import mysql.connector

app = Flask(__name__)

# Database connection
def connect_to_database():
    return mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        database="flight_game",  # Fill in your database name here
        user="",           # Fill in your MySQL username here
        password="",        # Fill in your MySQL password here
        autocommit=True
    )

# Function to get airport information by ICAO code
def get_airport_by_icao(icao_code):
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute("SELECT ident, name, municipality FROM airport WHERE ident = %s", (icao_code,))
    row = cursor.fetchone()
    cursor.close()
    connection.close()
    return row

# Route to retrieve airport information by ICAO code
@app.route('/kenttä/<string:icao_code>')
def airport_info(icao_code):
    airport = get_airport_by_icao(icao_code.upper())
    if airport:
        result = {
            "ICAO": airport[0],
            "Name": airport[1],
            "Municipality": airport[2]
        }
        return jsonify(result)
    else:
        # Return a 404 error if the ICAO code is not found in the database
        abort(404, description="Airport not found")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
