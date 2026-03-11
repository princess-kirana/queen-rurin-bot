import telebot
import os

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Halo! Aku Queen Rurin Bot 👑\nKirim link video untuk didownload.")

bot.infinity_polling()
