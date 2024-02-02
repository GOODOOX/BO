import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import(InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, InputMediaVideo, Message)
from config import LOGGER_ID as LOG_GROUP_ID
from DAXXMUSIC import app 
from pyrogram.errors import RPCError
from pyrogram.types import ChatMemberUpdated, InlineKeyboardMarkup, InlineKeyboardButton
from os import environ
from typing import Union, Optional
from PIL import Image, ImageDraw, ImageFont
from os import environ
from pyrogram.types import ChatJoinRequest, InlineKeyboardButton, InlineKeyboardMarkup
from PIL import Image, ImageDraw, ImageFont
import asyncio, os, time, aiohttp
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from asyncio import sleep
from pyrogram import filters, Client, enums
from pyrogram.enums import ParseMode


photo = [
"https://graph.org/file/9340f44e4a181b18ac663.jpg",
"https://graph.org/file/50037e072302b4eff55ba.jpg",
"https://graph.org/file/39f39cf6c6c68170f6bf2.jpg",
"https://graph.org/file/abf9931642773bc27ad7f.jpg",
"https://graph.org/file/60764ec9d2b1fda50c2d1.jpg",
"https://graph.org/file/a90c116b776c90d58f5e8.jpg",
"https://graph.org/file/b2822e1b60e62caa43ceb.jpg",
"https://graph.org/file/84998ca9871e231df0897.jpg",
"https://graph.org/file/6c5493fd2f6c403486450.jpg",
"https://graph.org/file/9dd91a4a794f15e5dadb3.jpg",
"https://graph.org/file/0a2fb6e502f6c9b6a04ac.jpg",
"https://graph.org/file/774380facd73524f27d26.jpg"
]


@app.on_message(filters.new_chat_members, group=2)
async def join_watcher(_, message):    
    chat = message.chat
    link = await app.export_chat_invite_link(message.chat.id)
    for members in message.new_chat_members:
        if members.id == app.id:
            count = await app.get_chat_members_count(chat.id)

            msg = (
                f"📝 ᴍᴜsɪᴄ ʙᴏᴛ ᴀᴅᴅᴇᴅ ɪɴ ᴀ ɴᴇᴡ ɢʀᴏᴜᴘ\n\n"
                f"____________________________________\n\n"
                f"📌 ᴄʜᴀᴛ ɴᴀᴍᴇ: {message.chat.title}\n"
                f"🍂 ᴄʜᴀᴛ ɪᴅ: {message.chat.id}\n"
                f"🔐 ᴄʜᴀᴛ ᴜsᴇʀɴᴀᴍᴇ: @{message.chat.username}\n"
                f"🛰 ᴄʜᴀᴛ ʟɪɴᴋ: [ᴄʟɪᴄᴋ]({link})\n"
                f"📈 ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀs: {count}\n"
                f"🤔 ᴀᴅᴅᴇᴅ ʙʏ: {message.from_user.mention}"
            )
            await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=msg, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"sᴇᴇ ɢʀᴏᴜᴘ👀", url=f"{link}")]
         ]))



@app.on_message(filters.left_chat_member)
async def on_left_chat_member(_, message: Message):
    if (await app.get_me()).id == message.left_chat_member.id:
        remove_by = message.from_user.mention if message.from_user else "**بەکارهێنەری نەناسراو**"
        title = message.chat.title
        username = f"@{message.chat.username}" if message.chat.username else "**گرووپی تایبەت**"
        chat_id = message.chat.id
        left = f"**✫ لێفتی گرووپ ✫\n\nناوی گرووپ : {title}\n\nئایدی گرووپ : {chat_id}\n\nدەرکرا لەلایەن : {remove_by}\n\nبۆت : @{app.username} **"
        await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=left)


#welcome
@app.on_message(filters.new_chat_members, group=3)
async def _greet(_, message):    
    chat = message.chat
    
    for member in message.new_chat_members:
        
            count = await app.get_chat_members_count(chat.id)

            msg = (
                f"**🫶🏻 بەخێربێی بۆ گرووپ {message.from_user.mention} 💘\n\n**"
                f"**🍻 ناوی گرووپ: {message.chat.title}\n**"
                f"**🧚🏻‍♀ یوزەری گرووپ: @{message.chat.username}\n**"
                f"**🚀 ئایدی: {member.id}\n**"
                f"**👻یوزەر: @{member.username}\n**"
                f"**🌚 ژمارەی ئەندام {count} 🍓**"
            )
            await app.send_photo(message.chat.id, photo=random.choice(photo), caption=msg, 
            reply_markup=InlineKeyboardMarkup(
                [
                    [    
                        InlineKeyboardButton(f"⦿ زیادم بکە بۆ کەناڵت ⦿", url=f"https://t.me/IQMCBOT?startchannel=true"),
                    ],[
                        InlineKeyboardButton(text="⦿ زیادم بکە بۆ گرووپت ⦿",
                                         url=f"https://t.me/IQMCBOT?startgroup=true"),
                  ]

              ],  

           ),
        )
