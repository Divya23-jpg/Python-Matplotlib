
#! Step 1: Import Libraries 
import matplotlib.pyplot as plt
import pandas as pd


# ! Step 2 : Load the data
from pathlib import Path
file_path = Path("C:/Users/Divya/Desktop/netflix_dataset.csv")
df = pd.read_csv(file_path)