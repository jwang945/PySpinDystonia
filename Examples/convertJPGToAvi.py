from cv2 import cv2
import numpy as np
import glob
import os

#VARIABLES TO CHANGE
DIRECTORY_NAME = "Secondary_TO_JPG"
DIRECTORY_PATH = "/Volumes/Extreme_SSD/1_21_21/" #add path to directory if not in same folder
IMG_HEIGHT = 1080
IMG_WIDTH = 1440
FPS = 30.0

# Define the codec and create VideoWriter object.
out = cv2.VideoWriter(DIRECTORY_NAME[:-7] + ".mp4",cv2.VideoWriter_fourcc(*'mp4v'), FPS, (IMG_WIDTH,IMG_HEIGHT))

os.chdir(DIRECTORY_PATH+DIRECTORY_NAME)
count = 0
print("Converting...")

glob_results = sorted(glob.glob('*.jpg')) #glob picks files at random using listdir, need to have it sorted by name, be wary for if recording at midnight and next day flips over.
glob_results = glob_results[:90001]
print("Num Frames: " + str(len(glob_results)))
for filename in glob_results:
    img = cv2.imread(filename)
    out.write(img)
    count = count+1
    if count % 1000 == 0:
        print("Current file: " + str(count))
out.release()

print("Video Complete")