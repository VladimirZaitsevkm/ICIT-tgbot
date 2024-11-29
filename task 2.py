import telebot
import json

with open('api.json', 'r') as config_file:
    config = json.load(config_file)

API_TOKEN = config['API_TOKEN']  

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(content_types=['voice'])
def handle_voice_message(message):
    bot.reply_to(message, "Спасибо за ваше голосовое сообщение!")

@bot.message_handler(func=lambda message: True)
def handle_other_messages(message):
    bot.send_message(message.chat.id, "Я реагирую только на голосовые сообщения.")

bot.polling()
