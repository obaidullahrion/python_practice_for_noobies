from telegram import Bot, Update, InputFile
from telegram.ext import Updater, CommandHandler, CallbackContext

def send_message(update: Update, context: CallbackContext) -> None:
    chat_id = context.args[0]
    message = context.args[1]
    
    bot = Bot(token='7064620974:AAE8J9Xy6y6AfOA0X9SfWIhuPysm_MDvUno')
    bot.send_message(chat_id=chat_id, text=message)

def main() -> None:
    updater = Updater("7064620974:AAE8J9Xy6y6AfOA0X9SfWIhuPysm_MDvUno", use_context=True)

    dispatcher = updater.dispatcher

    send_message_handler = CommandHandler('send', send_message)

    dispatcher.add_handler(send_message_handler)

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()