import os
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests

def fetch_game_data(casino_url, username):
    try:
        response = requests.get(casino_url, timeout=5)  # Added timeout to avoid hanging requests
        if response.status_code == 200:
            game_data = response.json()
            prediction = {
                "multiplier": "x2.5",
                "confidence": "High",
                "data_fetched": game_data  # Including fetched data for debugging
            }
            return prediction
        else:
            return {"error": f"Failed to fetch game data. Status Code: {response.status_code}"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

@app.route('/predict', methods=['GET'])
def predict():
    username = request.args.get('username')
    casino_url = request.args.get('url')

    if not username or not casino_url:
        return jsonify({"error": "Username and Casino URL are required"}), 400  # Return 400 Bad Request
    
    prediction = fetch_game_data(casino_url, username)
    return jsonify(prediction), 200  # Explicitly set response status

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "API is running!"}), 200  # Simple health check

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use Render's assigned port
    app.run(host='0.0.0.0', port=port)

