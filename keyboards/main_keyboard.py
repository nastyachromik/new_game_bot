from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from lexicon.commands_dict import LEXICON_RU

button_yes = KeyboardButton(text=LEXICON_RU['yes_button'])
button_no = KeyboardButton(text=LEXICON_RU['no_button'])
yes_no_keyboard = ReplyKeyboardMarkup(keyboard=[[button_yes, button_no]])

button_stone = KeyboardButton(text=LEXICON_RU['rock'])
button_paper = KeyboardButton(text=LEXICON_RU['paper'])
button_scissors = KeyboardButton(text=LEXICON_RU['scissors'])
choice_keyboard = ReplyKeyboardMarkup(keyboard=[[button_stone, button_paper], [button_scissors]])