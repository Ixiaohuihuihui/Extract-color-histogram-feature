# -*- coding: utf-8 -*-
# @Time    : 2019/3/1 22:11
# @Author  : Linhui Dai
# @FileName: feature_index.py
# @Software: PyCharm

import rgb_feature
import argparse
import glob
import cv2

# Construct the argument parser and parse the argument
ap = argparse.ArgumentParser()
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset",
                help="Path to the directory that contains the images to be indexed",
                default='./test_images')
ap.add_argument("-i", "--index",
                help="Path to where the computed index will be stored",
                default='index1.csv')
args = vars(ap.parse_args())

# initialize the color descriptor
cd = rgb_feature.ColorDescriptor((8, 8, 8))

# open the output index file for writing image RGB feature
output = open(args["index"], "w")

# use glob to grab the image paths and loop over them
for imagePath in glob.glob(args["dataset"] + "/*.jpg"):
    # extract the image ID from the image path and load the image itself
    imageID = imagePath[imagePath.rfind("/") + 1:]
    image = cv2.imread(imagePath)

    # describe the image
    features = cd.describe(image)

    # write the features to file
    features = [str(f) for f in features]
    output.write("%s,%s\n" % (imageID, ",".join(features)))
output.close()
