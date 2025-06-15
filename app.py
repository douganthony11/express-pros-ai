from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/llm', methods=['POST', 'GET'])
@app.route('/llm/<path:subpath>', methods=['POST', 'GET'])
def handle_llm_request(subpath=None):
    try:
        print(f"Request method: {request.method}")
        print(f"Request path: {request.path}")
        print(f"Request headers: {dict(request.headers)}")
        
        response = {
            "response": "Hi! Thanks for calling Express Pros Logan. I'm here to help - what can I do for you today?",
            "response_id": 1
        }
        
        print(f"Sending response: {response}")
        return jsonify(response)
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/', methods=['GET'])
def health():
    return "Express Pros LLM is running!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))