from telegram import Update
from telegram.ext import CallbackContext, CommandHandler

def buy_sell(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    action = query.data.split(":")[1]

    keyboard = [
        [
            InlineKeyboardButton("Купить BTC", callback_data=f"choose_currency:{action}:btc"),
            InlineKeyboardButton("Купить USDT", callback_data=f"choose_currency:{action}:usdt"),
        ],
        [InlineKeyboardButton("Назад", callback_data="start")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_text(
        "Выберите тип криптовалюты:",
        reply_markup=reply_markup,
    )

buy_sell_handler = CallbackQueryHandler(buy_sell, pattern="^buy_sell:")
