# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 20:35:18 2021

@author: kevin
"""

import pandas as pd
netflix = pd.read_csv("C:/Users/kevin/OneDrive/Desktop/netflix_titles.csv", index_col = 0)
print(netflix.head())
netflix_filtered = netflix[["type", "title", "country", "date_added", "release_year", "rating", "duration", "listed_in"]]
print(netflix_filtered.head())
netflix_sorted_duration = netflix_filtered.sort_values("duration", ascending = False)
print(netflix_sorted_duration.head())
netflix_movies = netflix_sorted_duration[netflix_sorted_duration["type"] == "Movie"]
print(netflix_movies.head())
print(netflix_sorted_duration['type'].value_counts())
print(netflix_sorted_duration['release_year'].value_counts())
print(netflix_sorted_duration['rating'].value_counts())
print(netflix_sorted_duration['listed_in'].value_counts())
netflix_titles_unique = netflix_sorted_duration.drop_duplicates(subset = ["title", "release_year", "duration"])
print(netflix_titles_unique["title"].value_counts())