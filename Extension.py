import cv2
import os
import numpy as np
from shutil import copyfile


def saveToFile(image, file, outFile):
    copyfile(file, outFile)


def showMask(img, mask):
    if (img.shape):
        print(mask)
        cv2.imshow("img", img)
        cv2.imshow("mask", mask)


# count % of white mask
def result(img, mask):
    showMask(img, mask)

    num_rows, num_cols = mask.shape
    total = num_rows * num_cols
    nonzeroElements = np.count_nonzero(mask)

    if (nonzeroElements != 0):
        div_res = nonzeroElements / total
        # 15%
        if (div_res > 0.15):
            print("YES", div_res)
            return True
        else:
            print("No", div_res)

    return False


def check(color, file, outFilePath):
    print('check is', file, color)
    img = cv2.imread(file, cv2.COLOR_BGR2HSV)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # mask
    mask = []

    if color == 'yellow':
        mask = cv2.inRange(hsv, (18, 40, 90), (27, 255, 255))
    elif color == 'red':
        mask = cv2.inRange(hsv, (0, 50, 50), (10, 255, 255))
    elif color == 'green':
        mask = cv2.inRange(hsv, (36, 0, 0), (70, 255, 255))
    elif color == 'blue':
        mask = cv2.inRange(hsv, (100, 150, 0), (140, 255, 255))
    elif color == 'special':
        print('TODO baklajan color')

    # result mask
    if (result(img, mask)):
        saveToFile(img, file, outFilePath)


# default value is red
def method(color='green', inPath='./images/', outDir='./output'):
    for file in os.listdir(inPath):
        check(color, os.path.join(inPath, file), os.path.join(outDir, file))
