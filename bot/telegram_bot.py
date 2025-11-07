import requests
import telebot

TOKEN = 'ВАШ_ТОКЕН'
API_URL = 'http://127.0.0.1:8000/chat'
DEFAULT_LANG = 'ru'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Здравствуйте! Я Sitora. Спросите меня о ваших делах или заказе.")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    user = message.from_user.first_name
    msg = message.text
    payload = {'user': user, 'message': msg, 'lang': DEFAULT_LANG}
    try:
        r = requests.post(API_URL, json=payload, timeout=5)
        reply = r.json().get('response', 'Ошибка связи')
    except Exception:
        reply = "Извините, сервис временно недоступен."
    bot.reply_to(message, reply)

bot.polling()
