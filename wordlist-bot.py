import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import hbold, text
from aiogram.dispatcher.filters import Text
from config import token
from main import get_words, get_phrase


# Configure loggin
logging.basicConfig(level=logging.INFO)


# Initialize bot and dispatcher
bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    # This handler will be called when user sends '/start' or '/help' command
    await message.reply("Hi!\nI'm Wordlist-bot! I want to help you learn and remember new words.\nPowered by aiogram.")
    start_buttons = ["Get new word", "Get new random phrase", "/start"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)
    await message.answer("Choose commands", reply_markup=keyboard)

# Function for sending random word from dictionary
@dp.message_handler(Text(equals='Get new word'))
async def get_new_words(message: types.Message):
    # This handler will be called when user sends 'Get new word' command
    wordlist = get_words()
    # For get word and url from wordlist
    word = wordlist[0]
    url = wordlist[1]
    # The user receives a new word and a link to it in the dictionary
    word = f"{text(hbold('New english word:'), text(word))}\n" \
           f"{text(url)}\n"
    await message.answer(word)

# Function for sending random phrase from dictionary
@dp.message_handler(Text(equals='Get new random phrase'))
async def get_new_phrase(message: types.Message):
    # This handler will be called when user sends 'Get new random phrase' command
    phrase = get_phrase()
    # The user receives a new word and a link to it in the dictionary
    words = f"{text(hbold('New english 12 words phrase:'))}\n" \
            "{} / {} / {} / {} / {} / {} / {} / {} / {} / {} / {} / {}".format(*phrase).upper()
    await message.answer(words)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
