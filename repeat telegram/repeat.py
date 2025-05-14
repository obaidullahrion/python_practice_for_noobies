import telegram
from telegram.ext import Updater ,CommandHandler,  MessageHandler


updater = Updater("7064620974:AAE8J9Xy6y6AfOA0X9SfWIhuPysm_MDvUno" , use_context=True)
dispatcher = updater.dispatcher

def messg_handler(update , context):
    update.message.reply_text(f"😛 {update.message.text} 😛🤪")

def start(update , context):
    update.message.reply_text("I'm alive")



dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(MessageHandler(telegram.ext.Filters.text , messg_handler))

updater.start_polling()
updater.idle



