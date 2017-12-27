# -*- coding:utf-8 -*-

import pytesseract
from PIL import Image

def ocr_image():

    # 1.加载图片
    # image = Image.open("test.jpg")
    image = Image.open("排序算法.png")
    # image = Image.open("7code.png")

    # 2.识别
    txt = pytesseract.image_to_string(image, lang='chi_sim')
    # txt = pytesseract.image_to_string(image)
    print txt



if __name__ == '__main__':
    ocr_image()

