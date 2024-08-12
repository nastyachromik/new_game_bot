from aiogram import Bot
from aiogram.types import BotCommand
from lexicon.commands_dict import LEXICON_COMMAND_RU
async def set_menu(bot: Bot):
    menu = [BotCommand(command=command, description=des) for command, des in LEXICON_COMMAND_RU.items()]
    await bot.set_my_commands(menu)