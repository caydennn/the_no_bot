import logging
import json
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import os
from dotenv import load_dotenv
from os.path import join, dirname
import uwuify
import random

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def increaseCount(currentCount):
    currentCount += 1

    updatedData = {'count': currentCount}

    with open('data.json', 'w') as json_file:
        json.dump(updatedData, json_file)
        print("data updated with {}".format(updatedData))

    return


def say_stuff(update: Update, context: CallbackContext) -> None:

    with open('data.json') as f:
        data = json.load(f)
        currentCount = data['count']
        print(data)

    """Echo the user message."""

    try:
        user = update.message.from_user

     except Exception as e:
        print("Error:")
        print(e)
        increaseCount[currentCount]
        return
    

    if (user['username'].lower() == "folkloreee"):
        increaseCount(currentCount)

        if (currentCount % 5 == 0):
            print("filbert sent the msg")
            update.message.reply_text("No")

    if (user['username'].lower() == "feliceho"):
        increaseCount(currentCount)

        if (currentCount % 5 == 0):
            uwuMessage = uwuify.uwu(update.message.text)
            update.message.reply_text(uwuMessage)

    if (user['username'].lower() == "Joeloooooong"):
        increaseCount(currentCount)

        if (currentCount % 5 == 0):
            update.message.reply_text("YASS KINGGGG")

    if (user['username'].lower() == "nicolefranc"):
        increaseCount(currentCount)

        if (currentCount % 5 == 0):
            update.message.reply_text("neRD sIA")

    if (user['username'].lower() == "yongta"):
        increaseCount(currentCount)

        if (currentCount % 5 == 0):
            choices = ['lunch?', 'DINNer', 'SUPPPERR?']
            update.message.reply_text(random.choice(choices))
    # if (user['username'].lower() == "ohyamn"):
    #     increaseCount(currentCount)

    #     if (currentCount % 5 == 0):
    #         print("yanlin sent the msg")
    #         update.message.reply_text("hi yanlin")

    # if (user['username'].lower() == "yongta"):
    #     increaseCount(currentCount)

    #     if (currentCount % 5 == 0):
    #         print("yt sent the msg")
    #         update.message.reply_text("hi yt")


def main():
    count = 0
    TELEGRAM_TOKEN = os.environ.get("TOKEN")
    print(TELEGRAM_TOKEN)
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(TELEGRAM_TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on noncommand i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(
        Filters.text & ~Filters.command, say_stuff))

    print("Starting...")

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
