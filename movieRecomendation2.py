import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('dark')
#%matplotlib inline

ratings_data = pd.read_csv("ml-latest-small\\ratings.csv")
#print(ratings_data.head())

movie_names = pd.read_csv("ml-latest-small\\movies.csv")
#print(movie_names.head())

movie_data = pd.merge(ratings_data, movie_names, on='movieId')
#print(movie_data.head())

#print(movie_data.groupby('title')['rating'].count().sort_values(ascending=False).head())

ratings_mean_count = pd.DataFrame(movie_data.groupby('title')['rating'].mean())
ratings_mean_count['rating_counts'] = pd.DataFrame(movie_data.groupby('title')['rating'].count())
#print(ratings_mean_count.head())

plt.figure(figsize=(8,6))
plt.rcParams['patch.force_edgecolor'] = True
print(ratings_mean_count['rating_counts'].hist(bins=50))