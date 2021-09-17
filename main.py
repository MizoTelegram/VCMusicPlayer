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
from pyrogram import Client, idle
import os
from config import Config
from utils import mp
from pyrogram.raw import functions, types

CHAT=Config.CHAT
bot = Client(
    "Musicplayer",
    Config.API_ID,
    Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins=dict(root="plugins")
)
if not os.path.isdir("./downloads"):
    os.makedirs("./downloads")
async def main():
    async with bot:
        await mp.start_radio()

bot.run(main())
bot.start()
bot.send(
    functions.bots.SetBotCommands(
        commands=[
            types.BotCommand(
                command="start",
                description="Bot a nung leh nun loh enna"
            ),
            types.BotCommand(
                command="help",
                description="Bot-in a puih theihna te"
            ),
            types.BotCommand(
                command="play",
                description="Hla (MP3) YouTube/AudioFile aṭanga na"
            ),
            types.BotCommand(
                command="dplay",
                description="Deezer aṭanga Hla Play-na"
            ),
            types.BotCommand(
                command="player",
                description="Hla Play lai mêk enna"
            ),
            types.BotCommand(
                command="playlist",
                description="Playlist enna"
            ),
            types.BotCommand(
                command="skip",
                description="Hla play laia Skip-na"
            ),
            types.BotCommand(
                command="join",
                description="VoiceChat Join tirna"
            ),
            types.BotCommand(
                command="leave",
                description="VoiceChat Leave tirna"
            ),
            types.BotCommand(
                command="vc",
                description="VoiceChat join lai enna"
            ),
            types.BotCommand(
                command="stop",
                description="Hla Play lai mek tihtawp na"
            ),
            types.BotCommand(
                command="radio",
                description="Radio/Live Stream Start-na"
            ),
            types.BotCommand(
                command="stopradio",
                description="Radio/Live Stream tih tawpna"
            ),
            types.BotCommand(
                command="replay",
                description="A bul aṭanga Play lehna"
            ),
            types.BotCommand(
                command="clean",
                description="RAW Files Clear-na"
            ),
            types.BotCommand(
                command="pause",
                description="Hla Pause na"
            ),
            types.BotCommand(
                command="resume",
                description="Pause lai mek Resume lehna"
            ),
            types.BotCommand(
                command="mute",
                description="VoiceChat mute na"
            ),
            types.BotCommand(
                command="volume",
                description="Set volume between 0-200"
            ),
            types.BotCommand(
                command="unmute",
                description="VoiceChat unmute leh na"
            ),
            types.BotCommand(
                command="restart",
                description="Restart the bot"
            )
        ]
    )
)

idle()
bot.stop()
