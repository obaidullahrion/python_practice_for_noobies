from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


def hello(update, context):
    print(update)
    update.message.reply_text(f'Hello {update.message.from_user.first_name}')


updater = Updater('1930022408:AAG7b-N8Muu3g_CRnct-d9h9l-RwYmnHLp0' , use_context = True)

updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()