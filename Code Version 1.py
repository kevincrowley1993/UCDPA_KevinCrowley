# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 20:35:18 2021

@author: kevin
"""

import pandas as pd
netflix = pd.read_csv("C:/Users/kevin/OneDrive/Desktop/netflix_titles.csv", index_col = 0)
print(netflix.head())