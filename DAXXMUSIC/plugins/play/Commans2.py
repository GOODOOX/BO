#test
import asyncio
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.types import (Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery)
from DAXXMUSIC import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from youtubesearchpython.__future__ import VideosSearch
from typing import Union
from pyrogram.types import InputMediaPhoto, InputMediaVideo
from DAXXMUSIC import app
import config
from config import BANNED_USERS, BAND
from config import OWNER_ID
from DAXXMUSIC import Telegram, YouTube, app
from DAXXMUSIC.misc import SUDOERS



@app.on_callback_query(filters.regex("tt"))
async def gtt(_, query: CallbackQuery):
    
    if query.from_user.id in BAND:
        return await query.answer("ببورن، داواکارییەکە بۆ ئێوە نییە !", show_alert=True)
        
    await query.edit_message_text(
        f"""\n\n**╭── • [𝗔𝗹𝗶𝗻𝗮 𝗠𝘂𝘀𝗶𝗰](t.me/MGIMT) • ──╮**\n\n** ✧ فەرمانی پەخشکردن لە کەناڵ**\n\n**• پ کەناڵ + ناوی گۆرانی یان ڕیپلەی لینك** \n-› بۆ پەخشکردنی گۆرانی لە کەناڵ\n\n**• وەستان**\n-› بۆ وەستانی هەموو گۆرانیەکان کۆتایی هاتن\n\n**• دواتر**\n-› بۆ گۆڕینی گۆرانی بۆ گۆرانی دواتر\n\n**• وەستانی کاتی**\n-› بۆ وەستانی پەخشکردن بۆ ماوەیەکی کاتی\n\n**• دەستپێکردنەوە**\n-› بۆ دەستپێکردنەوەی پەخشکردن کاتێ وەستاوە\n\n**╰── • [𝗔𝗹𝗶𝗻𝗮 𝗠𝘂𝘀𝗶𝗰](t.me/MGIMT) • ──╯**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "", callback_data="fft"),
                    InlineKeyboardButton(
                        "”﮼احساس“", url=f"https://t.me/EHS4SS")
                ], [
                InlineKeyboardButton(
                    "گەڕانەوە", callback_data="am"),
                InlineKeyboardButton(
                    "داخستن", callback_data="close"),
            ], [

                InlineKeyboardButton(
                    "", callback_data="kdm"),
            ], [

                InlineKeyboardButton(
                    "◌sᴏᴜʀᴄᴇ ᴀʟɪɴᴀ◌", callback_data=f"fft")

            ],
            ]
        ),
    )


@app.on_callback_query(filters.regex("am"))
async def gtt(_, query: CallbackQuery):
    
    if query.from_user.id in BAND:
        return await query.answer("ببورن، داواکارییەکە بۆ ئێوە نییە !", show_alert=True)
        
    await query.edit_message_media(
        InputMediaVideo(
            "https://graph.org/file/0a648eba9c9163765c265.mp4", None,
            "**✧ بەخێربێن بۆ فەرمانی بۆتی ئەلینا\n\n•هەندێك دوگمە هەن بۆ فێربوون\n\n• گەشەپێدەری بۆت -› @IQ7amo\n• کەناڵی بۆت -› @MGIMT**"),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "فێرکاری پەخشکردن لە پلاتفۆڕمەکان", callback_data=f"ko"),
                ], [
                InlineKeyboardButton(
                    "فەرمانی گرووپ", callback_data=f"ddd"),

                InlineKeyboardButton(
                    "فەرمانی کەناڵ", callback_data=f"tt"),

            ], [
                InlineKeyboardButton(
                    "گرێدانی کەناڵ", callback_data=f"cha"),

                InlineKeyboardButton(
                    "فەرمانی گەڕان", callback_data=f"don"),
            ], [

                InlineKeyboardButton(
                    "فەرمانی خزمەتگوزاری", callback_data=f"kdm"),
            ], [

                InlineKeyboardButton(
                    "نوێکارییەکانی ئەلینا 🥢", url=f"https://t.me/MGIMT"),
            ],
            ]
        ),
    )


@app.on_callback_query(filters.regex("amm"))
async def gtt(_, query: CallbackQuery):
    
    if query.from_user.id in BAND:
        return await query.answer("ببورن، داواکارییەکە بۆ ئێوە نییە !", show_alert=True)
        
    await query.edit_message_media(
        InputMediaVideo(
            "https://graph.org/file/0a648eba9c9163765c265.mp4", None,
            "**✧ بەخێربێن بۆ فەرمانی بۆتی ئەلینا\n\n• فەرمانەکان بە دوگمەن فێریان بە\n\n• 𝖣𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋 -› [𝑴𝒖𝒉𝒂𝒎𝒎𝒆𝒅](t.me/IQ7amo)\n• 𝖢𝗁𝖺𝗇𝗇𝖾𝗅 -› [𝑺𝒐𝒖𝒓𝒄𝒆 𝑨𝒍𝒊𝒏𝒂](t.me/MGIMT)**"),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "فێرکاری پەخشکردن لە پلاتفۆڕمەکان", callback_data=f"ko"),
                ], [
                InlineKeyboardButton(
                    "فەرمانی گرووپ", callback_data=f"ddd"),

                InlineKeyboardButton(
                    "فەرمانی کەناڵ", callback_data=f"tt"),

            ], [
                InlineKeyboardButton(
                    "گرێدانی کەناڵ", callback_data=f"cha"),

                InlineKeyboardButton(
                    "فەرمانی گەڕان", callback_data=f"don"),
            ], [

                InlineKeyboardButton(
                    "فەرمانی خزمەتگوزاری", callback_data=f"kdm"),
            ], [

                InlineKeyboardButton(
                    "نوێکارییەکانی ئەلینا 🥢", url=f"https://t.me/MGIMT"),
            ],
            ]
        ),
    )


@app.on_callback_query(filters.regex("sound"))
async def gtt(_, query: CallbackQuery):
    
    if query.from_user.id in BAND:
        return await query.answer("ببورن، داواکارییەکە بۆ ئێوە نییە !", show_alert=True)
        
    await query.edit_message_media(
        InputMediaPhoto(
            "https://telegra.ph/file/13308564f92131709856c.jpg",
            "**✶ بەخێربێن بۆ بەشی پەخشی 𝖲𝗈𝗎𝗇𝖽𝖢𝗅𝗈𝗎𝖽 ♪**\n\n**• فەرمانی پەخشکردن بنووسە لەگەڵ لینکی ساوند کڵاود**\n\n**• نموونە :** [ `پلەی https://soundcloud.app.goo.gl/asiXLu19szSrVLFo9` ]\n\n-› [𝖲𝗈𝗎𝗇𝖽𝖢𝗅𝗈𝗎𝖽 ♪](t.me/EHS4SS)"),
        reply_markup=InlineKeyboardMarkup(
            [
                [

                    InlineKeyboardButton(
                        "گەڕانەوە", callback_data=f"ko")
                ], [

                InlineKeyboardButton(
                    "◌sᴏᴜʀᴄᴇ ᴀʟɪɴᴀ◌", callback_data=f"fft")

            ],
            ]
        ),
    )


@app.on_callback_query(filters.regex("cha"))
async def gtt(_, query: CallbackQuery):
    
    if query.from_user.id in BAND:
        return await query.answer("ببورن، داواکارییەکە بۆ ئێوە نییە !", show_alert=True)
        
    await query.edit_message_media(
        InputMediaVideo(
            "https://graph.org/file/31a48bd8769b47d9b2db8.mp4", None,
            "**✧ بەخێربێن بۆ فەرمانی بۆتی ئەلینا**\n**◌پەخشکردن لە کەناڵ چەند هەنگاوێکی پێویستە◌ :**\n\n**1 -› بۆت زیادبکە کەناڵ و بیکە بە ئەدمین**\n**2 -› بگەڕێوە گرووپ و بنووسە ⇣**\n{ **گرێدان + یوزەری کەناڵ** }\n**3 -› دەست بدە لە فەرمانی پەخشکردن بۆ زانینی پەخشکردن**\n\n**✶ پەیوەندی کردن - @IQ7amo**"),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "فەرمانی پەخشکردن لە کەناڵ", callback_data=f"tt"),

                ],
            ]
        ),
    )


@app.on_callback_query(filters.regex("kdm"))
async def gtt(_, callback_query: CallbackQuery):
    
    if callback_query.from_user.id in BAND:
        return await query.answer("ببورن، داواکارییەکە بۆ ئێوە نییە !", show_alert=True)
        
    await query.edit_message_media(
        InputMediaPhoto(
            "https://graph.org/file/3cd7d168316e95c6dbfbd.jpg",
            "**✧ بەخێربێن بۆ فەرمانی خزمەتگوزاری بۆتی ئەلینا\n- هەبوونی کۆمەڵێ فەرمانی جوان ↓\n\n-› گۆرانی\n-› وێنەی کچان\n-› ڤیدیۆ\n-› ق\n-› وەسف\n-› وتە\n-› کەپڵ\n-› وێنەکەم\n-› سەرۆکی گرووپ\n-› بایۆ\n-› گرووپ\n\n✶ جۆینی کەناڵ بکە بۆ بینینی وتە و پۆستی شاز\n-› @EHS4SS**"),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "گەڕانەوە", callback_data=f"am"),
                ], [

                InlineKeyboardButton(
                    "• 𝑷𝒓𝒐𝒑𝒆𝒓𝒕𝒚 𝑨𝒍𝒊𝒏𝒂 •", url=f"t.me/EHS4SS")

            ],
            ]
        ),
    )
