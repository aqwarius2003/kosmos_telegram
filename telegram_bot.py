import telegram
from dotenv import load_dotenv
import os
ID_CANNEL='omg_spice'



if __name__=='__main__':
    load_dotenv()
    telegram_api_key = os.environ['API_TELEGRAM']
    chat_id = os.environ['CHAT_ID']
    bot = telegram.Bot(token=telegram_api_key)
    updates = bot.get_updates()
    print(updates[0])
    print(bot.get_me())
    bot.send_message(text='Hello world!!!', chat_id=chat_id)
    updates = bot.get_updates()