from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/llm', methods=['POST'])
@app.route('/llm/<path:subpath>', methods=['POST', 'GET'])
def handle_llm_request(subpath=None):
    data = request.get_json() if request.is_json else {}
    
    # For now, just return a simple response to test
    return jsonify({
        "response": "Hi! Thanks for calling Express Pros Logan. I'm here to help - what can I do for you today?",
        "response_id": 1
    })

@app.route('/', methods=['GET'])
def health():
    return "Express Pros LLM is running!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))