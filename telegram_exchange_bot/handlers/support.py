# support.py

from telegram import Update
from telegram.ext import CallbackContext, CommandHandler

def support(update: Update, context: CallbackContext):
    support_message = "Если у вас возникли проблемы или вопросы, пожалуйста, свяжитесь с нашей службой поддержки по адресу: support@example.com"
    update.message.reply_text(support_message)

support_handler = CommandHandler("support", support)
