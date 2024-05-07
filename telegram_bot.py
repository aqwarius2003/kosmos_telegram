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
    # print(updates[0])
    # print(bot.get_me())
    bot.send_message(text='Hello world!!!5', chat_id=chat_id)
    # updates = bot.get_updates()
    # bot.send_message(chat_id=chat_id,
    #                  text='<b>bold</b> <i>italic</i> <a href="http://google.com">link</a>.',
    #                  parse_mode=telegram.ParseMode.HTML)
    path = 'nasa_apod/'
    with open(f'{path}apod_0.jpg', 'rb') as image_file:
        # Отправьте изображение в канал
        bot.send_photo(chat_id=chat_id, photo=image_file)