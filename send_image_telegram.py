import telegram
from dotenv import load_dotenv
import os
import time
import argparse
import random


# Функция для обработки файла
def process_file(file_path):
    max_size = 20971520  # 20 мегабайт в байтах (20*1024*1024)
    if os.path.getsize(file_path) > max_size:
        return
    if file_path.lower().endswith(('.jpg', '.png', '.gif', 'jpeg')):
        print(file_path)
        pubilish_img_tg(file_path)


def pubilish_img_tg(file_path):
    with open(file_path, 'rb') as image_file:
        bot.send_photo(chat_id=chat_id, photo=image_file)
        time.sleep(delay)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Публикует изображения в тг')
    parser.add_argument('-t', '--time',
                        help='Интервал между публикациями, в часах. 4 часа по умолчанию',
                        default=4)
    delay = float(parser.parse_args().time) * 3600  # в 1 часе 3600 секунд

    path = 'images'
    load_dotenv()
    telegram_api_key = os.environ['API_TELEGRAM']
    chat_id = os.environ['CHAT_ID']

    bot = telegram.Bot(token=telegram_api_key)

    while True:
        for root, dirs, files in os.walk(path):
            for file in files:
                # Получаем полный путь к файлу
                file_path = os.path.join(root, file)
                # проверка, что это изображение и вес
                process_file(file_path)
        # Получаем список файлов в папке
        files = os.listdir(path)
        # Перемешиваем список файлов
        random.shuffle(files)
        # Выбираем случайный файл из перемешанного списка
        random_file = random.choice(files)
        # Получаем полный путь к выбранному файлу
        random_file_path = os.path.join(path, random_file)
        process_file(random_file_path)
