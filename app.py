from flask import Flask, jsonify
import firebase_admin
from firebase_admin import credentials, firestore

app = Flask(__name__)

# --- INICJALIZACJA FIREBASE ---
# Bezpośrednio ładujemy plik o nazwie, którą podaliśmy w Render
try:
    cred = credentials.Certificate('firebase-key.json')
    firebase_admin.initialize_app(cred)
except FileNotFoundError:
    print("BŁĄD: Nie znaleziono pliku 'firebase-key.json'.")
    print("Upewnij się, że dodałeś go jako Secret File w panelu Render.")
    # Możesz dodać obsługę błędu, jeśli pliku nie ma
except Exception as e:
    print(f"Błąd inicjalizacji Firebase: {e}")

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
