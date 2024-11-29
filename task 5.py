import telebot
import json
import requests
from telebot import types

with open('api.json', 'r') as config_file:
    config = json.load(config_file)

API_TOKEN = config['API_TOKEN']
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "Отправьте команду /get_user, чтобы выбрать данные о пользователе."
    )

@bot.message_handler(commands=['get_user'])
def get_user(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Имя", callback_data='first_name')
    btn2 = types.InlineKeyboardButton("Фамилия", callback_data='last_name')
    btn3 = types.InlineKeyboardButton("Email", callback_data='email')
    btn4 = types.InlineKeyboardButton("Аватар", callback_data='avatar')
    markup.add(btn1, btn2, btn3, btn4)

    bot.send_message(
        message.chat.id,
        "Выберите, какую информацию о пользователе вы хотите увидеть:",
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    response = requests.get("https://reqres.in/api/users/2")

    if response.status_code == 200:
        data = response.json()
        user_data = data['data']

        if call.data == 'first_name':
            bot.send_message(call.message.chat.id, f"Имя: {user_data['first_name']}")
        elif call.data == 'last_name':
            bot.send_message(call.message.chat.id, f"Фамилия: {user_data['last_name']}")
        elif call.data == 'email':
            bot.send_message(call.message.chat.id, f"Email: {user_data['email']}")
        elif call.data == 'avatar':
            bot.send_photo(call.message.chat.id, user_data['avatar'])
    else:
        bot.send_message(
            call.message.chat.id,
            "Произошла ошибка при запросе данных."
        )

bot.polling()
