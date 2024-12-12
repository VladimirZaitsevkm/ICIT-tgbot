import telebot
import json

with open('api.json', 'r') as config_file:
    config = json.load(config_file)

API_TOKEN = config['API_TOKEN']  
bot = telebot.TeleBot(API_TOKEN)

user_data = {}

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Как тебя зовут?")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_id = message.chat.id

    if user_id not in user_data:
        user_data[user_id] = {'name': message.text}
        bot.send_message(user_id, f"Тебя зовут {message.text}, сколько тебе лет?")

    elif 'age' not in user_data[user_id]:
        user_data[user_id]['age'] = message.text
        bot.send_message(user_id, f"Тебе {message.text} лет")
bot.polling()
