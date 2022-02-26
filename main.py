from telegram.ext import *
import responses
# from decouple import config

# API_KEY = config('API_KEY')
API_KEY = '5158894773:AAEXv5EDzOdpLoxv4xHaieVodp2oZa4-kz4'

print('Bot started...')


def start_command(update, context):
    update.message.reply_text(
        'This bot searches what you type on Wikipedia and returns the first lines of the page')


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
