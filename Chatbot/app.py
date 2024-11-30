from flask import Flask, request, jsonify
from newrag import get_model_response
from flask_cors import CORS


app = Flask(__name__)
# CORS(app, origins="https://proud-meadow-0ace66e00.4.azurestaticapps.net")
CORS(app, origins="*")


@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data['user_input']
    last_context = data['last_context']
    conversation_history = data['conversation_history']
    response,context = get_model_response(user_input,conversation_history,last_context)
    return jsonify({'response': response, 'context': context})

@app.route('/hello', methods=['GET'])
def say_hello():
    return jsonify({'message': 'Hello'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)