# Copyright (C) 2021 By Veez Music-Project
# Commit Start Date 20/10/2021
# Finished On 28/10/2021

import re
import asyncio

from config import ASSISTANT_NAME, BOT_USERNAME, IMG_1, IMG_2
from driver.design.thumbnail import thumb
from driver.design.chatname import CHAT_TITLE
from driver.filters import command, other_filters
from driver.queues import QUEUE, add_to_queue
from driver.veez import call_py, user
from driver.utils import bash
from pyrogram import Client
from pyrogram.errors import UserAlreadyParticipant, UserNotParticipant
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pytgcalls import StreamType
from pytgcalls.types.input_stream import AudioPiped
from youtubesearchpython import VideosSearch


def ytsearch(query: str):
    try:
        search = VideosSearch(query, limit=1).result()
        data = search["result"][0]
        songname = data["title"]
        url = data["link"]
        duration = data["duration"]
        thumbnail = f"https://i.ytimg.com/vi/{data['id']}/hqdefault.jpg"
        return [songname, url, duration, thumbnail]
    except Exception as e:
        print(e)
        return 0


async def ytdl(format: str, link: str):
    stdout, stderr = await bash(f'youtube-dl -g -f "{format}" {link}')
    if stdout:
        return 1, stdout.split("\n")[0]
    return 0, stderr


