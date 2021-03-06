# Copyright (C) 2021 By VeezMusicProject

from driver.queues import QUEUE
from pyrogram import Client, filters
from program.utils.inline import menu_markup
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.answer("home start")
    await query.edit_message_text(
        f"""{message.from_user.mention()} ๐ฎโ ูุฑุญุจุง ุจู ุนุฒูุฒู*\n
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
                        "- ูู ุนุงูุฒ ุชูุตุจ ุจูุช", url="https://t.me/k_p_s_6"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.answer("ุฏููู ุงูุชุดุบูู")
    await query.edit_message_text(
        f""" **ุฏููู ุชุดุบูู ุงูุจูุช:**

1.) **ุงุถููู ุงูู ูุฌููุนุชู.**

2.) **ุจุนุฏ ุฐูู ุ ูู ุจุชุฑููุชู ููุณุคูู ูููุญ ุฌููุน ุงูุฃุฐููุงุช ุจุงุณุชุซูุงุก ุงููุณุคูู ุงููุฌููู.**

3.) **ุจุนุฏ ุชุฑููุชู ุ ุงูุชุจ /reload ูู ูุฌููุนุฉ ูุชุญุฏูุซ ุจูุงูุงุช ุงูุงุฏูููู.**

3.) **ุฃุถู @{ASSISTANT_NAME} ุฅูู ูุฌููุนุชู ุฃู ุงูุชุจ /userbotjoin ูุฏุนูุชูุง**

4.) **ูู ุจุชุดุบูู ูุญุงุฏุซุฉ ุงูููุฏูู ุฃููุงู ูุจู ุงูุจุฏุก ูู ุชุดุบูู ุงูููุฏูู / ุงูููุณููู..**

5.) **ูู ุจุนุถ ุงูุฃุญูุงู ุ ูููู ุฃู ุชุณุงุนุฏู ุฅุนุงุฏุฉ ุชุญููู ุงูุจูุช ุจุงุณุชุฎุฏุงู ุงูุฃูุฑ /reload ูู ุฅุตูุงุญ ุจุนุถ ุงููุดููุงุช.**

๐ **ุฅุฐุง ูู ููุถู ุงููุณุชุฎุฏู ุงูุจูุช ุฅูู ุงูุฏุฑุฏุดุฉ ุงููุฑุฆูุฉ ุ ูุชุฃูุฏ ูู ุชุดุบูู ุงูุฏุฑุฏุดุฉ ุงููุฑุฆูุฉ ุจุงููุนู ุ ุฃู ุงูุชุจ /userbotleave ุซู ุงูุชุจ /userbotJoin ูุฑุฉ ุฃุฎุฑู.**

๐ก **ุฅุฐุง ูุงูุช ูุฏูู ุฃุณุฆูุฉ ูุชุงุจุนุฉ ุญูู ูุฐุง ุงูุจูุช ุ ูููููู ุฅุฎุจุงุฑู ูู ุฎูุงู ุฌุฑูุจ ุงูุฏุนู ุงูุฎุงุตุฉ ุจู ููุง: @{GROUP_SUPPORT}**

