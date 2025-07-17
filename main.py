
from flask import Flask
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from PIL import Image
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Veteriner Bot is running!"

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Merhaba! Veteriner botuna hoş geldiniz.')

def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

def run_telegram_bot():
    TOKEN = os.getenv("BOT_TOKEN")
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    updater.start_polling()

if __name__ == '__main__':
    run_telegram_bot()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
