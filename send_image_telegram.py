import telegram
from dotenv import load_dotenv
import os
import time
import argparse
import random


def process_file(file_path):
    """
    Функция для обработки файла на размер в мегабайтах

    :param file_path: путь к файлу, который нужно обработать
    :return: None
    """
    max_size = 20971520  # 20 мегабайт в байтах (20*1024*1024)
    if os.path.getsize(file_path) > max_size:
        return
    if file_path.lower().endswith(('.jpg', '.png', '.gif', 'jpeg')):
        publish_img_tg(file_path)


def publish_img_tg(file_path):
    with open(file_path, 'rb') as image_file:
        bot.send_photo(chat_id=tg_chat_id, photo=image_file)
    time.sleep(delay)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Публикует изображения в тг'
    )
    parser.add_argument(
        '-t', '--time',
        help='Интервал между публикациями, в часах. 4 часа по умолчанию',
        default=4)
    delay = float(parser.parse_args().time) * 3600

    path = 'images'
    load_dotenv()
    telegram_api_key = os.environ['API_TELEGRAM']
    tg_chat_id = os.environ['TG_CHAT_ID']

    bot = telegram.Bot(token=telegram_api_key)

    while True:
        for root, dirs, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                process_file(file_path)
        files = os.listdir(path)
        random.shuffle(files)
        random_file = random.choice(files)
        random_file_path = os.path.join(path, random_file)
        process_file(random_file_path)
