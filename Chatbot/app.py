from flask import Flask, request, jsonify
from newrag import get_model_response,clear_convo_history
from flask_cors import CORS


app = Flask(__name__)
CORS(app, origins="https://proud-meadow-0ace66e00.4.azurestaticapps.net")

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data['user_input']
    response = get_model_response(user_input)
    return jsonify({'response': response})

@app.route('/hello', methods=['GET'])
def say_hello():
    return jsonify({'message': 'Hello'})

@app.route('/clear_history', methods=['GET'])
def clear_history():
    clear_convo_history()
    return jsonify({"message": "Conversation history cleared."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)