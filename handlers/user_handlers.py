from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from services.functions import random_stuff
from lexicon.commands_dict import LEXICON_RU
from keyboards.main_keyboard import yes_no_keyboard, choice_keyboard
router = Router()

@router.message(CommandStart())
async def start_func(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=yes_no_keyboard)

@router.message(Command(commands='help'))
async def help_func(message: Message):
    await message.answer(text=LEXICON_RU['/help'], reply_markup=yes_no_keyboard )
@router.message(F.text == LEXICON_RU['yes_button'])
async def game_func(message: Message):
    await message.answer(text=LEXICON_RU['yes'], reply_markup=choice_keyboard)

@router.message(F.text == LEXICON_RU['no_button'])
async def stop_func(message: Message):
    await message.answer(text=LEXICON_RU['no'], reply_markup=yes_no_keyboard)

@router.message(F.text.in_([LEXICON_RU['rock'],
                            LEXICON_RU['paper'],
                            LEXICON_RU['scissors']]))
async def main_func(message: Message):
    rand = random_stuff()
    user_stuff = message.text
    await message.answer(f'{LEXICON_RU["bot_choice"]}: {rand}')
    if rand == message.text:
        await message.answer(text=LEXICON_RU['nobody_won'], reply_markup=yes_no_keyboard)
    elif user_stuff == LEXICON_RU['paper'] and rand == LEXICON_RU['rock'] or user_stuff == LEXICON_RU['scissors'] and rand == LEXICON_RU['paper'] or user_stuff == LEXICON_RU['rock'] and rand == LEXICON_RU['scissors']:
        await message.answer(text=LEXICON_RU['user_won'], reply_markup=yes_no_keyboard)
    else:
        await message.answer(text=LEXICON_RU['bot_won'], reply_markup=yes_no_keyboard)