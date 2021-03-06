import requests
from os import makedirs
from os import getenv
from os.path import exists
from os.path import splitext
from os.path import join as joinpath
from dotenv import load_dotenv


def fetch_photo_from_hubble(list_image_id, path_folder):
    url_for_hubble = 'http://hubblesite.org/api/v3/image/'
    list_urls_and_id_for_request = [
        [joinpath(url_for_hubble, str(image_id)), image_id]
        for image_id in list_image_id
    ]
    makedirs(path_folder, exist_ok=True)
    for image_url, image_id in list_urls_and_id_for_request:
        response = requests.get(image_url).json()
        files_info = response['image_files']
        list_image_urls = [image_info['file_url'] for image_info in files_info]
        high_quality_image_url = list_image_urls[-1]
        file_name = '{name}{format}'.format(
            name=image_id,
            format=splitext(high_quality_image_url)
        )

        path_for_download_image = '{path_folder}{image_name}'.format(
            path_folder=path_folder,
            image_name=file_name
        )
        with open(path_for_download_image, 'wb') as f:
            f.write(requests.get(high_quality_image_url).content)


def fetch_image_id_from_collection(params):
    url = 'http://hubblesite.org/api/v3/images/'
    response = requests.get(url, params=params).json()
    list_image_id = [image_info['id'] for image_info in response]
    return list_image_id


if __name__ == '__main__':
    load_dotenv()
    path_folder_for_image = getenv('PATH_FOLDER')
    params = {
        'collection_name': 'spacecraft'
    }
    list_image_id = fetch_image_id_from_collection(params)
    fetch_photo_from_hubble(list_image_id, path_folder_for_image)