"""
1st project of Athanasios Koukosias Student ID(AM):2122160
Academic Year: 2024-2025
University of Thessaly
Class: Computetional Intelligence and Machine Learning
Professor: Dr. Kolomvatsos Konstantinos
Professor Assistants(Lab Proffessors): Fountas Panagiotis-Papathanasaki Maria
"""

# Importing all the important libraries 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import tkinter as tk
import sys
sys.path.append("/storage/emulated/0/Android/data/ru.iiec.pydroid3/files/Project1/")


# Creating the main set up of the program
dataset = pd.read_csv('student-por.csv')
#dataset.drop()
print(dataset.head())