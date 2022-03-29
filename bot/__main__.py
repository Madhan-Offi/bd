import time
from datetime import datetime
import pytz
import subprocess

from telegram.ext import CommandHandler
from bot import dispatcher, updater, botStartTime, IMAGE_URL
from bot.helper.telegram_helper.bot_commands import BotCommands
from bot.helper.telegram_helper.message_utils import *
from .helper.telegram_helper.filters import CustomFilters
from .modules import authorize, list


def start(update, context):
    start_string = f"𝗛𝗲𝘆 {uname}👋,\n\n𝗧𝗵𝗮𝗻𝗸 𝗬𝗼𝘂 𝗙𝗼𝗿 𝗦𝘂𝗯𝘀𝗰𝗿𝗶𝗯𝗶𝗻𝗴 𝗺𝗲."
    if CustomFilters.authorized_chat(update):
        update.effective_message.reply_photo(IMAGE_URL, start_string, parse_mode=ParseMode.MARKDOWN, reply_markup=reply_markup)
    else:
        update.effective_message.reply_photo(IMAGE_URL, start_string, parse_mode=ParseMode.MARKDOWN, reply_markup=reply_markup)


def log(update, context):
    sendLogFile(context.bot, update)


botcmds = [(f'{BotCommands.ListCommand}','Search files in My Drive')]


def main():
    bot.set_my_commands(botcmds)
    try:
        kie = datetime.now(pytz.timezone('Asia/Kolkata'))
        jam = kie.strftime('\n📅 𝘿𝘼𝙏𝙀: %d/%m/%Y\n⏲️ 𝙏𝙄𝙈𝙀: %I:%M%P')
        text = f"<b>✨𝐁𝐨𝐭 𝐒𝐭𝐚𝐫𝐭𝐞𝐝✨\n{jam}\n\nᴇᴠᴇʀʏ ᴍᴏᴍᴇɴᴛ ɪs ᴀ ғʀᴇsʜ ʙᴇɢɪɴɴɪɴɢ</b>"
        bot.sendMessage(chat_id=OWNER_ID, text=text, parse_mode=ParseMode.HTML)
        if AUTHORIZED_CHATS:
            for i in AUTHORIZED_CHATS:
                bot.sendMessage(chat_id=i, text=text, parse_mode=ParseMode.HTML)
     except Exception as e:
            LOGGER.warning(e)           

    start_handler = CommandHandler(BotCommands.StartCommand, start, filters=CustomFilters.authorized_chat | CustomFilters.authorized_user, run_async=True)
    log_handler = CommandHandler(BotCommands.LogCommand, log, filters=CustomFilters.owner_filter, run_async=True)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(log_handler)

    updater.start_polling()
    LOGGER.info("𝐁𝐨𝐭 𝐒𝐭𝐚𝐫𝐭𝐞𝐝!")
    updater.idle()

main()
