from flask import Flask, jsonify
import firebase_admin
from firebase_admin import credentials, firestore
import os  # Do odczytania zmiennej

app = Flask(__name__)

# --- INICJALIZACJA FIREBASE ---
# Użyj klucza ze zmiennej środowiskowej (Secret File)
key_path = os.environ.get('FIREBASE_KEY_JSON', 'firebase-key.json')
cred = credentials.Certificate(key_path)
firebase_admin.initialize_app(cred)

# Pobierz klienta bazy danych
db = firestore.client()


# ------------------------------

@app.route('/hello', methods=['GET'])
def get_hello():
    # Zamiast tylko zwracać JSON, zapiszmy coś do bazy

    # Dane, które "rozpoznałeś" z paragonu
    dane_paragonu = {
        'sklep': 'Sklep Testowy',
        'data': firestore.SERVER_TIMESTAMP,  # Użyj czasu serwera
        'produkty': [
            {'nazwa': 'Jbłk', 'cena': 2.99},
            {'nazwa': 'Mleko', 'cena': 3.50}
        ],
        'suma': 6.49
    }

    # Dodaj nowy dokument do kolekcji "paragony"
    # Firebase automatycznie wygeneruje unikalne ID
    doc_ref = db.collection('paragony').document()
    doc_ref.set(dane_paragonu)

    # Zwróć ID dokumentu do aplikacji
    return jsonify({
        "status": "sukces",
        "id_paragonu": doc_ref.id
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=10000)
