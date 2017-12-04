# creating a conda environment
c:\Users\eltoukhysm>conda create -n pandas python=3.6 pandas
c:\Users\eltoukhysm>activate pandas
c:\Users\eltoukhysm>python

# importing pandas and numpy
import pandas as pd
import numpy as np

# reading in csv file of tweets
df = pd.read_csv(r'c:\Users\eltoukhysm\Biof309_Fall2017\Assignments\Loop_assignment\tweets.csv')
df.head()

#creating a subset dataframe with only tweets that were favored or retweeted one or more times
include = df[np.logical_and(df["favorite_count"]>=1, df["retweet_count"]>=1)]
include.head()
include.describe()

#creating a function low/high based on mean favorite_count (10.62) and retweet_count(18.09)
f = []
for row in include['favorite_count']:
    if row < 10.62:
        f.append('low')
    elif row > 10.62:
        f.append('high')

r = []
for row in include['retweet_count']:
    if row < 18.09:
        r.append('low')
    elif row >18.09:
        r.append('high')

include['f'] = f
include['r'] = r
