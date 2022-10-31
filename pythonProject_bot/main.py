import telebot
import os
import time
import random
from telebot import types


def generate_markup(answers):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    random.shuffle(answers)
    for item in answers:
        markup.add(item)
    return markup


API_TOKEN = '5297760495:AAHxzRB93VylGzK-MdlKkCNQdeI6YPe9X20'
bot = telebot.TeleBot(API_TOKEN)
audios = {'AwACAgIAAxkDAAIPK2NasdDqvSrvRPEbtSP-riscOlWpAAInIAACTzfQSnBAJg29MrpNKgQ': 'Game of thrones',
          'AwACAgIAAxkDAAIPLWNasdR1ZzH1buFAf2FKyhOl4rRhAAIpIAACTzfQSqD0lgWO9LZVKgQ': 'Terminator',
          'AwACAgIAAxkDAAIPL2NasdgTuYyx9d0xDsyRpokIhtiGAAIqIAACTzfQSlus2A-1PmhPKgQ': 'Rocky',
          'AwACAgIAAxkDAAIPMWNasdvsVs9VkP8tj-iVwj6avfVTAAIrIAACTzfQSpCqQFdVvWFHKgQ': 'Indiana Jones',
          'AwACAgIAAxkDAAIPM2Nasd8Re334GFD79FljivzAiBETAAIsIAACTzfQSvGNTvUIsCU9KgQ': 'Pirates of the Caribbean',
          'AwACAgIAAxkDAAIPNWNaseMt5qf-Afcu8uKJqbfVk1DYAAItIAACTzfQSp1EFeeWVxtdKgQ': 'Star Wars'}
users = dict()


@bot.message_handler(commands=['start'])
def start(message):
    msg = "Chat ID: " + str(message.chat.id) + "\n"
    msg += "Name: " + str(message.from_user.first_name) + "\n"
    msg += "Surname: " + str(message.from_user.last_name) + "\n"
    msg += "Username: " + str(message.from_user.username) + "\n"
    msg += "\n"
    msg += "Message: " + str(message.text)
    bot.send_message(message.chat.id, msg)


@bot.message_handler(commands=['test'])
def find_file_ids(message):
    for file in os.listdir('sounds/'):
        if file.split('.')[-1] == 'ogg':
            f = open('sounds/'+file, 'rb')
            msg = bot.send_voice(message.chat.id, f, None)
            bot.send_message(message.chat.id, msg.voice.file_id, reply_to_message_id=msg.message_id)
        time.sleep(3)


@bot.message_handler(commands=['game'])
def game(message):
    markup = generate_markup(list(audios.values()))
    file_id = random.choice(list(audios))
    bot.send_voice(message.chat.id, file_id, reply_markup=markup)
    users[message.chat.id] = audios[file_id]


@bot.message_handler(func=lambda message: True, content_types=['text'])
def check_answer(message):
    if message.chat.id in users:
        keyboard_hider = types.ReplyKeyboardRemove()
        answer = users[message.chat.id]
        if message.text == answer:
            msg = 'Congratulations! Your answer is correct!'
        else:
            msg = 'Your answer is not correct. Try again!'
        bot.send_message(message.chat.id, msg, reply_markup=keyboard_hider)
        users.pop(message.chat.id)
    else:
        msg = 'To start the game use command /game'
        bot.send_message(message.chat.id, msg)


bot.polling()
