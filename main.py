import logging  # Para ver que esta haciendo el bot
import telegram
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s,")

logger = logging.getLogger()

TOKEN = "5820768310:AAH5idM3TIfen4fkKsL41mZjDmT5Pr8Jolg"


def start(update, context):
    username = update.message.from_user.username
    first_name = update.message.from_user.first_name
    chat_id = update.message.from_user.id
    logger.info(f"Usuario {username} ha iniciado el bot")
    update.message.reply_text(
        text=f'Hola wenas señor {username}!',
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(
                text="About Me", url="https://etecsa.cu")]
        ])
    )


if __name__ == "__main__":
    myBot = telegram.Bot(token=TOKEN)

    # Updater se conecta y recibe los mensajes
updater = Updater(myBot.token, use_context=True)

# Create dispatcher
dp = updater.dispatcher

# Create command
dp.add_handler(CommandHandler("start", start))

updater.start_polling()

updater.idle()
