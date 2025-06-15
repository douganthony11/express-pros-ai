from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/llm', methods=['POST', 'GET'])
@app.route('/llm/', methods=['POST', 'GET'])  
@app.route('/llm/<anything>', methods=['POST', 'GET'])
@app.route('/llm/<path:anything>', methods=['POST', 'GET'])
def handle_llm_request(anything=None):
    try:
        print(f"LLM request received!")
        print(f"Method: {request.method}")
        print(f"Path: {request.path}")
        print(f"Args: {request.args}")
        
        response = {
            "response": "Hi! Thanks for calling Express Pros Logan. I'm here to help - what can I do for you today?",
            "response_id": 1
        }
        
        return jsonify(response), 200
        
    except Exception as e:
        print(f"Error in LLM handler: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/', methods=['GET'])
def health():
    return "Express Pros LLM is running!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))