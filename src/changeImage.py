#!/usr/bin/env python3

from pathlib import Path
from PIL import Image


def manipulate_images(fileNames, destinationPath):
    """
    function that recieves a list of files, rotates and resizes them,
    and saves them as .jpeg
    """
    size = (600, 400)
    newFiles = []
    for filename in fileNames:
        try:
            newFileName = Path(filename).stem + '.jpeg'
            newFileName = Path(destinationPath) / newFileName
            with Image.open(filename) as im:
                im = im.convert("RGB")
                im.thumbnail(size)
                im.save(newFileName, "JPEG")
        except Exception:
            pass

        newFiles.append(newFileName)
    return newFiles


if __name__ == "__main__":
    fileNames = []
    path = Path(
        '/home/jonas/Projects/W4-IT-Automation-Final/src/finished/supplier-data/images/')
    # must be full path unless I add expand home
    destinationPath = '/home/jonas/Projects/W4-IT-Automation-Final/src/finished/supplier-data/images/'
    for fNames in path.glob('*'):
        fileNames.append(fNames)

    newNames = manipulate_images(fileNames, destinationPath)
    print("New thumbnails saved as: ")
    for n in newNames:
        print(n)
