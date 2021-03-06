from datetime import datetime
from sys import version_info
from time import time

from config import (
    ALIVE_IMG,
    ALIVE_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)
from program import __version__
from driver.veez import user
from driver.filters import command, other_filters
from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""{message.from_user.mention()} ๐ฎโ ูุฑุญุจุง ุจู ุนุฒูุฒู\n
๐งโุงูุง ุจูุช ุชุดุบูู ุงููุฏูู ู ุงูููุณููู ูู ุงูุฏุฑุฏุดุงุช ุงูุตูุชูู.

๐ฅโุงุณุชุทูุน ุงูุถุง ุงูุชุญูู ูู ุงูููุชููุจ ูุฏูู ุงู ุตูุช ุจุฌููุน ุงูุฏูู.

๐ฎโููุนุฑูู ููููู ุชุดุบููู ูู ูุฌููุนุชู ุงุถุบุท ุนูู ุฒุฑ ุงูุงูุฑ ุงูุจูุช ุจุงูุงุณูู ููู ุงุนุฑุถ ูู ุฌููุน ุงูุงูุงูุฑ.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "- ุงุถู ุงูุจูุช ุงูู ูุฌููุนุชู",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("- ุทุฑููู ุชุดุบูู ุงูุจูุช", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("- ุงูุงูุงูุฑ", callback_data="cbcmds"),
                    InlineKeyboardButton("- ุงููุทูุฑ", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "- ุฌุฑูุจ ุงูุฏุนู", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "- ููุงู ุงูุจูุช", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "- ูู ุนุงูุฒ ุชูุตุจ ุจูุช", url="https://github.com/levina-lab/video-stream"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_message(
    command(["alive", f"alive@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def alive(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("โจ ุฌุฑูุจ ุงูุฏุนู", url=f"https://t.me/{GROUP_SUPPORT}"),
                InlineKeyboardButton(
                    "๐ฃ ููุงู ุงูุจูุช", url=f"https://t.me/{UPDATES_CHANNEL}"
                ),
            ]
        ]
    )

    alive = f"ูุฑุญุจูุง {message.from_user.mention ()} ุ ุฃูุง {BOT_NAME} \n \nโจ ูุนูู ุงูุจูุช ุจุดูู ุทุจูุนู \n๐ ุฑุฆูุณู: [{ALIVE_NAME}] (https://t.me/ {OWNER_NAME}) \nโจ ุฅุตุฏุงุฑ Bot: v\{__version__} n๐ ุฅุตุฏุงุฑ Pyrogram {pyrover} \nโจ ุฅุตุฏุงุฑ Python: {__python_version__} \n๐ ุฅุตุฏุงุฑ PyTgCalls: {pytover.__version__} \nโจ ุญุงูุฉ ููุช ุงูุชุดุบูู: {uptime} \n \nุดูุฑูุง ูุฅุถุงูุชู ููุง ุ ูุชุดุบูู ุงูููุฏูู ูุงูููุณููู ุนูู ุฏุฑุฏุดุฉ ุงูููุฏูู ุงูุฎุงุตุฉ ุจูุฌููุนุชู โค"

    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=alive,
        reply_markup=keyboard,
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text("๐ `PONG!!`\n" f"โก๏ธ `{delta_ping * 1000:.3f} ms`")


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "๐ค ุญูุงูู ุงููุจูุช:\n"
        f"โข **ูููุช ุงููุชุดุบููู:** `{uptime}`\n"
        f"โข **ูููุช ุจุฏุฃ ุงูุชุดุบูู:** `{START_TIME_ISO}`"
    )


@Client.on_message(filters.new_chat_members)
async def new_chat(c: Client, m: Message):
    ass_uname = (await user.get_me()).username
    bot_id = (await c.get_me()).id
    for member in m.new_chat_members:
        if member.id == bot_id:
            return await m.reply(
                "**ุดูุฑุง ูุฅุถุงูุชู ุฅูู ุงููุฌููุนุฉ** โฅ๏ธ๐ \n\n"
                "ููู ุจูุฑูุนูู ูุดูุฑู ููู ุงูููุฌููุนู ูุงุชูููู ูู ุงููุนููู ุจุดููู ุฌูุฏ โโโโโขโโโโโข ุงููุชุจ. `/userbotjoin` ููุฏุฎูู ุงูุญูุณุงุจ ุงูููุณุงุนุฏ ููููุฌููุนู.\n\n"
                "ุจูุนุฏ ู ุชูุฎูุต ุงูุชุจ ุงูุงูุฑ `/reload`",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("๐ฃ ููุงู ุงูุจูุช", url=f"https://t.me/{UPDATES_CHANNEL}"),
                            InlineKeyboardButton("๐ญ ุฌุฑูุจ ุงูุฏุนู", url=f"https://t.me/{GROUP_SUPPORT}")
                        ],
                        [
                            InlineKeyboardButton("๐ค ุงูุญุณุงุจ ุงููุณุงุนุฏ", url=f"https://t.me/{ass_uname}")
                        ]
                    ]
                )
            )
