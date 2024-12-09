#
# Copyright (C) 2024 by MISH0009@Github, < https://github.com/MISH0009 >.
#
# This file is part of < https://github.com/MISH0009/DNS > project,
# and is released under the MIT License.
# Please see < https://github.com/MISH0009/DNS/blob/master/LICENSE >
#
# All rights reserved.

import requests
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from DnsXMusic import app


@app.on_message(
    filters.command(
        [
            "boob",
            "ludo",
            "dart",
            "basket",
            "basketball",
            "football",
            "slot",
            "bowling",
            "jackpot",
        ]
    )
)
async def dice(c, m: Message):
    command = m.text.split()[0]
    if command == "/boob" or command == "/boob":
        keyboard = InlineKeyboardMarkup(
            [[InlineKeyboardButton("🙈", callback_data="send_boob")]]
        )
        value = await c.send_dice(m.chat.id, reply_markup=keyboard)

    elif command == "/dart":

        value = await c.send_dice(m.chat.id, emoji="🎯", reply_to_message_id=m.id)
        await value.reply_text("ʏᴏᴜʀ sᴄᴏʀᴇ ɪs {0}".format(value.dice.value))

    elif command == "/basket" or command == "/basketball":
        basket = await c.send_dice(m.chat.id, emoji="🏀", reply_to_message_id=m.id)
        await basket.reply_text("ʏᴏᴜʀ sᴄᴏʀᴇ ɪs {0}".format(basket.dice.value))

    elif command == "/football":
        value = await c.send_dice(m.chat.id, emoji="⚽", reply_to_message_id=m.id)
        await value.reply_text("ʏᴏᴜʀ sᴄᴏʀᴇ ɪs {0}".format(value.dice.value))

    elif command == "/slot" or command == "/jackpot":
        value = await c.send_dice(m.chat.id, emoji="🎰", reply_to_message_id=m.id)
        await value.reply_text("ʏᴏᴜʀ sᴄᴏʀᴇ ɪs {0}".format(value.dice.value))
    elif command == "/bowling":
        value = await c.send_dice(m.chat.id, emoji="🎳", reply_to_message_id=m.id)
        await value.reply_text("ʏᴏᴜʀ sᴄᴏʀᴇ ɪs {0}".format(value.dice.value))

    elif command == "/boob" or command == "boob":
    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("🍒", callback_data="send_boob")]
        ]
    )
    # Replace "https://t.me/yrfgghshhs/620" with the actual path of the video
    video_path = "https://t.me/yrfgghshhs/620"
    await c.send_video(
        chat_id=m.chat.id,
        video=video_path,
        caption="https://t.me/yrfgghshhs/620",
        reply_markup=keyboard
        )
bored_api_url = "https://apis.scrimba.com/bored/api/activity"


@app.on_message(filters.command("bored", prefixes="/"))
async def bored_command(client, message):
    response = requests.get(bored_api_url)
    if response.status_code == 200:
        data = response.json()
        activity = data.get("activity")
        if activity:
            await message.reply(f"𝗙𝗲𝗲𝗹𝗶𝗻𝗴 𝗯𝗼𝗿𝗲𝗱? 𝗛𝗼𝘄 𝗮𝗯𝗼𝘂𝘁:\n\n {activity}")
        else:
            await message.reply("Nᴏ ᴀᴄᴛɪᴠɪᴛʏ ғᴏᴜɴᴅ.")
    else:
        await message.reply("Fᴀɪʟᴇᴅ ᴛᴏ ғᴇᴛᴄʜ ᴀᴄᴛɪᴠɪᴛʏ.")


@app.on_callback_query(filters.regex(r"send_dice"))
async def dice_again(client, query):
    try:
        await app.edit_message_text(
            query.message.chat.id, query.message.id, query.message.boob.emoji
        )
    except BaseException:
        pass
    keyboard = InlineKeyboardMarkup(
        [[InlineKeyboardButton("🔄", callback_data="send_boob")]]
    )
    await client.send_dice(query.message.chat.id, reply_markup=keyboard)


__MODULE__ = "๏ Mᴀsᴛɪ ๏"
__HELP__ = """
**ʜᴀᴠɪɴɢ ꜰᴜɴ:**

• `/boob`: Yᴏᴜʀ Bᴏᴏʙ Sɪᴢᴇ.
• `/ludo`: Pʟᴀʏ Lᴜᴅᴏ.
• `/dart`: Tʜʀᴏᴡs ᴀ ᴅᴀʀᴛ.
• `/basket` ᴏʀ `/basketball`: Pʟᴀʏs ʙᴀsᴋᴇᴛʙᴀʟʟ.
• `/football`: Pʟᴀʏs ғᴏᴏᴛʙᴀʟʟ.
• `/slot` ᴏʀ `/jackpot`: Pʟᴀʏs ᴊᴀᴄᴋᴘᴏᴛ.
• `/bowling`: Pʟᴀʏs ʙᴏᴡʟɪɴɢ.
• `/bored`: Gᴇᴛs ʀᴀɴᴅᴏᴍ ᴀᴄᴛɪᴠɪᴛʏ ɪғ ʏᴏᴜ'ʀᴇ ʙᴏʀᴇᴅ.
"""
