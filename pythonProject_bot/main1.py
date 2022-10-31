# t.me/karazin261022_bot
# Use this token to access the HTTP API:
# 5585935997:AAF6xpx25ki9NxWXUtbRXp6k79GcPnRAYlQ
# /setinline Hint

import telebot
from telebot import types
import re

token = '5585935997:AAF6xpx25ki9NxWXUtbRXp6k79GcPnRAYlQ'
bot = telebot.TeleBot(token)
# morze = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
#          'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
#          'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
#          'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
#          'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
#          'z': '--..', '1': '.----', '2': '..---', '3': '...--',
#          '4': '....-', '5': '.....', '6': '-....', '7': '--...',
#          '8': '---..', '9': '----.', '0': '-----'}

digits_pattern = re.compile(r'^[0-9]+ [0-9]+$', re.MULTILINE)


@bot.inline_handler(func=lambda query: len(query.query) == 0)
def empty_query(query):
    # hint = "Введите ровно 2 числа и получите результат!"
    hint = "Input two numbers!"
    try:
        r = types.InlineQueryResultArticle(
                id='1',
                title="Math-bot",
                description=hint,
                input_message_content=types.InputTextMessageContent(
                message_text="Should be two numbers")  # Эх, зря я не ввёл 2 числа :(
        )
        bot.answer_inline_query(query.id, [r])
    except Exception as e:
        print(e)


@bot.inline_handler(func=lambda query: len(query.query) > 0)
def query_text(query):
    try:
        matches = re.match(digits_pattern, query.query)
    except AttributeError as ex:
        return
    # print(matches)
    # print(type(matches))
    if matches is None:
        return
    num1, num2 = matches.group().split()
    try:
        m_sum = int(num1) + int(num2)
        r_sum = types.InlineQueryResultArticle(
                id='1', title="Sum",
                # Описание отображается в подсказке,
                # message_text - то, что будет отправлено в виде сообщения
                description="Result: {!s}".format(m_sum),
                input_message_content=types.InputTextMessageContent(
                message_text="{!s} + {!s} = {!s}".format(num1, num2, m_sum)))
                # # Указываем ссылку на превью и его размеры
                # thumb_url=plus_icon, thumb_width=48, thumb_height=48
        # )
        # m_sub = int(num1) - int(num2)
        # r_sub = types.InlineQueryResultArticle(
        #         id='2', title="Разность",
        #         description="Результат: {!s}".format(m_sub),
        #         input_message_content=types.InputTextMessageContent(
        #         message_text="{!s} - {!s} = {!s}".format(num1, num2, m_sub))
        #         # thumb_url=minus_icon, thumb_width=48, thumb_height=48
        # )
        # # Учтем деление на ноль и подготовим 2 варианта развития событий
        # if num2 != "0":
        #     m_div = int(num1) / int(num2)
        #     r_div = types.InlineQueryResultArticle(
        #             id='3', title="Частное",
        #             description="Результат: {0:.2f}".format(m_div),
        #             input_message_content=types.InputTextMessageContent(
        #             message_text="{0!s} / {1!s} = {2:.2f}".format(num1, num2, m_div))
        #             # thumb_url=divide_icon, thumb_width=48, thumb_height=48
        #     )
        # else:
        #     r_div = types.InlineQueryResultArticle(
        #             id='3', title="Частное", description="На ноль делить нельзя!",
        #             input_message_content=types.InputTextMessageContent(
        #             message_text="Я нехороший человек и делю на ноль!")
        #             # thumb_url=error_icon, thumb_width=48, thumb_height=48,
        #             # # Сделаем превью кликабельным, по нажатию юзера направят по ссылке
        #             # url="https://ru.wikipedia.org/wiki/%D0%94%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5_%D0%BD%D0%B0_%D0%BD%D0%BE%D0%BB%D1%8C",
        #             # disable_web_page_preview=True,
        #             # # Не будем показывать URL в подсказке
        #             # hide_url=True
        #     )
        # m_mul = int(num1) * int(num2)
        # r_mul = types.InlineQueryResultArticle(
        #         id='4', title="Произведение",
        #         description="Результат: {!s}".format(m_mul),
        #         input_message_content=types.InputTextMessageContent(
        #         message_text="{!s} * {!s} = {!s}".format(num1, num2, m_mul))
        #         # thumb_url=multiply_icon, thumb_width=48, thumb_height=48
        # )
        # В нашем случае, результаты вычислений не изменятся даже через долгие годы, НО!
        # если где-то допущена ошибка и cache_time уже выставлен большим, то это уже никак не исправить (наверное)
        # Для справки: 2147483646 секунд - это 68 с копейками лет :)
        # bot.answer_inline_query(query.id, [r_sum, r_sub, r_div, r_mul], cache_time=2147483646)
        bot.answer_inline_query(query.id, [r_sum], cache_time=2147483646)
    except Exception as e:
        print("{!s}\n{!s}".format(type(e), str(e)))


bot.polling()
