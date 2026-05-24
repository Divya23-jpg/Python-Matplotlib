
#! Step 1: Import Libraries 
import matplotlib.pyplot as plt
import pandas as pd


# ! Step 2 : Load the data
df=pd.read_csv("netflix_dataset.csv")

# ! Show all Col name
# print(df.columns)

df=df.dropna(subset=['type','release_year','rating','country','duration'])
type_counts= df['type'].value_counts()
plt.figure(figsize=(6,4))
plt.bar(type_counts.index,type_counts.values,color=['skyblue','orange'])
plt.title("Number of Movies VS TV shows on Netfix")
plt.xlabel("Type")
plt.ylabel("Count")
plt.tight_layout()

plt.savefig('')