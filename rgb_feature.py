# -*- coding: utf-8 -*-
# @Time    : 2019/3/1 21:15
# @Author  : Linhui Dai
# @FileName: rgb_feature.py.py
# @Software: PyCharm

import cv2


class ColorDescriptor:
    def __init__(self, bins):
        self.bins = bins

    def describe(self, image):
        features = []
        hist = cv2.calcHist([image], [0, 1, 2], None, self.bins, [0, 180, 0, 256, 0, 256])
        hist = cv2.normalize(hist, hist).flatten()
        features.extend(hist)
        return features
