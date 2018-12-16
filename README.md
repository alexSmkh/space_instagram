# Космический Инстаграм
Программа, состоящая из трех файлов, скачивает фотографии и 
загружает их в instagram:
 * `fetch_spacex.py` - скачивает фотографии с последнего запуска SpaceX.
 * `fetch_hubble.py` - скачивает фотографии из коллекции `spacecraft`, сделанные
 телескопом Хаббл.
 * `load_image_to_instagram` - загружает скаченные фотографии в Ваш аккаунт 
 instagram
 
 ### Как настроить доступ к аккаунту
 * Для изоляции проекта рекомендуется использовать 
 [virtualenv/venv](https://docs.python.org/3/library/venv.html)
 * Чтобы получить доступ к аккаунту instagram, нужно записать в файл `.env` Ваш
 логин и пароль:
 ```txt
 LOGIN='ВашЛогин'
 PASSWORD='ВашПароль'
 ```
 * Программа должна знать, куда/откуда ей скачивать/загружать фотографии.
 Укажите путь к папке в `.env`:
 ```txt
 PATH_FOLDER='Путь'
 ```
 
 ### Как установить
 Должен быть установлен `python3`. Затем используйте `pip`(или `pip3`, 
 если есть конфликт с `Python2`) для установки зависимостей: 
 ```bash
 pip install -r requirements.txt
 ```
 
 ### Цель проекта
 Код написать в образовательных целях на онлайн-курсе для веб-разработчиков 
 [dvmn.org](dvmn.org)