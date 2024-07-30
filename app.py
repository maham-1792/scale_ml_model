from flask import Flask, request, jsonify
import cohere
import os
import logging
import socket

app = Flask(__name__)

# Initialize the Cohere client
cohere_api_key = os.getenv('tqTkOB5IwS69rO8XirIcu0rk6dfzQ0coiZYoxxHa')
cohere_client = cohere.Client(cohere_api_key)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        response = cohere_client.generate(
            model='command-xlarge-nightly',
            prompt=data['text'],
            max_tokens=50
        )
        pod_name = socket.gethostname()
        pod_ip = socket.gethostbyname(pod_name)
        return jsonify({
            'generated_text': response.generations[0].text,
            'pod_name': pod_name,
            'pod_ip': pod_ip
        })
    except Exception as e:
        logging.error(f"Error: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/', methods=['GET'])
def home():
    return "Cohere Model Service is running!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

