from loguru import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import hbold, text
from aiogram.dispatcher.filters import Text
from config import token
from main import get_words, get_phrase


''' Configure loggin. '''
logging.basicConfig(level=logging.INFO)


''' Initialize bot and dispatcher. '''
bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message) -> None:
    '''
    This handler will be called when user sends '/start' command.
    '''
    text = "Hi!\nI'm Newwword-bot! I want to help you learn and" \
           " remember new words.\nMade with aiogram and pandas."
    await message.reply(text)
    start_buttons = ["New word", "New random phrase", "/start"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)
    await message.answer("Choose commands", reply_markup=keyboard)


@dp.message_handler(commands=['help'])
async def send_help(message: types.Message) -> None:
    '''
    This handler will be called when user sends '/help' command
    '''
    start_buttons = ["New word", "New random phrase", "/start"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)
    await message.answer("Choose commands", reply_markup=keyboard)


@dp.message_handler(Text(equals='New word'))
async def get_new_words(message: types.Message) -> None:
    '''
    Function for sending random word from dictionary.
    This handler will be called when user sends 'Get new word' command.
    '''
    wordlist = get_words()
    '''
    Get word and url from wordlist.
    '''
    word = wordlist[0]
    url = wordlist[1]
    '''
    User receives a new word and a link to it in the dictionary.
    '''
    word = f"{text(hbold('New english word:'), text(word))}\n" \
           f"{text(url)}\n"
    await message.answer(word)
    await message.answer("Success! - /help")


@dp.message_handler(Text(equals='New random phrase'))
async def get_new_phrase(message: types.Message) -> None:
    '''
    Function for sending random phrase from dictionary.
    This handler will be called when user sends
    'Get new random phrase' command.
    '''
    phrase = get_phrase()
    '''
    The user receives a new word and a link to it in the dictionary.
    '''
    words = f"{text(hbold('New english mnemonic phrase:'))}\n" \
            "{} / {} / {} / {} / {} / {} " \
            "/ {} / {} / {} / {} / {} / {}".format(*phrase)
    await message.answer(words)
    await message.answer("Success! - /help")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
