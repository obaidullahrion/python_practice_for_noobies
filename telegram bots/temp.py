import telegram

TELEGRAM_BOT_TOKEN = '1930022408:AAG7b-N8Muu3g_CRnct-d9h9l-RwYmnHLp0'
TELEGRAM_CHAT_ID = '1226579179'
PHOTO_PATH = 'screenshot.png'

bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)

bot.send_message(chat_id=TELEGRAM_CHAT_ID, text="From Telegram Bot")

bot.send_photo(chat_id=TELEGRAM_CHAT_ID, photo=open(PHOTO_PATH, 'rb'))