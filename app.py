from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend to communicate with backend

def fetch_game_data(casino_url, username):
    try:
        response = requests.get(casino_url)
        if response.status_code == 200:
            game_data = response.json()
            prediction = {
                "multiplier": "x2.5",
                "confidence": "High"
            }
            return prediction
        else:
            return {"error": "Failed to fetch game data"}
    except Exception as e:
        return {"error": str(e)}

@app.route('/predict', methods=['GET'])
def predict():
    username = request.args.get('username')
    casino_url = request.args.get('url')
    if not username or not casino_url:
        return jsonify({"error": "Username and Casino URL are required"})
    
    prediction = fetch_game_data(casino_url, username)
    return jsonify(prediction)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
