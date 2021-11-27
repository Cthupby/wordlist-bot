import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import hbold, text
from aiogram.dispatcher.filters import Text
from config import token
from main import get_words

# Configure loggin
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    # This handler will be called when user sends '/start' or '/help' command
    await message.reply("Hi!\nI'm Wordlist-bot! I want to help you learn and remember new words.\nPowered by aiogram.")

    start_buttons = ["Get new word", "/start"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)
    await message.answer("Choose commands", reply_markup=keyboard)

# Function for sending random word from dictionary
@dp.message_handler(Text(equals='Get new word'))
async def get_new_words(message: types.Message):
    # This handler will be called when user sends 'Get new word' command
    wordlist = get_words()
    # For get word and url from wordlist
    wordr = wordlist[0]
    worde = wordlist[1]
    url = wordlist[2]
    # The user receives a new word and a link to it in the dictionary
    word =  f"{text(hbold('Русский:'), text(wordr))}\n" \
	    f"{text(hbold('New english word:'), text(worde))}\n" \
            f"{text(url)}\n"
    await message.answer(word)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
