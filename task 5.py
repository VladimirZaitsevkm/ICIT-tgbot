import telebot
import json
import requests

with open('api.json', 'r') as config_file:
    config = json.load(config_file)

API_TOKEN = config['API_TOKEN']
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "Отправьте команду /get_user, чтобы получить данные с API."
    )

@bot.message_handler(commands=['get_user'])
def get_user(message):
    response = requests.get("https://reqres.in/api/users/2")

    if response.status_code == 200:
        data = response.json()
        email = data['data']['email']
        bot.send_message(message.chat.id, f"Email пользователя: {email}")
    else:
        bot.send_message(message.chat.id, "Произошла ошибка при запросе данных.")

bot.polling()
