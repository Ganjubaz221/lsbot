from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext, MessageHandler, Filters

def enter_amount(update: Update, context: CallbackContext):
    amount = update.message.text.replace(',', '.')
    try:
        amount = float(amount)
    except ValueError:
        update.message.reply_text("Неверный формат числа. Пожалуйста, попробуйте еще раз.")
        return

    context.user_data["amount"] = amount

    keyboard = [
        [InlineKeyboardButton("Банк 1", callback_data="choose_bank:bank1")],
        [InlineKeyboardButton("Банк 2", callback_data="choose_bank:bank2")],
        [InlineKeyboardButton("Назад", callback_data="buy_sell")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(
        "Выберите банк для оплаты:",
        reply_markup=reply_markup,
    )

enter_amount_handler = MessageHandler(Filters.text & ~Filters.command, enter_amount)
