from cv2 import cv2
import numpy as np
import glob
import os

#VARIABLES TO CHANGE
DIRECTORY_NAME = "1_19_21-Secondary-30_TO_JPG"
DIRECTORY_PATH = "/Users/jetwang/Desktop/Georgia_Tech_Classes/SNEL/Hess_Lab/spinnaker_python-2.2.0.48-cp37-cp37m-macosx_10_9_x86_64/Examples/" #add path to directory if not in same folder
IMG_HEIGHT = 1080
IMG_WIDTH = 1440
FPS = 30.0

# Define the codec and create VideoWriter object.
out = cv2.VideoWriter(DIRECTORY_NAME[:-7] + ".mp4",cv2.VideoWriter_fourcc(*'mp4v'), FPS, (IMG_WIDTH,IMG_HEIGHT))

os.chdir(DIRECTORY_PATH+DIRECTORY_NAME)
count = 0
print("Converting...")

glob_results = sorted(glob.glob('*.jpg')) #glob picks files at random using listdir, need to have it sorted by name, be wary for if recording at midnight and next day flips over.

for filename in glob_results:
    img = cv2.imread(filename)
    out.write(img)
    count = count+1
    if count % 5000 == 0:
        print("Current file: " + str(count))
out.release()

print("Video Complete")