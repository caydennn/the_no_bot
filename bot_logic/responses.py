
def feliceResponses(update, bot):
    chat_id = update.message.chat.id
    # update.message.reply_text("えっと、、私の友達は君のことが本当に好きなので")
    # bot.sendAudio(chat_id=chat_id, audio=open('assets/audio/felice.wav', 'rb') , title='felice: えっと、、私の友達は君のことが本当に好きなので')
    update.message.reply_text("Yesuuuu :>")
    return 'ok'


def filbertResponses(update):
    update.message.reply_text("no.")
    return 'ok'

def joelResponses(update):
    update.message.reply_text("YASS KINGGGG")
    return 'ok'


def ytResponses(update):
    update.message.reply_text("yes president 💦")
    return 'ok'


def nicoleResponses(update):
    update.message.reply_text("neRD sIA")
    return 'ok'
