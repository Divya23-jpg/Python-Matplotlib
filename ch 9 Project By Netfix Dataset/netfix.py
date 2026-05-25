
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
# plt.show()


# ! For showing Rekease year of the Movies 
realease_counts=df['release_year'].value_counts().sort_index()
plt.figure(figsize=(10,6))
plt.scatter(realease_counts.index,realease_counts.values,color='red')
plt.title('Release Year VS Number of Shows')
plt.xlabel("Release Year")
plt.ylabel("Number of Shows")
plt.tight_layout()
plt.savefig('release_year.png')
# plt.show()


# ! For Showing Top 10 Country and num of shows they give us

country_counts=df['country'].value_counts().head(10)
plt.figure(figsize=(8,6))
plt.barh(country_counts.index,country_counts.values,color='teal')
plt.title('Top 10 Countries By Number of shows')
plt.xlabel("Number of Shows")
plt.ylabel("Country")
plt.tight_layout()
plt.savefig('top_10_country.png')
# plt.show()


# ! Subplots for Movies VS Tv shows
content_by_year=df.groupby(['release_year','type']).size().unstack().fillna(0)
fig,ax=plt.subplots(1,2,figsize=(12,5))
#  First Subplot: Movies
ax[0].plot(content_by_year.index,content_by_year['Movie'],color='blue')
ax[0].set_title("Movies Release Per Year")
ax[0].set_xlabel('Year')
ax[0].set_ylabel('Number of Movies ')

#  Second  Subplot: TV Shows
ax[0].plot(content_by_year.index,content_by_year['TV Show'],color='Orange')
ax[0].set_title("TV Shows Release Per Year")
ax[0].set_xlabel('Year')
ax[0].set_ylabel('Number of Movies ')

fig.suptitle("Comparison of Movies and TV Shows Over Year")
plt.tight_layout()
plt.savefig('movies_Tv_shows_comparison.png')
plt.show()