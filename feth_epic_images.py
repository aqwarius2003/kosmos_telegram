import requests
import os
from datetime import datetime
from save_foto import save_image
from dotenv import load_dotenv
import argparse


def epic_download_images(token_nasa, path, data_string=None):  # если даты нет - то качает последние
    os.makedirs(path, exist_ok=True)  # Создаем папку, если ее нет
    payload = {'api_key': token_nasa}
    if data_string is None:  # ищем последнюю публикацию
        url = 'https://api.nasa.gov/EPIC/api/natural/all'
        response = requests.get(url, params=payload)
        response.raise_for_status()
        data_string = response.json()[0]['date']  # последнюю дату публикации
    data = datetime.strptime(data_string, '%Y-%m-%d').date()
    print(data)
    url = f"https://api.nasa.gov/EPIC/api/natural/date/{str(data)}"
    response = requests.get(url, params=payload)  # Исправлено: передаем параметры запроса как словарь
    response.raise_for_status()
    response_images = response.json()
    print(response_images)

    for image_n in response_images:
        image_name = image_n['image']
        image_url = (
            "https://epic.gsfc.nasa.gov/archive/natural/"
            f"{str(data.strftime('%Y/%m/%d'))}/png/{image_name}.png"
        )
        save_image(image_url, f'{path}{image_name}.png', payload)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Скачивает EPIC фото с сайта NASA')
    parser.add_argument('-d', '--date',
                        help='Дата фотографий, формат %Y-%m-%d, без указания скачает последние'
                        )
    data = parser.parse_args().date
    load_dotenv()
    token_nasa = os.environ['API_TOKEN_NASA']
    path = 'nasa_epic_png/'
    epic_download_images(token_nasa, path, data)
