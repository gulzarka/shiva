import logging
import telebot
from environs import Env

logger = logging.getLogger(__file__)


def main():
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )

    env = Env()
    env.read_env()
    tlgm_bot_token = env('TLGM_BOT_TOKEN')

    logger.setLevel(logging.INFO)

    bot = telebot.TeleBot(tlgm_bot_token)

    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, "Привет! Кто ты клиент или подрядчик?")

    bot.infinity_polling()


if __name__ == '__main__':
    main()
