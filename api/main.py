"""
Sitora API Core
----------------
Это базовый модуль, через который внешние приложения (бот, веб-панель)
могут обращаться к ИИ-ядру Sitora.

Позже сюда добавится подключение к локальной модели или ChatGPT-API.
"""

from flask import Flask, request, jsonify
import json

app = Flask(__name__)

def localize(lang, key):
    with open(f'../i18n/{lang}.json', encoding='utf-8') as f:
        return json.load(f).get(key, key)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user = data.get('user', 'Гость')
    msg = data.get('message', '')
    lang = data.get('lang', 'ru')

    # Кейсовый обработчик (пример)
    if 'заказ' in msg.lower():
        reply = localize(lang, "order_response")
    else:
        reply = localize(lang, "default")

    return jsonify({'response': f"{user}, {reply}"})

if __name__ == '__main__':
    app.run(port=8000, host='0.0.0.0', debug=True)
