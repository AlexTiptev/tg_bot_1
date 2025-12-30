import telebot
from telebot import types
import dotenv, os

dotenv.load_dotenv(".env")

token = os.getenv("TOKEN")
bot = telebot.TeleBot(token)

print(bot)
# @bot.message_handler(commands = ['start'])
# def url(message):
#     # markup = types.InlineKeyboardMarkup()
#     # btn1 = types.InlineKeyboardButton(text='Наш сайт', url='https://habr.com/ru/all/')
#     # markup.add(btn1)
#     bot.send_message(message.from_user.id, "Прив")

bot.polling(none_stop=True, interval=0)