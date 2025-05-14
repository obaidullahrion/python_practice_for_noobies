

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext




from pytube import YouTube
from telegram.inline.inlinekeyboardmarkup import InlineKeyboardMarkup
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext




video_url = "https://www.youtube.com/watch?v=RtgoOAn6aT8"
#video_url = input("url:")
yt = YouTube(video_url)


formats = ["one" , "two" , "three"]


def options(update: Update, context: CallbackContext) -> None:
    """Sends a message with three inline buttons attached."""
    keyboard = []


    for i in formats:
        keyboard.append([InlineKeyboardButton(text=i,  callback_data="1")])

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Please choose:', reply_markup=reply_markup)




def button(update: Update, context: CallbackContext) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    query.answer()

    query.edit_message_text(text=f"Selected option: {query.data}")

def main() -> None:
    """Run the bot."""
    
    updater = Updater("1930022408:AAG7b-N8Muu3g_CRnct-d9h9l-RwYmnHLp0")

    updater.dispatcher.add_handler(CommandHandler('yt', options))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))


   
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()