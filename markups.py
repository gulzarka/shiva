import telebot
from telebot import types


bot = telebot.TeleBot('6217841760:AAEaXQ0Vs3N8Yw8v4ZOmIBrNT7DqhD-AXFE')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot_command = types.BotCommand('start', 'start page')
    command_scope = types.BotCommandScopeChat(message.chat.id)
    bot.set_my_commands([bot_command], command_scope)
    button2 = types.InlineKeyboardButton('Я-заказчик', callback_data='customer')
    button3 = types.InlineKeyboardButton('Я-подрядчик', callback_data='executer')
    markup = types.InlineKeyboardMarkup()
    markup.add(button2, button3)
    bot.send_message(message.chat.id,
                     reply_markup=markup,
                     text='Добро пожаловать в сервис "Shiva"! Для продолжения выберите пожалуйста ваш статус')


@bot.callback_query_handler(func=lambda call: call.data == "customer")
def customer(call: types.CallbackQuery):
    bot.send_message(call.message.chat.id, text="Hi customer")


@bot.callback_query_handler(func=lambda call: call.data == "executer")
def executer(call: types.CallbackQuery):
    button = types.InlineKeyboardButton('choose', callback_data='client')
    markup = types.InlineKeyboardMarkup()
    markup.add(button)
    bot.send_message(call.message.chat.id, reply_markup=markup, text='AAA!')


bot.infinity_polling()
