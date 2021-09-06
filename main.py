import os
import json
import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

PROJECT_DIR = os.environ['PROJECT_DIR']

# Import CountVectorizer and create the count matrix
def load_model(model_csv):
    count = CountVectorizer(stop_words='english')
    count_matrix = count.fit_transform(model_csv['soup'])

    # Compute the Cosine Similarity matrix based on the count_matrix
    cosine_sim = cosine_similarity(count_matrix, count_matrix)

    # Reset index of our main DataFrame and construct reverse mapping as before
    model_csv = model_csv.reset_index()
    indices = pd.Series(model_csv.index, index=model_csv['original_title'])
    return model_csv, cosine_sim, indices

# Function that takes in movie title as input and outputs most similar movies
def get_recommendations(title, model_csv, cosine_sim, indices):
    # Get the index of the movie that matches the title
    idx = indices[title]

    # Get the pairwsie similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 10 most similar movies
    sim_scores = sim_scores[1:11]

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]

    # Return the top 10 most similar movies
    return model_csv['original_title'].iloc[movie_indices]

if __name__ == "__main__":
    print('Loading model...')
    model_csv, cosine_sim, indices = load_model(pd.read_csv(PROJECT_DIR + '/model/model.csv'))
    print('Done loading model...')
    # An input is requested and stored in a variable
    input_title = input("Enter a movie title: ")
    print(get_recommendations(input_title, model_csv=model_csv, cosine_sim=cosine_sim, indices=indices))