from flask import Flask, request, jsonify
from query_data import get_llama_response

app = Flask(__name__)


@app.route('/query', methods=['POST'])
def query_llama():
    data = request.get_json()
    if 'query' not in data:
        return jsonify({'error': 'No query provided'}), 400
    
    query = data['query']
    convo_history = data['conversation_history']
    response = get_llama_response(query,convo_history)
    return jsonify({'response': response})


@app.route('/hello', methods=['GET'])
def say_hello():
    return jsonify({'message': 'Hello'})


if __name__ == '__main__':
    app.run(debug=True)