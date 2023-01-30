# -*- coding: utf-8 -*-
"""Preprocessing_Dataset.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GpDLcT7Hp7RuEXp497U6Tcn1nBu8pxf4
"""

import numpy as np
import pandas as pd
import plotly.express as px

df=pd.read_csv(r"/content/nutrients.csv")

df = df.replace("t", 0)
df = df.replace("t'", 0)

df.head()

df.isnull().sum()

df.dropna(inplace = True)

df.isnull().sum()

df = df.replace(",","",regex = True)

df.info()

df.reset_index(drop = True,inplace = True)

df['Grams'].unique()

df['Protein'] = df['Protein'].replace("-1","", regex=True)
df['Fiber'] = df['Fiber'].replace("a","", regex=True)

df['Grams'] = df['Grams'].astype('int32')

df.columns

df['Protein'] = pd.to_numeric(df['Protein'])

df['Fat'] = df['Fat'].astype('int32')

df['Sat.Fat'] = df['Sat.Fat'].astype('int32')

df['Fiber'] = pd.to_numeric(df['Fiber'])

df['Carbs'] = pd.to_numeric(df['Carbs'])

df['Calories'][90] = 26

df['Calories'] = pd.to_numeric(df['Calories'])

df['Actual_Protein'] = pd.to_numeric(df['Protein']/df['Grams'])

df['Actual_Calories'] = pd.to_numeric(df['Calories']/df['Grams'])
df['Actual_Fat'] = pd.to_numeric(df['Fat']/df['Grams'])
df['Actual_Sat.Fat'] = pd.to_numeric(df['Sat.Fat']/df['Grams'])
df['Actual_Fiber'] = pd.to_numeric(df['Fiber']/df['Grams'])
df['Actual_Carbs'] = pd.to_numeric(df['Carbs']/df['Grams'])

df.head()

df = df.drop_duplicates(subset = 'Food')

df.to_csv('final_dataset.csv',index = False)
