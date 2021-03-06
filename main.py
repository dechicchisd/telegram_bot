from telegram.ext import *
import responses
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')

print('Bot started...')


def start_command(update, context):
    update.message.reply_text(
        'This bot searches on Wikipedia what you type and returns the first lines of the page')


def handle_message(update, context):
    text = str(update.message.text)

    update.message.reply_text(responses.search_wiki(text))


def main():
    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    updater.start_polling()
    updater.idle()


main()
