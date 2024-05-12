import requests
import os
from datetime import datetime
from save_foto import save_image
from dotenv import load_dotenv
import argparse


def epic_download_images(token_nasa, path_images, photo_date=None):
    payload = {'api_key': token_nasa}
    date_photos_epic = datetime.strptime(photo_date, '%Y-%m-%d').date()
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


def get_latest_photo_date(api_key):
    payload = {'api_key': api_key}
    url = 'https://api.nasa.gov/EPIC/api/natural/all'
    response = requests.get(url, params=payload)
    response.raise_for_status()
    photo_date = response.json()[0]['date']
    return photo_date


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
    photos_date = parser.parse_args().date
    load_dotenv()
    token_nasa = os.environ['API_TOKEN_NASA']
    path = 'images/'

    if not photos_date:
        photos_date = get_latest_photo_date(token_nasa)

    os.makedirs(path, exist_ok=True)

    epic_download_images(token_nasa, path, photos_date)
