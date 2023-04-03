from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext, CallbackQueryHandler

def confirm_order(update: Update, context: Callback Context):

query = update.callback_query
query.answer()

choice = query.data.split(":")[1]

if choice == "accept":
    # Save order details and send them to the operator
    # You need to implement the appropriate functions to save and send order details to the operator

    query.edit_message_text(
        "Заявка принята. Ожидайте подтверждения оператора в течение 2-3 минут."
    )
else:
    # Go back to the previous step (choose_bank)
    query.edit_message_reply_markup(None)
    context.bot.send_message(
        chat_id=query.message.chat_id,
        text="Выберите банк для оплаты:",
        reply_markup=choose_bank_keyboard(),
    )

def choose_bank_keyboard():
keyboard = [
[InlineKeyboardButton("Банк 1", callback_data="choose_bank:bank1")],
[InlineKeyboardButton("Банк 2", callback_data="choose_bank:bank2")],
[InlineKeyboardButton("Назад", callback_data="buy_sell")],
]

return InlineKeyboardMarkup(keyboard)

confirm_order_handler = CallbackQueryHandler(confirm_order, pattern="^confirm_order:")