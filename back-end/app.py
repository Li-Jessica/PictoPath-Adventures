from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import base64

app = Flask(__name__)
CORS(app)

@app.route('/run_ai', methods=['POST'])
def run_ai():
    try:
        account_id = 'e10c9f080ad11db06ca95eb25bba9018'
        api_token = 'oiCOVhx5LwN4TcU6HkV8o87rFGTT3-0fveWTRtUs'
        model = '@cf/stabilityai/stable-diffusion-xl-base-1.0'
        ai_endpoint = f'https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/run/{model}'

        headers = {
            'Authorization': f'Bearer {api_token}',
            'Content-Type': 'application/json',
        }

        data = request.get_json()
        prompt = data.get('prompt', '')

        payload = {
            'prompt': prompt,
        }

        response = requests.post(ai_endpoint, json=payload, headers=headers)

        if response.status_code == 200:
            image_data_base64 = base64.b64encode(response.content).decode('utf-8')

            return jsonify({"image_data": image_data_base64})
        else:
            return jsonify({"error": True, "message": "AI request failed", "status_code": response.status_code})

    except Exception as e:
        return jsonify({"error": True, "message": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
