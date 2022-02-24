from urllib import response
from telegram.ext import *
import constants as keys
import responses as r

print('Bot started...')


def start_command(update, context):
    update.message.reply_text('Type something')


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = r.sample_response(text)

    update.message.reply_text(response)


def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    updater.start_polling()
    updater.idle()


main()
