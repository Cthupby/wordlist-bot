# Wordlist bot
Telegram bot made with [aiogram](https://docs.aiogram.dev/en/latest/) and [pandas](https://pandas.pydata.org/docs/) that can send words from dictionary on demand.

## Project Technologies:

1. Web-framework: [Aiogram](https://docs.aiogram.dev/en/latest/), [Flask](https://flask.palletsprojects.com/en/2.0.x/)
2. Database: [Pandas](https://pandas.pydata.org/docs/), [SQLAlchemy](https://www.sqlalchemy.org/)

## Usage with [Virtualenv](https://virtualenv.pypa.io/en/latest/)
1. Clone the wordlist-bot
2. Create and activate virtual environment  
   ```python -m virualenv venv```  
   ```source ./venv/bin/activate```
3. Install the required libraries  
  ```pip install -r requirements.txt```
4. Enter your token from Botfather to config  
5. For using worlist in terminal enter  
   ```python main.py```  
   For using worlist bot in telegram  
   ```python wordlist-bot.py```  

## Usage with [Docker](https://docs.docker.com/)
1. Clone the wordlist-bot
2. Create image  
   ```docker build -t wordlist_bot .```  
3. Create and activate coontainer  
   ```docker run -p 8000:8000 wordlist_bot```
5. Enter your token from Botfather to config    

## Realization
This bot in telegram - @Newwword_bot
