import argparse
import requests
import os
from save_foto import save_image


def fetch_spacex_last_launch(path_images_spicex, launch_id):
    url = f"https://api.spacexdata.com/v5/launches/{launch_id}"
    response = requests.get(url)
    response.raise_for_status()
    response_data = response.json()
    images = response_data['links']['flickr']['original']
    if images:
        for i, image_url in enumerate(images):
            save_image(image_url, f'{path_images_spicex}/spacex_{i}.jpeg')
    else:
        print(f'Фотографии с запуска {launch_id} не публиковались')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Скачивает с сайта SpiceX')
    parser.add_argument('-id', '--id_launch',
                        help='ID запуска, без указания скачает последние',
                        default='latest')
    id_launch = parser.parse_args().id_launch
    path = 'images/'
    os.makedirs(path, exist_ok=True)
    fetch_spacex_last_launch(path, id_launch)