@Client.on_message(command(["play", f"play@{BOT_USERNAME}"]) & other_filters)
async def play(c: Client, m: Message):
    await m.delete()
    replied = m.reply_to_message
    chat_id = m.chat.id
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text="• الــقـائـمه", callback_data="cbmenu"),
                InlineKeyboardButton(text="• اغــلاق", callback_data="cls"),
            ]
        ]
    )
    if m.sender_chat:
        return await m.reply_text("you're an __Anonymous__ Admin !\n\n» revert back to user account from admin rights.")
    try:
        aing = await c.get_me()
    except Exception as e:
        return await m.reply_text(f"خــطا:\n\n{e}")
    a = await c.get_chat_member(chat_id, aing.id)
    if a.status != "administrator":
        await m.reply_text(
            f"💡 لاستخدامي ، يجب أن أكون مسؤولاً مع الأذونات التالية: \n \n »❌ حذف الرسائل \n» ❌ إضافة مستخدمين \n »❌ إدارة محادثة الفيديو \n \nيتم تحديث البيانات تلقائيًا بعد ترقيتي"
        )
        return
    if not a.can_manage_voice_chats:
        await m.reply_text(
            "missing required permission:" + "\n\n» ❌ __Manage video chat__"
        )
        return
    if not a.can_delete_messages:
        await m.reply_text(
            "missing required permission:" + "\n\n» ❌ __Delete messages__"
        )
        return
    if not a.can_invite_users:
        await m.reply_text("missing required permission:" + "\n\n» ❌ __Add users__")
        return
    try:
        ubot = (await user.get_me()).id
        b = await c.get_chat_member(chat_id, ubot)
        if b.status == "kicked":
            await m.reply_text(
                f"تم حظر @{ASSISTANT_NAME} في المجموعة {m.chat.title} \n \n »قم بإلغاء حظر الاك المساعد أولاً إذا كنت تريد استخدام هذا البوت."
            )
            return
    except UserNotParticipant:
        if m.chat.username:
            try:
                await user.join_chat(m.chat.username)
            except Exception as e:
                await m.reply_text(f"❌ **فشل في الانضمام**\n\n**السبب**: `{e}`")
                return
        else:
            try:
                invitelink = await c.export_chat_invite_link(
                    m.chat.id
                )
                if invitelink.startswith("https://t.me/+"):
                    invitelink = invitelink.replace(
                        "https://t.me/+", "https://t.me/joinchat/"
                    )
                await user.join_chat(invitelink)
            except UserAlreadyParticipant:
                pass
            except Exception as e:
                return await m.reply_text(
                    f"❌ **فشل في الانضمام**\n\n**السبب**: `{e}`"
                )
    if replied:
        if replied.audio or replied.voice:
            suhu = await replied.reply("📥 **يـتم تحـميل الـمقطع...**")
            dl = await replied.download()
            link = replied.link
            if replied.audio:
                if replied.audio.title:
                    songname = replied.audio.title[:70]
                else:
                    if replied.audio.file_name:
                        songname = replied.audio.file_name[:70]
                    else:
                        songname = "Audio"
            elif replied.voice:
                songname = "Voice Note"
            if chat_id in QUEUE:
                pos = add_to_queue(chat_id, songname, dl, link, "Audio", 0)
                await suhu.delete()
                await m.reply_photo(
                    photo=f"{IMG_1}",
                    caption=f"💡 تمت إضافة الاغنيه إلى قائمة الانتظار »{pos} \ n \ n🏷 الاسم: [{songname}] ({link}) | موسيقى \n💭 الدردشة: {chat_id} \n🎧 طلب من: {m.from_user.mention ()}",
                    reply_markup=keyboard,
                )
            else:
             try:
                await suhu.edit("🔄 **يـنضم الي المحادثه الصوتيه...**")
                await call_py.join_group_call(
                    chat_id,
                    AudioPiped(
                        dl,
                    ),
                    stream_type=StreamType().local_stream,
                )
                add_to_queue(chat_id, songname, dl, link, "Audio", 0)
                await suhu.delete()
                requester = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                await m.reply_photo(
                    photo=f"{IMG_2}",
                    caption=f"🏷 الاسم: [{songname}] ({link}) \n💭 الدردشة: {chat_id} \n💡 الحالة: قيد التشغيل \n🎧 طلب من: {requester} \n📹 نوع البث: موسيقى",
                    reply_markup=keyboard,
                )
             except Exception as e:
                await suhu.delete()
                await m.reply_text(f"🚫 خطـا:\n\n» {e}")
        else:
            if len(m.command) < 2:
                await m.reply(
                    "»قم بالرد على ملف صوتي أو إعطاء شيء للبحث."
                )
            else:
                suhu = await c.send_message(chat_id, "🔍 **يـتم الـبـحث...**")
                query = m.text.split(None, 1)[1]
                search = ytsearch(query)
                if search == 0:
                    await suhu.edit("❌ **لا يــوجد نتـائـج.**")
                else:
                    songname = search[0]
                    title = search[0]
                    url = search[1]
                    duration = search[2]
                    thumbnail = search[3]
                    userid = m.from_user.id
                    gcname = m.chat.title
                    ctitle = await CHAT_TITLE(gcname)
                    image = await thumb(thumbnail, title, userid, ctitle)
                    format = "bestaudio[ext=m4a]"
                    veez, ytlink = await ytdl(format, url)
                    if veez == 0:
                        await suhu.edit(f"❌ yt-dl issues detected\n\n» `{ytlink}`")
                    else:
                        if chat_id in QUEUE:
                            pos = add_to_queue(
                                chat_id, songname, ytlink, url, "Audio", 0
                            )
                            await suhu.delete()
                            requester = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                            await m.reply_photo(
                                photo=image,
                                caption=f"💡 تمت إضافة الاغنيه إلى قائمة الانتظار »{pos} \n \n🏷 الاسم: [{songname}] ({url}) | موسيقى \n⏱ المدة: {duration} \n🎧 طلب بواسطة: {requester}",
                                reply_markup=keyboard,
                            )
                        else:
                            try:
                                await suhu.edit("🔄 **يـنضم الي المحادثه الصوتيه...*")
                                await call_py.join_group_call(
                                    chat_id,
                                    AudioPiped(
                                        ytlink,
                                    ),
                                    stream_type=StreamType().local_stream,
                                )
                                add_to_queue(chat_id, songname, ytlink, url, "Audio", 0)
                                await suhu.delete()
                                requester = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                                await m.reply_photo(
                                    photo=image,
                                    caption=f"🏷 الاسم: [{songname}] ({link}) \n💭 الدردشة: {chat_id} \n💡 الحالة: قيد التشغيل \n🎧 طلب من: {requester} \n📹 نوع البث: موسيقى",
                                    reply_markup=keyboard,
                                )
                            except Exception as ep:
                                await suhu.delete()
                                await m.reply_text(f"🚫 خـطا: `{ep}`")

    else:
        if len(m.command) < 2:
            await m.reply(
                "»قم بالرد على ملف صوتي أو إعطاء شيء للبحث."
            )
        else:
            suhu = await c.send_message(chat_id, "🔍 **يــتم الــبحـث...**")
            query = m.text.split(None, 1)[1]
            search = ytsearch(query)
            if search == 0:
                await suhu.edit("❌ **لا يــوجد نتـائـج.**")
            else:
                songname = search[0]
                title = search[0]
                url = search[1]
                duration = search[2]
                thumbnail = search[3]
                userid = m.from_user.id
                gcname = m.chat.title
                ctitle = await CHAT_TITLE(gcname)
                image = await thumb(thumbnail, title, userid, ctitle)
                format = "bestaudio[ext=m4a]"
                veez, ytlink = await ytdl(format, url)
                if veez == 0:
                    await suhu.edit(f"❌ yt-dl issues detected\n\n» `{ytlink}`")
                else:
                    if chat_id in QUEUE:
                        pos = add_to_queue(chat_id, songname, ytlink, url, "Audio", 0)
                        await suhu.delete()
                        requester = (
                            f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                        )
                        await m.reply_photo(
                            photo=image,
                            caption=f"💡 تمت إضافة الاغنيه إلى قائمة الانتظار »{pos} \n \n🏷 الاسم: [{songname}] ({url}) | موسيقى \n⏱ المدة: {duration} \n🎧 طلب بواسطة: {requester}",
                            reply_markup=keyboard,
                        )
                    else:
                        try:
                            await suhu.edit("🔄 **يـنضم الي المحادثه الصوتيه...*")
                            await call_py.join_group_call(
                                chat_id,
                                AudioPiped(
                                    ytlink,
                                ),
                                stream_type=StreamType().local_stream,
                            )
                            add_to_queue(chat_id, songname, ytlink, url, "Audio", 0)
                            await suhu.delete()
                            requester = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                            await m.reply_photo(
                                photo=image,
                                caption=f"🏷 الاسم: [{songname}] ({link}) \n💭 الدردشة: {chat_id} \n💡 الحالة: قيد التشغيل \n🎧 طلب من: {requester} \n📹 نوع البث: موسيقى",
                                reply_markup=keyboard,
                            )
                        except Exception as ep:
                            await suhu.delete()
                            await m.reply_text(f"🚫 خــطا: `{ep}`")
