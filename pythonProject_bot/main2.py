# t.me/karazin261022_bot
# Use this token to access the HTTP API:
# 5585935997:AAF6xpx25ki9NxWXUtbRXp6k79GcPnRAYlQ
# /setinline Hint

import telebot
from telebot import types
# import re

token = '5585935997:AAF6xpx25ki9NxWXUtbRXp6k79GcPnRAYlQ'
bot = telebot.TeleBot(token)
morze = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
         'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
         'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
         'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
         'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
         'z': '--..', '1': '.----', '2': '..---', '3': '...--',
         '4': '....-', '5': '.....', '6': '-....', '7': '--...',
         '8': '---..', '9': '----.', '0': '-----', ' ': ' '}

# digits_pattern = re.compile(r'^[0-9]+ [0-9]+$', re.MULTILINE)


@bot.inline_handler(func=lambda query: len(query.query) == 0)
def empty_query(query):
    hint = "Input letters or numbers!"
    try:
        r = types.InlineQueryResultArticle(
                id='1',
                title="Morze-bot",
                description=hint,
                input_message_content=types.InputTextMessageContent(message_text="Should be letters or numbers"))
        bot.answer_inline_query(query.id, [r])
    except Exception as e:
        print(e)


@bot.inline_handler(func=lambda query: len(query.query) > 0)
def query_text(query):
    str = ''
    for x in query.query:
        try:
            str += morze[x]
            str += ' '
        except KeyError as ex:
            return
    res = types.InlineQueryResultArticle(
                id='1', title="Morze code",
                description="Result: {!s}".format(str),
                input_message_content=types.InputTextMessageContent(message_text="{!s}".format(str)))
    bot.answer_inline_query(query.id, [res], cache_time=2147483646)


bot.polling()
