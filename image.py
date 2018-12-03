# -*- coding: UTF-8 -*-
# !/usr/bin/python
# author: wangxiaogang
"""
生成图片策略：
1. 截图一张底片，将上面的号码P掉
2. 通过PIL包生成相应的报销序号，画到底片上，保存
"""

import os

import sys
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

# 设置字体，如果没有，也可以不设置
font = ImageFont.truetype("wryh-Bbold.ttf", size=14)


# 底片
# backgroundImage = "002.png"
# prefixNumStr = "13100172806200"
# startNum = 828961
# endNum = 828980


def genImages(startNum, endNum, backgroundImage, prefixNumStr, preZeroNum):
    """图片循环生成逻辑"""
    # 打开底版图片

    numArray = range(startNum, endNum + 1)
    siveFilePath = "outs" + os.sep + str(startNum) + "_" + str(endNum)
    os.makedirs(os.getcwd() + os.sep + siveFilePath)
    print numArray

    try:
        for num in numArray:
            im1 = Image.open(backgroundImage)
            # 在图片上添加文字 1
            draw = ImageDraw.Draw(im1)
            numStr = prefixNumStr + '0'*preZeroNum + str(num)
            draw.text((181, 66), numStr, (80, 80, 80), font=font)
            # 003.png的： draw.text((192, 64), numStr, (80, 80, 80), font=font)
            draw = ImageDraw.Draw(im1)
            siveFileName = siveFilePath + os.sep + numStr + ".png"

            # 保存
            im1.save(siveFileName)
    except Exception as e:
        print("Error: " + str(e))
        return
    print("genImage susscess! save to: " + siveFilePath)


def main():
    """main"""
    backgroundImage = "002.png"
    prefixNumStr = sys.argv[1]
    startNum = int(sys.argv[2])
    endNum = int(sys.argv[3])
    # 发票号码前面0的数量
    preZeroNum = int(sys.argv[4])
    genImages(startNum, endNum, backgroundImage, prefixNumStr, preZeroNum)


if __name__ == "__main__":
    main()
