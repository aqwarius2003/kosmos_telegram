import requests
import os
from datetime import datetime
from save_foto import save_image
from dotenv import load_dotenv
import argparse


def epic_download_images(token_nasa, path_images, date_photo=None):
    payload = {'api_key': token_nasa}
    if not date_photo:
        url = 'https://api.nasa.gov/EPIC/api/natural/all'
        response = requests.get(url, params=payload)
        response.raise_for_status()
        date_photo = response.json()[0]['date']

    date_photos_epic = datetime.strptime(date_photo, '%Y-%m-%d').date()
    url = f"https://api.nasa.gov/EPIC/api/natural/date/{str(date_photos_epic)}"
    response = requests.get(url, params=payload)
    response.raise_for_status()
    response_images = response.json()

    for image_n in response_images:
        image_name = image_n['image']
        image_url = (
            "https://epic.gsfc.nasa.gov/archive/natural/"
            f"{str(date_photos_epic.strftime('%Y/%m/%d'))}/png/{image_name}.png"
        )
        save_image(image_url, f'{path_images}{image_name}.png', payload)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Скачивает EPIC фото с сайта NASA'
    )
    parser.add_argument(
        "-d",
        "--date",
        help="Дата фотографий, формат %Y-%m-%d, '"
             "'без указания скачает последние",
    )
    date_photos = parser.parse_args().date
    load_dotenv()
    token_nasa = os.environ['API_TOKEN_NASA']
    path = 'images/'
    os.makedirs(path, exist_ok=True)
    epic_download_images(token_nasa, path, date_photos)
