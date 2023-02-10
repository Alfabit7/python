botC = TeleBot(token=TOKEN)
# https://www.youtube.com/watch?v=q9qIPcrC9Mg


@botC.message_handler(commands=['start', 'calculater'])
def FormCalc(message):
    keyboard = types.InlineKeyboardMarkup()
    for i in range(row_col):
        keyboard.row(*[types.InlineKeyboardButton(button24[row_line*i+j],
                     callback_data=button24[row_line*i+j]) for j in range(row_line)])

    botC.send_message(message.from_user.id, 'Hi!', reply_markup=keyboard)

# @botC.callback_query_handler()
# def Print(query):
#     botC.edit_message_text(chat_id=query.messadge.chat.id, message_id=query.message.id, text=, )


botC.infinity_polling()
