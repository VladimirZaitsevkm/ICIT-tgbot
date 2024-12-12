import telebot
import json
from telebot import types

with open('api.json', 'r') as config_file:
    config = json.load(config_file)

API_TOKEN = config['API_TOKEN']
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Разработка")
    btn2 = types.KeyboardButton("Тестирование")
    btn3 = types.KeyboardButton("Аналитика")
    markup.add(btn1, btn2, btn3)

    bot.send_message(
        message.chat.id,
        "Выбери категорию, чтобы получить список сайтов:\n\n",
        reply_markup=markup
    )

@bot.message_handler(func=lambda message: message.text in ['Разработка', 'Тестирование', 'Аналитика'])
def send_resources(message):
    if message.text == "Разработка":
        bot.send_message(message.chat.id, "Вот полезные ресурсы для разработчиков:\n\n"
                                          "1. [Stack Overflow](https://stackoverflow.com)\n"
                                          "2. [GitHub](https://github.com)\n"
                                          "3. [MDN Web Docs](https://developer.mozilla.org)")
    elif message.text == "Тестирование":
        bot.send_message(message.chat.id, "Вот полезные ресурсы для тестировщиков:\n\n"
                                          "1. [Software Testing Help](https://www.softwaretestinghelp.com)\n"
                                          "2. [Guru99 Testing](https://www.guru99.com/software-testing.html)\n"
                                          "3. [Ministry of Testing](https://www.ministryoftesting.com)")
    elif message.text == "Аналитика":
        bot.send_message(message.chat.id, "Вот полезные ресурсы для аналитиков:\n\n"
                                          "1. [Kaggle](https://www.kaggle.com)\n"
                                          "2. [Google Analytics Academy](https://analytics.google.com/analytics/academy/)\n"
                                          "3. [Tableau Public](https://public.tableau.com)")
bot.polling()
