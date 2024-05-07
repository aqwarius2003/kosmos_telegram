import requests
import os
from dotenv import load_dotenv
from save_foto import save_image, get_extension_file
import argparse


def apod_download_images(path, images_count, nasa_token):
    os.makedirs(path, exist_ok=True)
    payload = {'api_key': nasa_token, 'count': images_count}
    url_apod = 'https://api.nasa.gov/planetary/apod'
    response = requests.get(url_apod, params=payload)
    response.raise_for_status()
    response_images = response.json()
    print(response_images)
    for n, image_n in enumerate(response_images):
        image_url = image_n['url']
        image_txt = image_n['explanation']
        image_extension = get_extension_file(image_url)
        save_image(image_url,
                   f'{path}apod_{n}{image_extension}')
        with open(f'{path}apod_{n}{image_extension}.txt', 'w', encoding='utf-8') as file:
            file.write(image_txt)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Скачивает случайные APOD материалы с сайта NASA')
    parser.add_argument('-c', '--count',
                        help='Количество, по умолчанию 2',
                        default=2)
    images_count = parser.parse_args().count
    load_dotenv()
    nasa_token = os.environ['API_TOKEN_NASA']
    path = 'nasa_apod/'
    apod_download_images(path, images_count, nasa_token)
