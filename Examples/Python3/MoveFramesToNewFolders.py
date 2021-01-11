#creates two new folders and moves the jpgs from same directory to those folders
import os
from datetime import date

os.mkdir(date.today().strftime("%d-%b-%Y"))