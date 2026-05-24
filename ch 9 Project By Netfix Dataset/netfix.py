
#! Step 1: Import Libraries 
import matplotlib.pyplot as plt
import pandas as pd


# ! Step 2 : Load the data
df=pd.read_csv("netflix_titles.csv")
# df=pd.read_csv("netflix_dataset.csv")

# ! Show all Col name

# print(df.columns)

df=df.dropna(subset=['type','release_year','rating','country','duration'])
type_counts= df['type'].value_counts()

# ! For Showing Relationship Between Movies Vs Tv shows (Bar Graph)
plt.figure(figsize=(6,4))
plt.bar(type_counts.index,type_counts.values,color=['skyblue','orange'])
plt.title("Number of Movies VS TV shows on Netfix")
plt.xlabel("Type")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig('movies_vs_tyshows.png')
# plt.show()

# ! For Showing Rating in Percentage (Pie chart)
rating_counts=df['rating'].value_counts()
plt.figure(figsize=(8,6))
plt.pie(rating_counts,labels=rating_counts.index,autopct='%1.1f%%',startangle=90)
plt.title("Percentage  of rating")
plt.tight_layout()
plt.savefig('content_rating_pie.png')
# plt.show()


# ! For showing Movies Duration according to Minutes (Histogram)
movies_df=df[df['type']=="Movie"].copy()
movies_df['duration_int']=movies_df['duration'].str.replace('min','').astype(int)

plt.figure(figsize=(8,6))
plt.hist(movies_df['duration_int'],bins=30,color='purple',edgecolor='black')
plt.title('Distribution Of Movie Duration')
plt.xlabel("Duration Minute")
plt.ylabel("Number of Movies")
plt.tight_layout()
plt.savefig('movies_duration_histo.png')
plt.show()



