import argparse
from dotenv import load_dotenv
import requests
import os
# from urllib.parse import urlparse, unquote
from save_foto import save_image


def fetch_spacex_last_launch(path, id_launch):
    url = f"https://api.spacexdata.com/v5/launches/{id_launch}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    images = data['links']['flickr']['original']
    if images != []:
        for i, image_url in enumerate(images):
            save_image(image_url, f'{path}/spacex_{i}.jpeg')
    else:
        print(f'Фотографии с запуска {id_launch} не публиковались')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Скачивает с сайта SpiceX')
    parser.add_argument('-id', '--id_launch',
                        help='ID запуска, без указания скачает последние',
                        default='latest')
    id_launch = parser.parse_args().id_launch
    load_dotenv()
    token_nasa = os.environ['API_TOKEN_NASA']
    path = 'Spice_X/'
    os.makedirs(path, exist_ok=True)
    fetch_spacex_last_launch(path, id_launch)
