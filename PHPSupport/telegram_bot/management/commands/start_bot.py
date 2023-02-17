from django.core.management import BaseCommand
import logging
import telebot
from environs import Env
from telebot import types
from telegram_bot.crud import is_user_client, is_user_subcontractor


logger = logging.getLogger(__file__)


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            start_bot()
        except Exception as exc:
            logger.debug(exc)
            raise


def start_bot():

    env = Env()
    env.read_env()
    tlgm_bot_token = env('TLGM_BOT_TOKEN')
    bot = telebot.TeleBot(tlgm_bot_token)
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )

    @bot.message_handler(commands=['start'])
    def check_user(message):
        bot_command = types.BotCommand('start', 'start page')
        command_scope = types.BotCommandScopeChat(message.chat.id)
        bot.set_my_commands([bot_command], command_scope)
        if is_user_client(message.from_user.id):
            bot.send_message(message.chat.id, text='Вы клиент!')
            return
        elif is_user_subcontractor(message.from_user.id):
            bot.send_message(message.chat.id, text='Вы контрактор!')
            return
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
        bot.answer_callback_query(callback_query_id=call.id)
        bot.send_message(call.message.chat.id, text="Зарегистрировать вас как клиента?")

    @bot.callback_query_handler(func=lambda call: call.data == "executer")
    def executer(call: types.CallbackQuery):
        button = types.InlineKeyboardButton('choose', callback_data='client')
        markup = types.InlineKeyboardMarkup()
        markup.add(button)
        bot.send_message(
            call.message.chat.id,
            reply_markup=markup,
            text='Зарегистрировать вас как исполнителя?'
        )

    bot.infinity_polling()
