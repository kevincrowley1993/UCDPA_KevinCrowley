# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 20:35:18 2021

@author: kevin
"""

# importing netflix and disney plus datasets

import numpy as np
import pandas as pd
netflix = pd.read_csv("C:/Users/kevin/OneDrive/Desktop/netflix_titles.csv", index_col = 0)
disney = pd.read_csv("C:/Users/kevin/OneDrive/Desktop/disney_plus_titles.csv", index_col = 0)
print(netflix.head())
print(disney.head())

# sorting and filtering

netflix_filtered = netflix[["type", "title", "country", "date_added", "release_year", "rating", "duration", "listed_in"]]
disney_filtered = disney[["type", "title", "country", "date_added", "release_year", "rating", "duration", "listed_in"]]
print(netflix_filtered.head())
print(disney_filtered.head())

netflix_sorted_year = netflix_filtered.sort_values(["release_year", "duration"], ascending = [False, False])
disney_sorted_year = disney_filtered.sort_values(["release_year", "duration"], ascending = [False, False])
print(netflix_sorted_year.head())
print(disney_sorted_year.head())

# replacing missing values

netflix_filled = netflix_sorted_year.fillna("Unknown")
disney_filled = disney_sorted_year.fillna("Unknown")

# removing duplicates

netflix_unique = netflix_filled.drop_duplicates(subset = ["title", "release_year", "duration"])
disney_unique = disney_filled.drop_duplicates(subset = ["title", "release_year", "duration"])

# how many shows are from before and after 2013, when Netflix started producing their own content?

netflix_added_after_2012 = netflix_unique[netflix_unique["release_year"] >= 2013]
netflix_added_before_2013 = netflix_unique[netflix_unique["release_year"] <= 2012]
print(netflix_added_after_2012["release_year"].value_counts())
print(netflix_added_before_2013["release_year"].value_counts())

# how many shows are from before and after 2019, when Disney+ was launched?

disney_added_after_2018 = disney_unique[disney_unique["release_year"] >= 2019]
disney_added_before_2019 = disney_unique[disney_unique["release_year"] <= 2018]
print(disney_added_after_2018["release_year"].value_counts())
print(disney_added_before_2019["release_year"].value_counts())

# indexing

netflix_new_index = netflix_unique.set_index('title')
print(netflix_new_index.head())

# undoing changes

netflix_undo_index = netflix_new_index.reset_index()
print(netflix_undo_index.head())

# netflix index as title and release year

netflix_title_year = netflix_undo_index.set_index(["title", "release_year"])
print(netflix_title_year.head())

#disney index as title and release year

disney_title_year = disney_unique.set_index(["title", "release_year"])
print(disney_title_year.head())

# merging netflix and disney+ tables

netflix_disney = netflix_title_year.merge(disney_title_year, on = "title", how = "outer", suffixes = ("_netflix", "_disney"))
print(netflix_disney)

# how many netflix shows only lasted one season?

netflix_one_season = netflix_disney.value_counts("duration_netflix")["1 Season"]
print(netflix_one_season)

# compared how many netflix titles in total?

netflix_unique_titles = netflix_unique.value_counts("title")
print(netflix_unique_titles)

# shows vs movies - netflix

netflix_shows = netflix_unique.value_counts("type")["TV Show"]
print(netflix_shows)

netflix_movies = netflix_unique.value_counts("type")["Movie"]
print(netflix_movies)

# shows vs movies - disney+

disney_shows = disney_unique.value_counts("type")["TV Show"]
print(disney_shows)

disney_movies = disney_unique.value_counts("type")["Movie"]
print(disney_movies)

# proportion of r rated shows across both streaming services

netflix_r = netflix_unique.value_counts("rating")["R"]
print(netflix_r)

netflix_unique_titles = netflix_unique.value_counts("title")
print(netflix_unique_titles)

disney_r = disney_unique.value_counts("rating")["R"]
print(disney_r)

import 