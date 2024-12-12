from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

RAILS_BASE_URL = "http://172.19.55.85:3000"

@app.route('/api/notifications', methods=['POST'])
def create_notification():
    data = request.json
    try:
        response = requests.post(f"{RAILS_BASE_URL}/notifications", json=data)
        response.raise_for_status()  # Lanza una excepción si hay un error HTTP
        return jsonify(response.json()), response.status_code
    except requests.exceptions.HTTPError as http_err:
        return {
            "error": str(http_err),
            "details": response.text
        }, response.status_code
    except ValueError:  # Maneja JSON inválido
        return {
            "error": "Invalid JSON response",
            "details": response.text
        }, 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)
