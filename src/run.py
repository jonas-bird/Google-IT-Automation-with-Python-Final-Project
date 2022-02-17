#!/usr/bin/env python3
"""Upload text descriptions of fruit items in json format to utl"""

import os
import requests


url = 'http:// /fruits/'  # put in proper IP for attempt
# targetPath = '/home//supplier-data/descriptions/'  # put in proper student home directory
# targetPath = '/home/jonas/Projects/W4-IT-Automation-Final/src/finished/supplier-data/descriptions/'
fieldnames = ['name', 'weight', 'description', 'image_name']


def process_files(fileNames, fieldnames):
    """convert the info in text files to JSON format"""
    for f in fileNames:
        record = {}
        lines = []
        filename = targetPath + f
        with open(filename) as handle:
            itemName = next(handle)
            lines.append(itemName.strip())
            itemWeight = int((next(handle).split()[0].strip()))
            lines.append(itemWeight)
            itemDescription = next(handle).strip()
            lines.append(itemDescription)
        # append the filename of the image
        lines.append(f.split('.')[0] + '.jpeg')
        record = dict(zip(fieldnames, lines))
        # print(record)
        response = requests.post(url, json=record)
        print(response.status_code)
        if response.status_code != response.codes.ok:
            print(response.status_code)


if __name__ == '__main__':
    fileNames = []
    fileNames = os.listdir(targetPath)
    for filename in fileNames:
        if filename.endswith(".txt"):
            continue
        fileNames.remove(filename)
    process_files(fileNames, fieldnames)
