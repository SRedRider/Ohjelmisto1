from flask import Flask, jsonify

app = Flask(__name__)

# Funktio, joka tarkistaa, onko luku alkuluku
def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Reitti, joka tarkistaa alkuluvun
@app.route('/alkuluku/<int:luku>')
def alkuluku(luku):
    result = {
        "Number": luku,
        "isPrime": is_prime(luku)
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
