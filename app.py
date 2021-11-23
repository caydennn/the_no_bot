# import everything
import os
from dotenv import load_dotenv
from os.path import join, dirname
from flask import Flask, request
import random

from bot_logic import responses
import telegram
import json


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

global bot
TOKEN = os.environ.get("TOKEN")
bot = telegram.Bot(token=TOKEN)

URL = os.environ.get("URL")


# start the flask app
app = Flask(__name__)


@app.route('/{}'.format(TOKEN), methods=['POST'])
def respond():
   # retrieve the message in JSON and then transform it to Telegram object

    update = telegram.Update.de_json(request.get_json(force=True), bot)

    if update.message == None:
        raw_data = request.get_json(force=True)
        chat_id = 80749729
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump((raw_data), f, ensure_ascii=False, indent=4)
        bot.sendMessage(chat_id=chat_id,
                        text=request.get_json(force=True)['id'])
        bot.sendDocument(chat_id=chat_id, document=open('data.json', 'rb'))
        return 'no message'

    user = update.message.from_user
    user = user['username'].lower()

    text = ''
    if update.message.text != None:
        # Telegram understands UTF-8, so encode text for unicode compatibility
        text = update.message.text.encode('utf-8').decode()

        # for debugging purposes only
        print("Got text message :", text)
        print("From: ", user)

    # just to check bot status
    if text == "/start":

        bot_welcome = """
			The No Bot is alive :)
		"""

        bot.sendMessage(chat_id=chat_id, text=bot_welcome,
                        reply_to_message_id=msg_id)

        return 'ok'

    if text == '/testAudio':
        bot.sendAudio(chat_id=chat_id, audio=open(
            'assets/audio/felice.wav', 'rb'), title='felice: えっと、、私の友達は君のことが本当に好きなので')
        return 'ok'

    # Random Speaking Chance
    percentage_chance = 0.15
    random_number = random.random()

    print("Bot Speaks if < {} : {}".format(percentage_chance, random_number))
    if random_number <= percentage_chance:
        if user == "feliceho":
            responses.feliceResponses(update, bot)

        if user == "folkloreee":
            responses.filbertResponses(update)

        if user == "joeloooooong":
            responses.joelResponses(update)

        if user == "yongta":
            responses.ytResponses(update)

        if user == "nicolefranc":
            responses.nicoleResponses(update)

    #    else:
    #        try:
    #            # clear the message we got from any non alphabets
    #            text = re.sub(r"\W", "_", text)
    #            # create the api link for the avatar based on http://avatars.adorable.io/
    #            url = "https://api.adorable.io/avatars/285/{}.png".format(text.strip())
    #            # reply with a photo to the name the user sent,
    #            # note that you can send photos by url and telegram will fetch it for you
    #            bot.sendPhoto(chat_id=chat_id, photo=url, reply_to_message_id=msg_id)
    #        except Exception:
    #            # if things went wrong
    #            bot.sendMessage(chat_id=chat_id, text="There was a problem in the name you used, please enter different name", reply_to_message_id=msg_id)

    return 'ok'


@app.route('/setwebhook', methods=['GET', 'POST'])
def set_webhook():
    # we use the bot object to link the bot to our app which live
    # in the link provided by URL

    # For development, use ngrok to port forward flask app
    if (os.environ.get('MODE') == 'dev'):  # Add MODE=dev in your .env
        # Run ngrok and add it to DEV_URL in your .env
        DEV_URL = os.environ.get("DEV_URL")
        print("In production mode... Setting to: {}".format(DEV_URL))
        s = bot.setWebhook('{DEV_URL}{HOOK}'.format(
            DEV_URL=DEV_URL, HOOK=TOKEN))
    else:
        s = bot.setWebhook('{URL}{HOOK}'.format(URL=URL, HOOK=TOKEN))
    # something to let us know things work
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"


@app.route('/')
def index():
    return '.'


if __name__ == '__main__':
    # note the threaded arg which allow
    # your app to have more than one thread
    app.run(threaded=True)
