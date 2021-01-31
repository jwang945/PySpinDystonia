from cv2 import cv2 #hot fix for VSCode annoyance that cv2 isn't recognized
import os
import numpy as np
import glob

#VARIABLES TO CHANGE

Cam1_DIRECTORY_PATH = "/Users/jetwang/Desktop/Cam1"
Cam2_DIRECTORY_PATH = "/Users/jetwang/Desktop/Cam2"

#CODE BODY
cam1count = 1
cam2count = 1

os.chdir("/Users/jetwang/Desktop/")

print("Renaming...")

os.chdir(Cam1_DIRECTORY_PATH)
cam1_glob_results = sorted(glob.glob("*.jpg"))

for file in cam1_glob_results:
    print(file + str(cam1count))
    os.rename(file, "camera-1-"+str(cam1count)+".jpg")
    cam1count = cam1count + 1

os.chdir(Cam2_DIRECTORY_PATH)
cam2_glob_results = sorted(glob.glob("*.jpg"))

for file in cam2_glob_results:
    print(file + str(cam2count))
    os.rename(file, "camera-2-"+str(cam2count)+".jpg")
    cam2count = cam2count + 1

print("Renaming Complete.")