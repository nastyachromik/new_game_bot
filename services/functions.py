import random
from lexicon.commands_dict import LEXICON_RU
def random_stuff():
    return random.choice([LEXICON_RU['paper'], LEXICON_RU['scissors'], LEXICON_RU['paper']])