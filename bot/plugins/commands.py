#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot import Translation, LOGGER # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error
import asyncio
from pyrogram.errors import FloodWait
from bot.bot import Bot
from bot import ADMINS, OWNER_ID, DISABLE_CHANNEL_BUTTON
from helper_func import encode, decode, get_messages

db = Database()

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = file_caption if file_caption != ("" or None) else ("<code>" + file_name + "</code>")
        try:
            await update.reply_cached_media(
                file_id,
                quote=True,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    'Developers', url="https://t.me/CrazyBotsz"
                                )
                        ]
                    ]
                )
            )
        except Exception as e:
            await update.reply_text(f"<b>Error:</b>\n<code>{e}</code>", True, parse_mode="html")
            LOGGER(__name__).error(e)
        return



    await bot.send_photo(
        chat_id=update.chat.id,
        photo="https://telegra.ph/file/fe403b72f9dd617f96441.jpg",
        caption=Translation.START_TEXT.format(
                update.from_user.mention),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⚙️𝙷𝙴𝙻𝙿", callback_data = "help")
                ],
                [
                    InlineKeyboardButton('🏘️𝙶𝚁𝙾𝚄𝙿', url='https://t.me/mv_mania'),
                    InlineKeyboardButton('🎬𝙲𝙷𝙰𝙽𝙽𝙴𝙻', url='https://t.me/BoX_0fFiCe')
                ],
                [
                    InlineKeyboardButton('🔎𝚄𝙿𝙳𝙰𝚃𝙴𝚂', url='https://t.me/MoviE_LinkS_0nlY'),
                    InlineKeyboardButton('🗃️𝚂𝙾𝚄𝚁𝙲𝙴', callback_data = "source")
                ]
            ]
        ), 
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('Auto Filter', callback_data = "autofilter"),
        InlineKeyboardButton('Vc Player 🚩', callback_data = "vcplayer")
    ],[
        InlineKeyboardButton('UFilters', callback_data = "filter"),
        InlineKeyboardButton('File Store', callback_data = "filestore")
    ],[
        InlineKeyboardButton('About', callback_data = "about")
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.text & ~ filters.command(["start","help","batch","genlink","cccurrent","userbotjoinchannel","channelplay","play","dplay","splay","player","skip","pause","resume","end","current","playlist","cresume","cplayer","cplaylist","cdplay","unset","csplay","cplay","pmpermit","gcast","userbotleaveall","userbotjoin","admincache","remall","rem","viewfilters","filter","info","set","sets","id","status"]) & filters.private & ~ filters.me)
async def note(bot, update):
    buttons = [[
        InlineKeyboardButton('🏡𝙼𝙰𝙸𝙽 𝙲𝙷𝙰𝙽𝙽𝙴𝙻', url='https://t.me/MoviE_LinkS_0nlY'),
        InlineKeyboardButton('📽️𝙼𝙾𝚅𝙸𝙴 𝙲𝙷𝙰𝙽𝙽𝙴𝙻', url='https://t.me/BoX_0fFiCe')
    ],[
        InlineKeyboardButton('🤔𝙷𝙾𝚆 𝚃𝙾 𝚁𝙴𝚀?', url='https://t.me/MoviE_LinkS_0nlY/5')
    ],[
        InlineKeyboardButton('𝚂𝙷𝙰𝚁𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙵𝚁𝙸𝙴𝙽𝙳𝚂😍', url='https://t.me/share/url?url=💯%20𝙽𝙾%201%20𝙼𝙾𝚅𝙸𝙴%20𝚁𝙴𝚀𝚄𝙴𝚂𝚃𝙸𝙽𝙶%20𝙶𝚁𝙾𝚄𝙿%20𝙸𝙽%20𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼%20✅%20%0A%0A𝙹𝙾𝙸𝙽%20𝙰𝙽𝙳%20𝚁𝙴𝚀%20𝚈𝙾𝚄𝚁%20𝙵𝙰𝚅𝙾𝚁𝙸𝚃𝙴%20𝙼𝙾𝚅𝙸𝙴𝚂%20𝚁𝙸𝙶𝙷𝚃%20𝙽𝙾𝚆%20%0A%0A💠%20➠%20𝙶𝚁𝙾𝚄𝙿%20:-%20@Mv_Mania%20%0A💠%20➠%20𝙲𝙷𝙰𝙽𝙽𝙴𝙻%20:-%20@BoX_0fFiCe%20%0A💠%20➠%20𝙲𝙷𝙰𝙽𝙽𝙴𝙻%20:-%20@MoviE_LinkS_0nlY')
  
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)

    if update.from_user.id not in ADMINS:
        await bot.send_message(
            chat_id=update.chat.id,
            text=Translation.REQ_IN_PM,
            reply_markup=reply_markup,
            parse_mode="html",
            reply_to_message_id=update.message_id
        )
