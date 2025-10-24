from flask import Flask, jsonify

# Tworzymy instancję aplikacji Flask
app = Flask(__name__)


# Definiujemy "endpoint" (adres) o nazwie /hello
# Używamy metody GET, bo tylko pobieramy dane
@app.route('/hello', methods=['GET'])
def get_hello():
    # Tworzymy dane, które chcemy zwrócić
    # Muszą być w formacie JSON (słownik Pythona)
    dane = {
        "id": 1,
        "wiadomosc": "Gratulacje, Twoja aplikacja Android połączyła się z API w Pythonie!"
    }

    # Zwracamy dane jako odpowiedź JSON
    return jsonify(dane)


# Ta część pozwala uruchomić serwer lokalnie do testów
# komendą "python app.py"
if __name__ == '__main__':
    # Używamy portu 10000, Render to lubi
    app.run(debug=True, host='0.0.0.0', port=10000)