from typing import Text
import telegram
from telegram.ext import Updater , CommandHandler, MessageHandler 
import logging
import requests
import re
import time

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
bot = telegram.Bot(token="1930022408:AAG7b-N8Muu3g_CRnct-d9h9l-RwYmnHLp0")
updater = Updater(token= "1930022408:AAG7b-N8Muu3g_CRnct-d9h9l-RwYmnHLp0",use_context=True )
dispatcher = updater.dispatcher


def start(update , context):
    msg = update.message.reply_text("hi whats up?")
    time.sleep(5)
    bot.edit_message_text(chat_id=update.message.chat_id, 
                          message_id=msg.message_id,
                          text="Seriously, you're on your own, kiddo.")

def help(update , context):
    update.message.reply_text("helping w8")

def attack(update , context):
    zero = context.args[0]
    if zero == "pybot":
        update.message.reply_text("how can i attack myself?")
    else:
        update.message.reply_text(f"atttacking process . target is{zero}")


def mssg_handler(update,context):
    update.message.reply_text(f"you just said {update.message.text}")

def exit(update , context):
    updater.stop()
    updater.message.reply_text("bot stopped")




def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url


def photo(bot, update):
    url = get_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)



    


start_handler = CommandHandler('start', start)
attack_handler = CommandHandler('attack', attack)
help_handler = CommandHandler('help' , help)
messagehandler = MessageHandler(telegram.ext.Filters.text , mssg_handler)
exit_handler = CommandHandler('stop' , exit)
photo_handler = CommandHandler('photo' , photo)




dispatcher.add_handler(start_handler)
dispatcher.add_handler(attack_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(exit_handler)
dispatcher.add_handler(photo_handler)



updater.start_polling()
updater.idle
