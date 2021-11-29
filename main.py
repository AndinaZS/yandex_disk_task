import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {'Content-Type': 'application/json',
                   'Authorization': f'OAuth {self.token}'}
        params = {"path": path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params).json()
        href = response.get("href", "")
        res = requests.put(href, data=open(path, 'rb'))
        if res.status_code == 201:
            print('Success')
        else:
            print('Error')
        return


if __name__ == '__main__':
    path_to_file = "..\poem.txt"
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)