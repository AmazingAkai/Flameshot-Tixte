import io
import json
import os
import random
import subprocess
import sys

import pyperclip
import requests

path = os.path.abspath(__file__)
file_name = "config.json"
file_path = os.path.join(os.path.dirname(path), file_name)


class UploadError(Exception):
    """An exception raised when the file fails to upload"""


def upload_to_server(url: str, authorization: str, filename: str, domain: str) -> None:
    buffer = sys.stdin.buffer.read()
    headers = {"Authorization": authorization}
    data = {"payload_json": json.dumps({"domain": domain})}
    files = {"file": (filename, io.BytesIO(buffer), "image/png")}
    response = requests.post(
        url=url, headers=headers, files=files, data=data, timeout=60
    )

    if response.status_code == 200:
        response_json = response.json()
        pyperclip.copy(response_json["data"]["direct_url"])
    else:
        raise UploadError(
            f"Failed to upload the file, status code: {response.status_code}"
        )


def get_filename(url: str) -> str:
    def generate_random_filename() -> str:
        return str(random.randint(0, 99999))

    def is_url_available(url: str) -> bool:
        response = requests.get(url)
        return response.status_code == 404

    while True:
        filename = generate_random_filename()
        if is_url_available(f"{url}/{filename}"):
            break

    return filename


def main():
    url = "https://api.tixte.com/v1/upload"
    if os.path.isfile(file_path):
        with open(file_path, "r") as file:
            data = json.load(file)
            authorization = data.get("authorization")
            domain = data.get("domain")

        if authorization and domain:
            filename = get_filename(f"https://{domain}")

            success = False
            for _ in range(5):
                try:
                    upload_to_server(url, authorization, filename, domain)
                    success = True
                    break
                except UploadError:
                    pass

            if success:
                subprocess.call(
                    [
                        "notify-send",
                        "Successfully Uploaded",
                        "Successfully uploaded image and copied the URL to clipboard.",
                    ]
                )
            else:
                subprocess.call(
                    [
                        "notify-send",
                        "Failed To Upload",
                        "Failed to upload the image to Tixte.",
                    ]
                )
        else:
            print("Invalid authorization or domain in the configuration file.")
    else:
        print(
            "No configuration file found. Make sure to create a config.json with authorization and domain."
        )


if __name__ == "__main__":
    main()
