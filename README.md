# Космо бот

Этот репозиторий содержит набор скриптов на языке Python, которые предназначены для загрузки фотографий космоса с различных источников и сохранения их в локальную папку. Кроме того, скрипты также позволяют публиковать эти фотографии в телеграм-канале с использованием телеграм-бота.

## Установка
Python должен быть установлен.

Скачайте проект и установите зависимости :
        
                git clone https://github.com/aqwarius2003/kosmos_telegram.git
                cd kosmos_telegram
                pip install -r requirements.txt

Создайте файл .env в папке проекта и заполните его своими данными:

                API_TOKEN_NASA=<ваш токен доступа к NASA>
                API_TELEGRAM=<API-токен вашего бота>
                TG_CHAT_ID=<ссылка на канал формата @ваш канал>

Получить токен NASA можно по [ссылке](https://api.nasa.gov/)

Получить API токен [телеграма](https://telegram.me/BotFather) 

## Основные скрипты

**fetch_spacex_images.py**  
Скачивает фотографии с запусков SpaceX. При запуске скрипта в командной строке можно указать идентификатор запуска в качестве аргумента. Если идентификатор не указан, то будут загружены фотографии последнего запуска, если они существуют.  
Например:

                python fetch_spacex_images.py -id 5eb87ce4ffd86e000604b337 


**fetch_nasa_apod_images.py**  
Скачивает Astronomy Picture of the Day - случайные материалы с сайта NASA [APOD](https://api.nasa.gov/#apod). 
При запуске скрипта в командной строке в качестве аргумента можно указать, сколько фото необходимо скачать.  
Например:

                python fetch_nasa_apod_images.py -с 100

**fetch_nasa_epic_images.py**  
Скачивает EPIC фото с сайта NASA - Земля из космоса [NASA API EPIC](https://api.nasa.gov/#epic). При запуске скрипта в командной строке в качестве аргумента можно указать дату фотографий, формат %Y-%m-%d, без указания скачает последние.  
Например:

                python fetch_nasa_epic_images.py -d 2011-09-11

**send_image_telegram.py**  

Публикует в вашем телеграм канале фотографии, скачанные скриптами из проекта.
Из-за ограничения телеграм в размере отправляемого изображения файла - фото больше 20 мегабайт скрипт пропускает.
При запуске скрипта в командной строке в качестве аргумента можно указать в часах (можно с десятыми и сотыми) частоту публикаций. Если не указать - по умолчанию разв 4 часа.   

#### Как использовать:

Создайте телеграм бота, [получите](https://telegram.me/BotFather) его токен _API_TELEGRAM_ (переменную добавить в файл .env - см. выше) 
Сделайте телеграм канал, добавьте своего бота админом и ссылку на канал в формате @name добавьте в переменную _TG_CHANNEL_NAME_.   
                
                send_image_telegram.py -t 3
