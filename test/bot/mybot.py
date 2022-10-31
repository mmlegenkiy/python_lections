import telebot

bot = telebot.TeleBot('5297760495:AAHxzRB93VylGzK-MdlKkCNQdeI6YPe9X20')

@bot.message_handler(commands=['start'])
def start(message):
    msg = "Я пробил информацию:\n"
    msg += "\n"
    msg += "Id чата: "+str(message.chat.id)+"\n"
    msg += "Id пользователя: " +str(message.from_user.id)+"\n"
    msg += "Имя: " + str(message.from_user.first_name)+"\n"
    msg += "Фамилия: " + str(message.from_user.last_name)+"\n"
    msg += "Псевдоним: " + str(message.from_user.username)+"\n"
    msg += "\n"
    msg += "Текст сообщения: " + str(message.text)
    bot.send_message(message.chat.id, msg)

bot.polling()