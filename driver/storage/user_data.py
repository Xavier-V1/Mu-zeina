""" user data """

import config
import logging
import datetime

from driver.storage.database import Database

DB_URL = config.MONGODB_URL
DB_NAME = config.MONGODB_NAME
LOG_CHANNEL = config.LOG_CHATID

db = Database(DB_URL, DB_NAME)

async def handle_user_status(bot, cmd):
    chat_id = cmd.from_user.id
    if not await db.is_user_exist(chat_id):
        data = await bot.get_me()
        BOT_USERNAME = data.username
        await db.add_user(chat_id)
        if LOG_CHANNEL:
            await bot.send_message(
                LOG_CHANNEL,
                f"#NEW_USER:\n\n📮: [{cmd.from_user.first_name}](tg://user?id={cmd.from_user.id})\nstarted @{BOT_USERNAME} !",
            )
        else:
            logging.info(f"#NEW - Name: {cmd.from_user.first_name} ID: {cmd.from_user.id}")

    ban_status = await db.get_ban_status(chat_id)
    if ban_status["is_banned"]:
        if (
            datetime.date.today() - datetime.date.fromisoformat(ban_status["banned_on"])
        ).days > ban_status["ban_duration"]:
            await db.remove_ban(chat_id)
        else:
            await cmd.reply_text("You're banned for using this bot", quote=True)
            return
    await cmd.continue_propagation()
