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
    percentage_chance = 0.25

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

    random_number = random.random()
    print("Bot Speaks if < {} : {}".format(percentage_chance, random_number))
    if random_number <= percentage_chance:

        if (user['username'].lower() == "folkloreee"):
            increaseCount(currentCount)
            update.message.reply_text("No")

        if (user['username'].lower() == "feliceho"):
            increaseCount(currentCount)
            uwuMessage = uwuify.uwu(update.message.text)
            if (uwuMessage != update.message.text):
                update.message.reply_text(uwuMessage)

        if (user['username'].lower() == "joeloooooong"):
            increaseCount(currentCount)
            update.message.reply_text("YASS KINGGGG")

        if (user['username'].lower() == "nicolefranc"):
            increaseCount(currentCount)
            update.message.reply_text("neRD sIA")

        if (user['username'].lower() == "yongta"):
            increaseCount(currentCount)
            # choices = ['lunch?', 'DINNer', 'SUPPPERR?']
            # update.message.reply_text(random.choice(choices))
            update.message.reply_text("oCay-den")


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
