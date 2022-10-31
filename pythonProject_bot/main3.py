# @school250422_bot

import telebot
from telebot import types

API_TOKEN = '5297760495:AAHxzRB93VylGzK-MdlKkCNQdeI6YPe9X20'
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(content_types=["text"])
def default_test(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Go to google!", url="https://google.com.ua")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Привет! Нажми на кнопку и перейди в поисковик.", reply_markup=keyboard)


bot.polling()