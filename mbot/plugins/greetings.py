"""MIT License

Copyright (c) 2022 Daniel

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from datetime import datetime
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from pyrogram.raw.functions import Ping
from mbot import LOG_GROUP, OWNER_ID, SUDO_USERS, Mbot,AUTH_CHATS
from os import execvp,sys

@Mbot.on_message(filters.command("start"))
async def start(client,message):
    reply_markup = [[
        InlineKeyboardButton(
            text="Update Channel", url="https://t.me/Silent_BOts"),
        InlineKeyboardButton(
            text="Developer",
            url=f"https://t.me/THE_DS_OFFICIAL")
        ],[
        InlineKeyboardButton(text="Help",callback_data="helphome")
        ]]
    # if LOG_GROUP:

    #     invite_link = await client.create_chat_invite_link(chat_id=(int(LOG_GROUP) if str(LOG_GROUP).startswith("-100") else LOG_GROUP))
    #     reply_markup.append([InlineKeyboardButton("LOG Channel", url=invite_link.invite_link)])
    if message.chat.type != "private" and message.chat.id not in AUTH_CHATS and message.from_user.id not in SUDO_USERS:
        return await message.reply_text("This Bot Will Not Work In Groups Unless It's Authorized.",
                    reply_markup=InlineKeyboardMarkup(reply_markup))
    return await message.reply_text(f"<b>Hᴇʟʟᴏ {message.from_user.first_name},  Jᴀɪ Sʜʀᴇᴇ Rᴀᴍ...🙏🏻\n\nɪ ᴀᴍ ᴛʜᴇ ᴍᴏꜱᴛ ᴘᴏᴡᴇʀꜰᴜʟ Mᴇᴅɪᴀ Dᴏᴡɴʟᴏᴀᴅᴇʀ ʙᴏᴛ!\n\nI Cᴀɴ Dᴏᴡɴʟᴏᴀᴅ Vɪᴅᴇᴏꜱ Fʀᴏᴍ Iɴꜱᴛᴀɢʀᴀᴍ, Fᴀᴄᴇʙᴏᴏᴋ & Tᴡɪᴛᴛᴇʀ Aɴᴅ Dᴏᴡɴʟᴏᴀᴅ Mᴜꜱɪᴄ Fʀᴏᴍ Sᴘᴏᴛɪғʏ, Yᴏᴜᴛᴜʙᴇ, Dᴇᴇᴢᴇʀ, Sᴏᴜɴᴅᴄʟᴏᴜᴅ, Eᴛᴄ 🔥\n\n<blockquote>Uꜱᴇ /song Cᴏᴍᴍᴀɴᴅ Tᴏ Dᴏᴡɴʟᴏᴀᴅ Aɴʏ Sᴏɴɢ Wɪᴛʜᴏᴜᴛ Lɪɴᴋ\nUꜱᴇ /lyrics Cᴏᴍᴍᴀɴᴅ Tᴏ Gᴇᴛ Lʏʀɪᴄꜱ Oғ Aɴʏ Sᴏɴɢ !</blockquote>\n\nJᴜꜱᴛ Sᴇɴᴅ Mᴇ Aɴʏ Mᴇᴅɪᴀ Lɪɴᴋ Aɴᴅ Sᴇᴇ Mᴀɢɪᴄ 🤞🏻✨.</b>",
                    reply_markup=InlineKeyboardMarkup(reply_markup))

@Mbot.on_message(filters.command("restart") & filters.chat(OWNER_ID) & filters.private)
async def restart(_,message):
    await message.delete()
    execvp(sys.executable,[sys.executable,"-m","mbot"])

@Mbot.on_message(filters.command("log") & filters.chat(SUDO_USERS))
async def send_log(_,message):
    await message.reply_document("bot.log")

@Mbot.on_message(filters.command("ping"))
async def ping(client,message):
    start = datetime.now()
    await client.invoke(Ping(ping_id=0))
    ms = (datetime.now() - start).microseconds / 1000
    await message.reply_text(f"**Pong!**\nResponse time: `{ms} ms`")

HELP = {
    "Youtube": "Send **Youtube** Link in Chat to Download Song.",
    "Spotify": "Send **Spotify** Track/Playlist/Album/Show/Episode's Link. I'll Download It For You.\n\n⚠ Playlist Not Support To Download, We Will Fix Soon",
    "Deezer": "Send Deezer Playlist/Album/Track Link. I'll Download It For You.",
    "Jiosaavn": "Not Implemented yet",
    "SoundCloud": "Not Implemented yet",
    "Group": "Add Bot In Your Group As admin."
}


@Mbot.on_message(filters.command("help"))
async def help(_,message):
    button = [
        [InlineKeyboardButton(text=i, callback_data=f"help_{i}")] for i in HELP
    ]
    button.append([InlineKeyboardButton(text="back", callback_data=f"backdome")])
    await message.reply_text(f"Hello **{message.from_user.first_name}**, I'm **@Public_Media_Downloader_Bot**.\nI'm Here to download your music.",
                        reply_markup=InlineKeyboardMarkup(button))

@Mbot.on_callback_query(filters.regex(r"backdome"))
async def backdo(_,query):
    button = [
        [InlineKeyboardButton(text=i, callback_data=f"help_{i}")] for i in HELP
    ]
    button.append([InlineKeyboardButton(text="back", callback_data=f"backdome")])
    await query.message.edit(f"Hello **{query.message.from_user.first_name}**, I'm **@Public_Media_Downloader_Bot**.\nI'm Here to download your music.",
                        reply_markup=InlineKeyboardMarkup(button))     
    
@Mbot.on_callback_query(filters.regex(r"help_(.*?)"))
async def helpbtn(_,query):
    i = query.data.replace("help_","")
    button = InlineKeyboardMarkup([[InlineKeyboardButton("Back",callback_data="helphome")]])
    text = f"Help for **{i}**\n\n{HELP[i]}"
    await query.message.edit(text = text,reply_markup=button)

@Mbot.on_callback_query(filters.regex(r"helphome"))
async def help_home(_,query):
    button = [
        [InlineKeyboardButton(text=i, callback_data=f"help_{i}")] for i in HELP
    ]
    await query.message.edit(f"Hello **{query.from_user.first_name}**,I'm **@Public_Media_Downloader_Bot**.\nI'm Here to download your music.",
                        reply_markup=InlineKeyboardMarkup(button))
