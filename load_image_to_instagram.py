import instabot
from os import listdir
from os import getenv
from os.path import join as joinpath
from dotenv import load_dotenv

load_dotenv()


def upload_photo_to_insta(image_folder_path, login, password):
    bot = instabot.Bot()
    bot.login(username=login, password=password)
    valid_files_for_instagram = filter(
        lambda x: (
                x.endswith('.jpg') |
                x.endswith('.png') |
                x.endswith('.gif') |
                x.endswith('.jpeg')

        ),
        listdir(image_folder_path)
    )
    list_image_path_and_name = [
        [
            joinpath(image_folder_path, valid_file),
            valid_file
        ]
        for valid_file in valid_files_for_instagram
    ]
    for image_path_and_name in list_image_path_and_name:
        image_path = image_path_and_name[0]
        image_name = image_path_and_name[1]
        bot.upload_photo(image_path, caption=image_name)


if __name__ == '__main__':
    image_folder_path = getenv('PATH_FOLDER')
    login = getenv('LOGIN')
    password = getenv('PASSWORD')
    upload_photo_to_insta(image_folder_path, login, password)