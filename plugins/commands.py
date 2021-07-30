#MIT License

#Copyright (c) 2021 Zaute Km

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters
import signal
from utils import USERNAME, FFMPEG_PROCESSES, mp
from config import Config
import os
import sys
import subprocess
import asyncio
from signal import SIGINT
U=USERNAME
CHAT=Config.CHAT
msg=Config.msg
HOME_TEXT = "<b>Hello, [{}](tg://user?id={})\n\nKei hi 24×7 Mizo Radio/Music Player ka ni e!</b>"
HELP = """
**User Commands:**
▷/play **[hla hming]/[yt link]**: Audio file Reply Rawh!
▷/dplay **[hla hming]:** Deezer Music aṭanga play na.
▷/player: Hla play mek enna.
▷/help: Min Commands theihna tur.
▷/playlist: Playlists enna.

**Admin Commands:**
▷/skip **[n]** ...  Skip current or n where n >= 2
▷/join: Join voice chat.
▷/leave: Leave current voice chat
▷/vc: Check which VC is joined.
▷/stop: Stop playing.
▷/radio: Start Radio.
▷/stopradio: Stops Radio Stream.
▷/replay: Play from the beginning.
▷/clean: Remove unused RAW PCM files.
▷/pause: Pause playing.
▷/resume: Resume playing.
▷/volume: Change volume(0-200).
▷/mute: Mute in VC.
▷/unmute: Unmute in VC.
▷/restart: Restarts the Bot.
"""



@Client.on_message(filters.command(['start', f'start@{U}']))
async def start(client, message):
    buttons = [
        [
        InlineKeyboardButton("🔥 Source Code 🔥", url='https://github.com/ZauteKm/tgvc-RadioBot'),
    ],
    [
        InlineKeyboardButton('👥 Group', url='https://t.me/mizotelegram/106'),
        InlineKeyboardButton('Channel 📢', url='https://t.me/joinchat/0io4YMY-xms1M2Q9'),
    ],
    [
        InlineKeyboardButton('🆘 Help & Commands 🆘', callback_data='help'),

    ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply(HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)
    await message.delete()



@Client.on_message(filters.command(["help", f"help@{U}"]))
async def show_help(client, message):
    buttons = [
        [
            InlineKeyboardButton("🔥 Source Code 🔥", url='https://github.com/LushaiMusic/VCMusicPlayer'),
        ],
        [
            InlineKeyboardButton('👥 Group', url='https://t.me/mizotelegram'),
            InlineKeyboardButton('Channel 📢', url='https://t.me/infotelmizo'),
        ],
        [
            InlineKeyboardButton('👉 Deploy your Own ⚠️', url='https://t.me/c/1481808444/131'),
        
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_text(
        HELP,
        reply_markup=reply_markup
        )
    await message.delete()
@Client.on_message(filters.command(["restart", f"restart@{U}"]) & filters.user(Config.ADMINS))
async def restart(client, message):
    await message.reply_text("🔄 Restarting...")
    await message.delete()
    process = FFMPEG_PROCESSES.get(CHAT)
    if process:
        try:
            process.send_signal(SIGINT)
        except subprocess.TimeoutExpired:
            process.kill()
    os.execl(sys.executable, sys.executable, *sys.argv)
