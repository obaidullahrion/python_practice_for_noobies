import telegram
from pytube import YouTube
from telegram.inline.inlinekeyboardmarkup import InlineKeyboardMarkup
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
import os

TOKEN = "7582837514:AAHA0m2xrGdHE6nneOARpc04g9DY-ogzQ9I"
bot = telegram.Bot(token=TOKEN)
updater = Updater(TOKEN)



def progress_function(chunk, file_handle, bytes_remaining , update):
    global filesize
    current = ((filesize - bytes_remaining)/filesize)
    percent = ('{0:.1f}').format(current*100)
    progress = int(50*current)
    status = '█' * progress + '-' * (50 - progress)
    update.message.reply_text(f" ↳ |{status}| {percent}%")

def options(update, context):
    global id
    id = update.message.chat_id
    url = context.args[0]
    update.message.reply_text("Finding formats.Please wait...")

    yt = YouTube(url , on_progress_callback=progress_function)

    global condition1
    global condition2
    global condition3
    global condition4
    global condition5


    formats = []

    global filesize
    condition1 =  yt.streams.filter(progressive=True , res= "720p")
    for i in condition1:
        formats.append("720p")
        filesize = condition1.first().filesize

    
    condition2 =  yt.streams.filter(progressive=True , res= "480p")
    for i in condition2:
        formats.append("480p")



    condition3 =  yt.streams.filter(progressive=True , res= "360p")
    for i in condition3:
        formats.append("360p")

    condition4 =  yt.streams.filter(progressive=True , res= "240p")
    for i in condition4:
        formats.append("240p")


    condition5 =  yt.streams.filter(progressive=True , res= "144p" )
    for i in condition5:
        formats.append("144p")

        
    keyboard = []


    for i in formats:
        keyboard.append([InlineKeyboardButton(text=i,  callback_data=i)])

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Please choose:', reply_markup=reply_markup)




def button_action(update, context):
    
    query = update.callback_query

    query.answer()

    query.edit_message_text(text=f"downlaoding {query.data}")

    if query.data == "720p":
        condition1.first().download(filename='video_send.mp4')

    if query.data == "480p":
        condition2.first().download(filename='video_send.mp4')    


    if query.data == "360p":
        condition3.first().download(filename='video_send.mp4')


    if query.data == "240p":
        condition4.first().download(filename='video_send.mp4')        


    if query.data == "144p":
        condition5.first().download(filename='video_send.mp4')

    bot.send_video(chat_id=id, video=open('video_send.mp4', 'rb'), supports_streaming=True)


    
    if os.path.exists("video_send.mp4"):
        os.remove("video_send.mp4")
    else:
        print("The file does not exist")







updater.dispatcher.add_handler(CommandHandler('yt', options))
updater.dispatcher.add_handler(CallbackQueryHandler(button_action))


updater.start_polling()

updater.idle()