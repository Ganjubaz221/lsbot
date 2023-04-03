from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext, CommandHandler

def start(update: Update, context: CallbackContext):
    keyboard = [
        [
            InlineKeyboardButton("Купить", callback_data="buy_sell:buy"),
            InlineKeyboardButton("Продать", callback_data="buy_sell:sell"),
        ],
        [InlineKeyboardButton("Поддержка", callback_data="support")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(
        "Добро пожаловать! Выберите действие:",
        reply_markup=reply_markup,
    )

start_handler = CommandHandler("start", start)
