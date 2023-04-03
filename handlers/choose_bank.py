from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext, CallbackQueryHandler

def choose_bank(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    bank = query.data.split(":")[1]
    context.user_data["bank"] = bank

    action = context.user_data["action"]
    currency = context.user_data["currency"]
    amount = context.user_data["amount"]

    # Calculate the amount to be paid and other information

    keyboard = [
        [InlineKeyboardButton("Согласен", callback_data="confirm_order:accept")],
        [InlineKeyboardButton("Назад", callback_data="enter_amount")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_text(
        f"Подтвердите заявку на {'покупку' if action == 'buy' else 'продажу'} {amount} {currency.upper()}:",
        reply_markup=reply_markup,
    )

choose_bank_handler = CallbackQueryHandler(choose_bank, pattern="^choose_bank:")
