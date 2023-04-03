# bot.py

from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters

from config import TOKEN
from start import start_handler
from buy_sell import buy_handler, sell_handler, buy_sell_callback_handler
from support import support_handler

def main():
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(buy_handler)
    dispatcher.add_handler(sell_handler)
    dispatcher.add_handler(buy_sell_callback_handler)
    dispatcher.add_handler(support_handler)

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
