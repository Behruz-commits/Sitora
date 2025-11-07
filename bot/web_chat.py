from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_URL = "http://127.0.0.1:8000/chat"

@app.route('/')
def index():
    return render_template("chat.html")

@app.route('/send', methods=['POST'])
def send():
    data = request.get_json()
    payload = {"user": "WebUser", "message": data['msg'], "lang": data.get('lang', 'ru')}
    resp = requests.post(API_URL, json=payload)
    return jsonify(resp.json())

if __name__ == "__main__":
    app.run(port=9000, debug=True)
