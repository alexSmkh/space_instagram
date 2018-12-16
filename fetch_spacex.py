import errno
import requests
from os import makedirs
from os import getenv
from dotenv import load_dotenv


load_dotenv()


def fetch_spasex_last_launch(path_folder, url):
    try:
        makedirs(path_folder)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

    r = requests.get(url).json()
    image_urls = r['links']['flickr_images']
    for image_number, image_url in enumerate(image_urls):
        path_file = '{path_folder}{filename}{image_number}{format}'.format(
            path_folder=path_folder,
            filename='image',
            image_number=image_number,
            format='.jpeg'
        )
        with open(path_file, 'wb') as f:
            f.write(requests.get(image_url).content)


if __name__ == '__main__':
    path_folder_for_image = getenv('PATH_FOLDER')
    last_launch_url = 'https://api.spacexdata.com/v3/launches/latest'
    fetch_spasex_last_launch(path_folder_for_image, last_launch_url)
