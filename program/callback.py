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
        f"""{message.from_user.mention()} 📮╎ مرحبا بك عزيزي*\n
🎧╎انا بوت تشغيل الفديو و الموسيقى في الدردشات الصوتيه.

📥╎استطيع ايضا التحمل من اليوتيوب فديو او صوت بجميع الدقق.

📮╎لمعرفه كيفيه تشغيلي في مجموعتك اضغط علي زر اوامر البوت بالاسفل لكي اعرض لك جميع الاوامر.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "- اضف البوت الي مجموعتك",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("- طريقه تشغيل البوت", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("- الاوامر", callback_data="cbcmds"),
                    InlineKeyboardButton("- المطور", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "- جروب الدعم", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "- قناه البوت", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "- لو عايز تنصب بوت", url="https://t.me/k_p_s_6"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.answer("دليل التشغيل")
    await query.edit_message_text(
        f""" **دليل تشغيل البوت:**

1.) **اضفني الي مجموعتك.**

2.) **بعد ذلك ، قم بترقيتي كمسؤول ومنح جميع الأذونات باستثناء المسؤول المجهول.**

3.) **بعد ترقيتي ، اكتب /reload في مجموعة لتحديث بيانات الادمنيه.**

3.) **أضف @{ASSISTANT_NAME} إلى مجموعتك أو اكتب /userbotjoin لدعوتها**

4.) **قم بتشغيل محادثة الفيديو أولاً قبل البدء في تشغيل الفيديو / الموسيقى..**

5.) **في بعض الأحيان ، يمكن أن تساعدك إعادة تحميل البوت باستخدام الأمر /reload في إصلاح بعض المشكلات.**

📌 **إذا لم ينضم المستخدم البوت إلى الدردشة المرئية ، فتأكد من تشغيل الدردشة المرئية بالفعل ، أو اكتب /userbotleave ثم اكتب /userbotJoin مرة أخرى.**

💡 **إذا كانت لديك أسئلة متابعة حول هذا البوت ، فيمكنك إخباره من خلال جروب الدعم الخاصة بي هنا: @{GROUP_SUPPORT}**

⚡️ __Powered by @K_P_S_6 __""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.answer("قائمه الاوامر")
    await query.edit_message_text(
        f"""✨ **مـرحبا [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

» **اضغط على الزر أدناه لقراءة الشرح ومشاهدة قائمة الأوامر المتاحة!**

⚡️ __Powered by @K_P_S_6 __""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("👷🏻 اوامـر الادمـنيه", callback_data="cbadmin"),
                    InlineKeyboardButton("🧙🏻 اوامر المطور", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("📚 الاوامر الاساسيه", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("🔙 رجوع", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.answer("الاوامر الاساسيه")
    await query.edit_message_text(
        f"""🏮 الاوامر الاساسيه:

» /play (اسم الأغنية / رابط) - تشغيل الموسيقى على دردشة الفيديو
» /vplay (اسم / رابط الفيديو) - تشغيل الفيديو على دردشة الفيديو
» /vstream - تشغيل فيديو مباشر من yt live / m3u8
» /playlist - تظهر لك قائمة التشغيل
» /video (query) - تحميل الفيديو من اليوتيوب
» /song (query) - تحميل اغنية من اليوتيوب
» /lyric (query) - قص الاغنية الغنائية
» /search (query) - ابحث عن رابط فيديو youtube

» /ping - كيف حالة بينغ البوت
» /uptime - عرض حالة bot الجهوزية
» /alive - عرض معلومات الروبوت على قيد الحياة (في مجموعة)

⚡️ __Powered by @K_P_S_6 __""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 رجوع", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.answer("اوامر الادمنيه")
    await query.edit_message_text(
        f"""🏮 اوامر الادمنيه:

» /pause - ايـقـاف الـبث
» /resume - استكمال البث
» /skip - تخـطي الاغنيه
» /stop - ايـقاف الـبث
» /vmute - كتم صوت المستخدم البوت في الدردشة الصوتية
» /vunmute - إلغاء كتم صوت البوت في الدردشة الصوتية
» /volume `1-200` - ضبط حجم الموسيقى (يجب أن يكون الـحساب المساعد مسؤولاً)
» /reload - اعاده تحميل البوت وتحديث بيانات المسؤلين
» /userbotjoin - اضافه الحساب المساعد للمجموعه
» /userbotleave - ازاله الحساب المساعد من المجموعه

⚡️ __Powered by @K_P_S_6 __""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 رجوع", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.answer("اوامر المطور")
    await query.edit_message_text(
        f"""🏮 اوامر المطور:

» /rmw - تنظيف جميع الملفات الـ raw
» /rmd - تنظيف جميع الملفات التي تم تنزيلها
» /sysinfo - show the system information
» /update - قم بتحديث الروبوت الخاص بك إلى أحدث إصدار
» /restart - اعاده تشغيل البوت
» /leaveall - مغادره الحساب المساعد كل المجموعات

⚡️ __Powered by @K_P_S_6 __""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 رجوع", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 المسؤول الوحيد الذي لديه إذن إدارة الدردشات الصوتية يمكنه الطغط علي هذه الازرار !", show_alert=True)
    chat_id = query.message.chat.id
    user_id = query.message.from_user.id
    buttons = menu_markup(user_id)
    chat = query.message.chat.title
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"⚙️ **اعدادات البوت** {chat} \n \n⏸: إيقاف البث مؤقتًا \n ▶ ️: استئناف البث \n🔇: كتم صوت المستخدم \n 🔊: إلغاء كتم صوت المستخدم \n ⏹: إيقاف البث",
              reply_markup=InlineKeyboardMarkup(buttons),
          )
    else:
        await query.answer("❌ لا يــتـم تـشـغيـل شئ حـالـيا", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 المسؤول الوحيد الذي لديه إذن إدارة الدردشات الصوتية يمكنه الطغط علي هذه الازرار !", show_alert=True)
    await query.message.delete()