โก๏ธ __Powered by @K_P_S_6 __""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("๐ Go Back", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.answer("ูุงุฆูู ุงูุงูุงูุฑ")
    await query.edit_message_text(
        f"""โจ **ููุฑุญุจุง [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

ยป **ุงุถุบุท ุนูู ุงูุฒุฑ ุฃุฏูุงู ููุฑุงุกุฉ ุงูุดุฑุญ ููุดุงูุฏุฉ ูุงุฆูุฉ ุงูุฃูุงูุฑ ุงููุชุงุญุฉ!**

โก๏ธ __Powered by @K_P_S_6 __""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("๐ท๐ป ุงูุงููุฑ ุงูุงุฏููููู", callback_data="cbadmin"),
                    InlineKeyboardButton("๐ง๐ป ุงูุงูุฑ ุงููุทูุฑ", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("๐ ุงูุงูุงูุฑ ุงูุงุณุงุณูู", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("๐ ุฑุฌูุน", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.answer("ุงูุงูุงูุฑ ุงูุงุณุงุณูู")
    await query.edit_message_text(
        f"""๐ฎ ุงูุงูุงูุฑ ุงูุงุณุงุณูู:

ยป /play (ุงุณู ุงูุฃุบููุฉ / ุฑุงุจุท) - ุชุดุบูู ุงูููุณููู ุนูู ุฏุฑุฏุดุฉ ุงูููุฏูู
ยป /vplay (ุงุณู / ุฑุงุจุท ุงูููุฏูู) - ุชุดุบูู ุงูููุฏูู ุนูู ุฏุฑุฏุดุฉ ุงูููุฏูู
ยป /vstream - ุชุดุบูู ููุฏูู ูุจุงุดุฑ ูู yt live / m3u8
ยป /playlist - ุชุธูุฑ ูู ูุงุฆูุฉ ุงูุชุดุบูู
ยป /video (query) - ุชุญููู ุงูููุฏูู ูู ุงูููุชููุจ
ยป /song (query) - ุชุญููู ุงุบููุฉ ูู ุงูููุชููุจ
ยป /lyric (query) - ูุต ุงูุงุบููุฉ ุงูุบูุงุฆูุฉ
ยป /search (query) - ุงุจุญุซ ุนู ุฑุงุจุท ููุฏูู youtube

ยป /ping - ููู ุญุงูุฉ ุจููุบ ุงูุจูุช
ยป /uptime - ุนุฑุถ ุญุงูุฉ bot ุงูุฌููุฒูุฉ
ยป /alive - ุนุฑุถ ูุนูููุงุช ุงูุฑูุจูุช ุนูู ููุฏ ุงูุญูุงุฉ (ูู ูุฌููุนุฉ)

โก๏ธ __Powered by @K_P_S_6 __""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("๐ ุฑุฌูุน", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.answer("ุงูุงูุฑ ุงูุงุฏูููู")
    await query.edit_message_text(
        f"""๐ฎ ุงูุงูุฑ ุงูุงุฏูููู:

ยป /pause - ุงููููุงู ุงููุจุซ
ยป /resume - ุงุณุชููุงู ุงูุจุซ
ยป /skip - ุชุฎูุทู ุงูุงุบููู
ยป /stop - ุงูููุงู ุงููุจุซ
ยป /vmute - ูุชู ุตูุช ุงููุณุชุฎุฏู ุงูุจูุช ูู ุงูุฏุฑุฏุดุฉ ุงูุตูุชูุฉ
ยป /vunmute - ุฅูุบุงุก ูุชู ุตูุช ุงูุจูุช ูู ุงูุฏุฑุฏุดุฉ ุงูุตูุชูุฉ
ยป /volume `1-200` - ุถุจุท ุญุฌู ุงูููุณููู (ูุฌุจ ุฃู ูููู ุงููุญุณุงุจ ุงููุณุงุนุฏ ูุณุคููุงู)
ยป /reload - ุงุนุงุฏู ุชุญููู ุงูุจูุช ูุชุญุฏูุซ ุจูุงูุงุช ุงููุณุคููู
ยป /userbotjoin - ุงุถุงูู ุงูุญุณุงุจ ุงููุณุงุนุฏ ูููุฌููุนู
ยป /userbotleave - ุงุฒุงูู ุงูุญุณุงุจ ุงููุณุงุนุฏ ูู ุงููุฌููุนู

โก๏ธ __Powered by @K_P_S_6 __""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("๐ ุฑุฌูุน", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.answer("ุงูุงูุฑ ุงููุทูุฑ")
    await query.edit_message_text(
        f"""๐ฎ ุงูุงูุฑ ุงููุทูุฑ:

ยป /rmw - ุชูุธูู ุฌููุน ุงููููุงุช ุงูู raw
ยป /rmd - ุชูุธูู ุฌููุน ุงููููุงุช ุงูุชู ุชู ุชูุฒูููุง
ยป /sysinfo - show the system information
ยป /update - ูู ุจุชุญุฏูุซ ุงูุฑูุจูุช ุงูุฎุงุต ุจู ุฅูู ุฃุญุฏุซ ุฅุตุฏุงุฑ
ยป /restart - ุงุนุงุฏู ุชุดุบูู ุงูุจูุช
ยป /leaveall - ูุบุงุฏุฑู ุงูุญุณุงุจ ุงููุณุงุนุฏ ูู ุงููุฌููุนุงุช

โก๏ธ __Powered by @K_P_S_6 __""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("๐ ุฑุฌูุน", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("๐ก ุงููุณุคูู ุงููุญูุฏ ุงูุฐู ูุฏูู ุฅุฐู ุฅุฏุงุฑุฉ ุงูุฏุฑุฏุดุงุช ุงูุตูุชูุฉ ููููู ุงูุทุบุท ุนูู ูุฐู ุงูุงุฒุฑุงุฑ !", show_alert=True)
    chat_id = query.message.chat.id
    user_id = query.message.from_user.id
    buttons = menu_markup(user_id)
    chat = query.message.chat.title
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"โ๏ธ **ุงุนุฏุงุฏุงุช ุงูุจูุช** {chat} \n \nโธ: ุฅููุงู ุงูุจุซ ูุคูุชูุง \n โถ ๏ธ: ุงุณุชุฆูุงู ุงูุจุซ \n๐: ูุชู ุตูุช ุงููุณุชุฎุฏู \n ๐: ุฅูุบุงุก ูุชู ุตูุช ุงููุณุชุฎุฏู \n โน: ุฅููุงู ุงูุจุซ",
              reply_markup=InlineKeyboardMarkup(buttons),
          )
    else:
        await query.answer("โ ูุง ูููุชูู ุชูุดูุบููู ุดุฆ ุญูุงูููุง", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("๐ก ุงููุณุคูู ุงููุญูุฏ ุงูุฐู ูุฏูู ุฅุฐู ุฅุฏุงุฑุฉ ุงูุฏุฑุฏุดุงุช ุงูุตูุชูุฉ ููููู ุงูุทุบุท ุนูู ูุฐู ุงูุงุฒุฑุงุฑ !", show_alert=True)
    await query.message.delete()
