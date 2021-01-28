#converts .raw pair images from two folders into .jpgs and renames them for easy callibration image set up
from cv2 import cv2 #hot fix for VSCode annoyance that cv2 isn't recognized
import os
import numpy as np
import glob

#VARIABLES TO CHANGE
CAM1_DIRECTORY_NAME = "Calibration_Primary"
CAM2_DIRECTORY_NAME = "Calibration_Secondary"
DIRECTORY_PATH = "/Volumes/Extreme_SSD/1_26_21/"
IMG_HEIGHT = 1080
IMG_WIDTH = 1440
MONOCHROME = True

#CODE BODY
cam1count = 0
cam2count = 0

os.chdir(DIRECTORY_PATH)
CAM1_NEW_DIRECTORY = "CAM_1_" + CAM1_DIRECTORY_NAME
CAM2_NEW_DIRECTORY = "CAM_2_" + CAM2_DIRECTORY_NAME
os.mkdir(CAM1_NEW_DIRECTORY)
os.mkdir(CAM2_NEW_DIRECTORY)
os.chdir(CAM1_DIRECTORY_NAME)
print("Converting...")
cam1_glob_results = sorted(glob.glob("*.raw"))
for file in cam1_glob_results:
    img = np.fromfile(file, dtype=np.uint8) #get .raw img from directory
    img = img.reshape(IMG_HEIGHT, IMG_WIDTH) #in order to convert from .raw to .jpg, need to provide original height and width of img
    if not MONOCHROME:
        img = cv2.cvtColor(img, cv2.COLOR_BAYER_RG2RGB)

    os.chdir("../" + CAM1_NEW_DIRECTORY)

    cv2.imwrite("camera-1-" + str(cam1count) + ".jpg", img)

    os.chdir("../" + CAM1_DIRECTORY_NAME)
    cam1count = cam1count + 1


os.chdir("../" + CAM2_DIRECTORY_NAME)
cam2_glob_results = sorted(glob.glob("*.raw"))
for file in cam2_glob_results:
    img = np.fromfile(file, dtype=np.uint8) #get .raw img from directory
    img = img.reshape(IMG_HEIGHT, IMG_WIDTH) #in order to convert from .raw to .jpg, need to provide original height and width of img
    if not MONOCHROME:
        img = cv2.cvtColor(img, cv2.COLOR_BAYER_RG2RGB)

    os.chdir("../" + CAM2_NEW_DIRECTORY)

    cv2.imwrite("camera-1-" + str(cam2count) + ".jpg", img)

    os.chdir("../" + CAM2_DIRECTORY_NAME)
    cam2count = cam2count + 1

print("Conversion complete.")