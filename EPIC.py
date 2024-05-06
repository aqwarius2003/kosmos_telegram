import json
import urllib.request
import os
from save_foto import save_image
import requests
from dotenv import load_dotenv

epic_url_all = 'https://api.nasa.gov/EPIC/api/natural/all'
epic_url_date = 'https://api.nasa.gov/EPIC/api/natural/date'
def epic_download_images(token_nasa, path):
    os.makedirs(path, exist_ok=True)           # создает папку если нет
    payload = {'api_key': token_nasa}
    response = requests.get(epic_url_all, params=payload)
    last_image_date = response.json()[0]['date']
    last_image_date_formatted = last_image_date.replace('-', '/')

    response = requests.get(epic_url_date, last_image_date, params = payload)
    response_images = response.json()
    for image_idx, image_payload in enumerate(response_images):
        image_identifier = image_payload['image']
        image_link = f'https://api.nasa.gov/EPIC/archive/natural/' \
                     f'{last_image_date_formatted}/png/{image_identifier}.png'
        # image_extension = get_file_extention(image_link)
        save_image(image_link,
                       f'{path}nasa_epic_{image_idx}{image_extension}',
                       payload)

if __name__ == '__main__':
    load_dotenv()
    token_nasa = os.environ['API_TOKEN_NASA']
    path = 'images'
    epic_download_images(token_nasa, path)

    # for item in arr:
    #     name = item['image'] + '.png'
    #     archive = f"https://epic.gsfc.nasa.gov/archive/natural/{year}/{month}/{day}/png/"
    #     source = archive + name
    #     file_destination = os.path.join(folder, name)

        #создает папку
        # os.makedirs(folder, exist_ok=True)
        # urllib.request.urlretrieve(source, file_destination)

# Пример использования функции
# year = '2024'
# month = '05'
# day = '04'
# folder = 'image_folder'
#
# epic_download_images(year, month, day, folder)



# from image_downloader import download_image, get_file_extention
# https://api.nasa.gov/EPIC/archive/natural/2024-05-05/png/{image_id}.png
# Примеры запросов
# https://api.nasa.gov/EPIC/api/natural/images?api_key=DEMO_KEY
# https://api.nasa.gov/EPIC/api/natural/date/2019-05-30?api_key=7dA86AdIPmFEcP21Hex6gCeOHrDQUIAazvB2WQGt
# https://api.nasa.gov/EPIC/api/natural/all?api_key=DEMO_KEY
# https://api.nasa.gov/EPIC/archive/natural/2019/05/30/png/epic_1b_20190530011359.png?api_key=DEMO_KEY
#
# Примеры запросов
# https://epic.gsfc.nasa.gov/api/natural
# https://epic.gsfc.nasa.gov/api/enhanced/date/2015-10-31
# https://epic.gsfc.nasa.gov/api/natural/all
# https://epic.gsfc.nasa.gov/archive/natural/2015/10/31/png/epic_1b_20151031074844.png
