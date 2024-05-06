import requests
import os
from urllib.parse import urlparse, unquote

# https://api.nasa.gov/EPIC/api/natural/all
# https://api.nasa.gov/planetary/apod?api_key=7dA86AdIPmFEcP21Hex6gCeOHrDQUIAazvB2WQGt
# https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08&api_key=7dA86AdIPmFEcP21Hex6gCeOHrDQUIAazvB2WQGt
url_api_spaceX= 'https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a'
folder = 'new_folder'

url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
filename = 'hubble.jpeg'


def fetch_spacex_last_launch(url):
    response = requests.get(url_api_spaceX)
    response.raise_for_status()
    data = response.json()
    foto_spisok = data['links']['flickr']['original']
    for i, foto_url in enumerate(foto_spisok):
        path = f'{folder}/spacex_{i}.jpeg'
        save_image(foto_url, path)


path = os.path.join(folder, filename)
os.makedirs(folder, exist_ok=True)
# with open(path, 'wb') as file:
#     file.write(response.content)
# save_image(url, path)

# fetch_spacex_last_launch(url_api_spaceX)

# Пример использования функции
file_url = '"https://example.com/txt/hello%20world.txt?v=9#python"'
extension = get_extension_file(file_url)
print(extension)  # Выведет 'txt'
