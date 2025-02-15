from tkinter import *
from tkinter import messagebox
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import os
import sys
import time
import csv

# Save data into a csv file
with open('lab_records.csv', 'a') as file:
        writer = csv.writer(file)
        if((os.path.getsize("lab_records.csv"))==0):
            writer.writerow(["Time","Patient Name","Age","Gender","Pelvic Incidence","Pelvic Tilt","Lumbar Lordosis Angle","Sacral slope","Pelvic Radius","Degree of Spondylolistesis","Result"])


