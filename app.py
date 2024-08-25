from flask import Flask, jsonify, request, send_from_directory
from collections import OrderedDict
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='static')
CORS(app)

@app.route('/testing', methods=['POST'])
def process_data():
    try:
        data = request.json.get("data", [])
        numbers = [item for item in data if item.isdigit()]
        alphabets = [item for item in data if item.isalpha()]
        lowercase_alphabets = [char for char in alphabets if char.islower()]
        highest_lowercase = max(lowercase_alphabets) if lowercase_alphabets else None

        user_id = "john_doe_17091999"
        email = "john@xyz.com"
        roll_number = "ABCD123"

        response = OrderedDict([
            ('is_success', True),
            ('user_id', user_id),
            ('email', email),
            ('roll_number', roll_number),
            ('numbers', numbers),
            ('alphabets', alphabets),
            ('highest_lowercase_alphabet', [highest_lowercase] if highest_lowercase else [])
        ])
        return jsonify(response)
    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 400

@app.route('/testing', methods=['GET'])
def get_operation_code():
    return jsonify({"operation_code": 1}), 200

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_react_app(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
