import telebot
from telebot import types
import dotenv, os

dotenv.load_dotenv(".env")

token = os.getenv("TOKEN")
bot = telebot.TeleBot(token)

print(bot)
@bot.message_handler()
def url(message):
    bot.send_message(message.from_user.id, message.text)

bot.polling(none_stop=True, interval=0)