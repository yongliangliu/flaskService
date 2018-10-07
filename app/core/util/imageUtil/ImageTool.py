# coding=utf-8
import requests, json
import cv2
import numpy as np
import urllib2
import cStringIO





def create_opencv_image_from_url(url):
    request = urllib2.urlopen(url)
    img_array = np.asarray(bytearray(request.read()), dtype=np.uint8)
    return cv2.imdecode(img_array, cv2.IMREAD_COLOR)


def create_cStringIO_from_opencv(opencvObject):
    img_encode = cv2.imencode('.jpg', opencvObject)[1]
    cStringIO_file = cStringIO.StringIO(img_encode)
    return cStringIO_file

# if __name__ == '__main__':
#     aaa = create_opencv_image_from_url(baseImage)
#     bbb = create_cStringIO_from_opencv(aaa)
#
#     ccc = uploadImage(bbb)
#     print ccc
