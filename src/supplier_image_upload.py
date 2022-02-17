#!/usr/bin/env python3
"""
upload processed jpeg images to web server
"""

import os
import requests


url = "http://localhost/upload/"
# with open('/usr/share/apache2/icons/icon.sheet.png', 'rb') as opened:
#    r = requests.post(url, files={'file': opened})


def upload_images(url, path, fileNames):
    """upload files to url"""
    for files in fileNames:
        fullPath = path + files
        with open(fullPath, 'rb') as opened:
            response = requests.post(url,files={'file':opened})
            if response.status_code != requests.codes.ok:
                print(response.status_code)


if __name__ == "__main__":
    fileNames = []
    path = '/home/jonas/Projects/W4-IT-Automation-Final/src/finished/supplier-data/images/'
    # must be full path unless I add expand home
    fileNames = os.listdir(path)
    for filename in fileNames:
        if filename.endswith(".jpeg"):
            continue
        fileNames.remove(filename)
       upload_images(url, path, fileNames)
    for n in fileNames:
        print("Uploading file: ", n)
