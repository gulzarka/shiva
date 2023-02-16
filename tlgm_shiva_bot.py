import logging
import telebot
from environs import Env
from telebot import types

logger = logging.getLogger(__file__)


def main():
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )

    env = Env()
    env.read_env()
    tlgm_bot_token = env('TLGM_BOT_TOKEN')
    bot = telebot.TeleBot(tlgm_bot_token)


    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot_command = types.BotCommand('start', 'start page')
        command_scope = types.BotCommandScopeChat(message.chat.id)
        bot.set_my_commands([bot_command], command_scope)
        button1 = types.InlineKeyboardButton(
            'Я-клиент',
            callback_data='client',
        )
        button2 = types.InlineKeyboardButton(
            'Я-подрядчик',
            callback_data='executer',
        )
        markup = types.InlineKeyboardMarkup()
        markup.add(button1, button2)
        bot.send_message(
            message.chat.id,
            reply_markup=markup,
            text='Добро пожаловать в сервис "Shiva"! Для продолжения выберите'
                 'пожалуйста ваш статус'
        )


    @bot.callback_query_handler(func=lambda call: call.data == "client")
    def client(call: types.CallbackQuery):
        bot.send_message(call.message.chat.id, text='Hi client!')


    @bot.callback_query_handler(func=lambda call: call.data == "customer")
    def customer(call: types.CallbackQuery):
        bot.send_message(call.message.chat.id, text="Hi customer")


    @bot.callback_query_handler(func=lambda call: call.data == "executer")
    def executer(call: types.CallbackQuery):
        button = types.InlineKeyboardButton('choose', callback_data='client')
        markup = types.InlineKeyboardMarkup()
        markup.add(button)
        bot.send_message(
            call.message.chat.id,
            reply_markup=markup,
            text='AAA!'
        )

    bot.infinity_polling()


if __name__ == '__main__':
    main()
