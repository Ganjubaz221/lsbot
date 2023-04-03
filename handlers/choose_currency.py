from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext, CallbackQueryHandler

def choose_currency(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    action, currency = query.data.split(":")[1:]
    context.user_data["action"] = action
    context.user_data["currency"] = currency

    query.edit_message_text(
        f"Введите сумму {'покупки' if action == 'buy' else 'продажи'} {currency.upper()}:"
    )
    # Move to the next step (enter_amount)

choose_currency_handler = CallbackQueryHandler(choose_currency, pattern="^choose_currency:")
