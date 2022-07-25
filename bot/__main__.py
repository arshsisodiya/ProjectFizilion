# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" bot start point """

from importlib import import_module
from sys import argv
from asyncio import sleep
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
from bot import LOGS, bot, BOTLOG, BOTLOG_CHATID, ALIVE_NAME, bot_VERSION, repo_lenk
from bot.modules import ALL_MODULES
from telethon import __version__, version
from platform import python_version, uname

INVALID_PH = '\nERROR: The Phone No. entered is INVALID' \
             '\n Tip: Use Country Code along with number.' \
             '\n or check your phone number and try again !'

try:
    bot.start()
except PhoneNumberInvalidError:
    print(INVALID_PH)
    exit(1)

for module_name in ALL_MODULES:
    imported_module = import_module("bot.modules." + module_name)

LOGS.info(f"You are running Project Fizilion on {repo_lenk}")

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
output = (
    "` =============================== `\n"
    f"`Fizilion is Up and Running.... `\n"
    f"`=============================== `\n"
    f"•`Telethon       : v{version.__version__} `\n"
    f"•`Python         : v{python_version()} `\n"
    f"•`User           : {DEFAULTUSER} `\n"
    f"•`Fizilion       : {bot_VERSION} `\n"
)

async def start():
    if BOTLOG:
        try:
            await bot.send_message(
                BOTLOG_CHATID, output
                        )
        except:
            None
    else:
        pass
bot.loop.run_until_complete(start())

LOGS.info(
    "Congratulations, your bot is now running !! Test it by typing .alive / .on in any chat."
    "If you need assistance, head to https://t.me/ProjectHelios")

sleep(300)
bot.run_until_disconnected()
bot.run_until_disconnected()
