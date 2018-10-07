# coding=utf-8
import cv2
import imutils
import numpy as np

import app.core.util.imageUtil.ImageTool as ImageTool
from app.common.util.baseUtil.baseUtil import multiProcess


def matchTemplate(data):
    grayB = data[0]
    grayA = data[1]
    start_x = data[2]
    start_y = data[3]
    window = grayA[start_y:start_y + 100, start_x:start_x + 100]
    match = cv2.matchTemplate(grayB, window, cv2.TM_CCOEFF_NORMED)
    _, _, _, max_loc = cv2.minMaxLoc(match)
    matched_window = grayB[max_loc[1]:max_loc[1] + 100, max_loc[0]:max_loc[0] + 100]
    result = cv2.absdiff(window, matched_window)
    return result


def matchAB(imgA, imgB):
    if imgA.shape[1] > 500:
        imgA = imutils.resize(imgA, width=500)
        imgB = imutils.resize(imgB, width=500)

    # 转换成灰色
    grayA = cv2.cvtColor(imgA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imgB, cv2.COLOR_BGR2GRAY)

    # 获取图片A的大小
    height, width = grayA.shape

    # 取局部图像，寻找匹配位置
    result_window = np.zeros((height, width), dtype=imgA.dtype)

    datas = []
    for start_y in range(0, height - 100, 30):
        for start_x in range(0, width - 100, 30):
            datas.append([grayB, grayA, start_x, start_y])

    results = multiProcess(function=matchTemplate, data_list=datas, parallel_num=10, type="xxx", return_swith=True)
    for i in range(len(results)):
        result = results[i]
        start_y = datas[i][3]
        start_x = datas[i][2]
        result_window[start_y:start_y + 100, start_x:start_x + 100] = result

    # 用四边形圈出不同部分
    _, result_window_bin = cv2.threshold(result_window, 30, 255, cv2.THRESH_BINARY)
    _, contours, _ = cv2.findContours(result_window_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    imgC = imgA.copy()

    for contour in contours:
        min_data = np.nanmin(contour, 0)
        max_data = np.nanmax(contour, 0)

        width_now = max_data[0][0] - min_data[0][0]
        height_now = max_data[0][1] - min_data[0][1]

        max_length = max(width_now, height_now)
        min_length = min(width_now, height_now)
        if max_length * min_length > 30 and max_length / min_length < 10:
            loc1 = (min_data[0][0], min_data[0][1])
            loc2 = (max_data[0][0], max_data[0][1])
            cv2.rectangle(imgC, loc1, loc2, 255, 2)

    return imgC


def _matchAB(imgA, imgB):
    if imgA.shape[1] > 500:
        imgA = imutils.resize(imgA, width=500)
        imgB = imutils.resize(imgB, width=500)

    # 转换成灰色
    grayA = cv2.cvtColor(imgA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imgB, cv2.COLOR_BGR2GRAY)

    # 获取图片A的大小
    height, width = grayA.shape

    # 取局部图像，寻找匹配位置
    result_window = np.zeros((height, width), dtype=imgA.dtype)
    try:
        for start_y in range(0, height - 100, 30):
            for start_x in range(0, width - 100, 30):
                window = grayA[start_y:start_y + 100, start_x:start_x + 100]
                match = cv2.matchTemplate(grayB, window, cv2.TM_CCOEFF_NORMED)
                _, _, _, max_loc = cv2.minMaxLoc(match)
                matched_window = grayB[max_loc[1]:max_loc[1] + 100, max_loc[0]:max_loc[0] + 100]
                result = cv2.absdiff(window, matched_window)
                result_window[start_y:start_y + 100, start_x:start_x + 100] = result
    except Exception, e:
        print e

    # 用四边形圈出不同部分
    _, result_window_bin = cv2.threshold(result_window, 30, 255, cv2.THRESH_BINARY)
    _, contours, _ = cv2.findContours(result_window_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    imgC = imgA.copy()

    for contour in contours:
        min_data = np.nanmin(contour, 0)
        max_data = np.nanmax(contour, 0)

        width_now = max_data[0][0] - min_data[0][0]
        height_now = max_data[0][1] - min_data[0][1]

        max_length = max(width_now, height_now)
        min_length = min(width_now, height_now)
        if max_length * min_length > 30 and max_length / min_length < 10:
            loc1 = (min_data[0][0], min_data[0][1])
            loc2 = (max_data[0][0], max_data[0][1])
            cv2.rectangle(imgC, loc1, loc2, 255, 2)

    return imgC


def ImageDiff(baseImage, compareImage):
    ret_data = {}
    ret_data['baseImage'] = baseImage
    ret_data['compareImage'] = compareImage
    try:
        baseImageObject = ImageTool.create_opencv_image_from_url(baseImage)
        compareImageObject = ImageTool.create_opencv_image_from_url(compareImage)
        imageDiff = matchAB(baseImageObject, compareImageObject)
        _, imageDiffUrl = ImageTool.uploadImage(ImageTool.create_cStringIO_from_opencv(imageDiff))

        ret_data['imageDiff'] = imageDiffUrl

        return True, ret_data
    except:
        ret_data['imageDiff'] = ""
        return False, ret_data

# if __name__ == '__main__':
#
#
#         print ImageDiff(baseImage, compareImage)
