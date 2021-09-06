import os
import json
import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

PROJECT_DIR = os.environ['PROJECT_DIR']
df_movie, df_credits = pd.read_csv(PROJECT_DIR + '/dataset/' + ['tmdb_5000_movies.csv', 'tmdb_5000_credits.csv'])

df_credits.rename(columns={'movie_id': 'id'}, inplace=True)
df_movie = df_movie.merge(df_credits, on='id')
df_movie.drop('id', inplace=True, axis=1)

# Features extraction from JSON
casts = ['Editor', 'Producer', 'Writer', 'Director']
for cast in casts:
    df_movie[cast] = df_movie['crew'].apply(lambda x:list({x.get('name') for x in json.loads(x) if x.get('job') == cast}))

features = ['keywords', 'production_companies', 'production_countries', 'genres']
for feature in features:
    df_movie[feature] = df_movie[feature].apply(lambda x:[i.get('name') for i in json.loads(x)])

df_movie_numerical = df_movie.select_dtypes('number')
df_movie_categorical = df_movie.select_dtypes('object')[['original_title', 'keywords', 'genres', 'original_language', 'production_companies', 'cast', 'Director', 'Producer', 'Writer', 'Editor']]
df_movie = pd.concat([df_movie_numerical, df_movie_categorical], axis = 1)

# Features extraction using most frequent appearance given samples.
features_top3 = ['keywords', 'genres', 'cast']
for feature in features_top3:
    unique_ = [item for sublist in df_movie[feature].tolist() for item in sublist]
    unique_ = pd.DataFrame({feature: unique_}).groupby(feature).size()
    df_movie[feature] = df_movie[feature].apply(lambda x:unique_[(unique_.index).isin(pd.Series(x, dtype='object'))].sort_values(ascending = False)[:3].index.tolist())


# Function to convert all strings to lower case and strip names of spaces
def clean_data(x):
    if isinstance(x, list):
        return [str.lower(i.replace(" ", "")) for i in x]
    else:
        # Check if director exists. If not, return empty string
        if isinstance(x, str):
            return str.lower(x.replace(" ", ""))
        else:
            return ''


# Apply clean_data function to your features.
features = ['keywords', 'genres', 'cast', 'Director']

for feature in features:
    df_movie[feature] = df_movie[feature].apply(clean_data)

def create_soup(x):
    return ' '.join(x['keywords']) + ' ' + ' '.join(x['cast']) + ' ' + ' '.join(x['Director']) + ' ' + ' '.join(x['genres'])

df_movie['soup'] = df_movie.apply(create_soup,axis=1)
df_movie.to_csv(PROJECT_DIR + '\\model\\model.csv', index=False)