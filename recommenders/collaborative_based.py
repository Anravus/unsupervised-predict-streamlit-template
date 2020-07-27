"""

    Collaborative-based filtering for item recommendation.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: You are required to extend this baseline algorithm to enable more
    efficient and accurate computation of recommendations.

    !! You must not change the name and signature (arguments) of the
    prediction function, `collab_model` !!

    You must however change its contents (i.e. add your own collaborative
    filtering algorithm), as well as altering/adding any other functions
    as part of your improvement.

    ---------------------------------------------------------------------

    Description: Provided within this file is a baseline collaborative
    filtering algorithm for rating predictions on Movie data.

"""

# Script dependencies
import pandas as pd
import numpy as np
import pickle
import copy
from surprise import Reader, Dataset
from surprise import SVD, NormalPredictor, BaselineOnly, KNNBasic, NMF
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# Importing data
movies = pd.read_csv('resources/data/movies.csv',sep = ',',delimiter=',')
train = pd.read_csv('resources/data/ratings.csv')
#train.drop(['timestamp'], axis=1,inplace=True)

# We make use of an SVD model trained on a subset of the MovieLens 10k dataset.
model=pickle.load(open('resources/models/SVD.pkl', 'rb'))

movieid_to_title_df = pd.merge(train,movies, on= 'movieId', how = 'left')
movieid_to_title_df = movieid_to_title_df.drop(['genres','rating','userId','timestamp'], axis = 1)
movieid_to_title_df = movieid_to_title_df.drop_duplicates()
movieid_to_title_df.dropna(inplace = True)

def prediction_item(item_id):
    """Map a given favourite movie to users within the
       MovieLens dataset with the same preference.

    Parameters
    ----------
    item_id : int
        A MovieLens Movie ID.

    Returns
    -------
    list
        User IDs of users with similar high ratings for the given movie.

    """
    # Data preprosessing
    reader = Reader(rating_scale=(0, 5))
    load_df = Dataset.load_from_df(train[['userId','movieId','rating']],reader)
    a_train = load_df.build_full_trainset()

    predictions = []
    for ui in a_train.all_users():
        predictions.append(model.predict(iid=item_id,uid=ui, verbose = False))
    return predictions

def pred_movies(movie_list):
    """Maps the given favourite movies selected within the app to corresponding
    users within the MovieLens dataset.

    Parameters
    ----------
    movie_list : list
        Three favourite movies selected by the app user.

    Returns
    -------
    list
        User-ID's of users with similar high ratings for each movie.

    """
    # Store the id of users
    id_store=[]
    # For each movie selected by a user of the app,
    # predict a corresponding user within the dataset with the highest rating
    for i in movie_list:
        #movie_id = movieid_to_title_df[movieid_to_title_df['title'] == i]['movieId'].values[0]
        predictions = prediction_item(item_id = i)
        predictions.sort(key=lambda x: x.est, reverse=True)
        # Take the top 10 user id's from each movie with highest rankings
        for pred in predictions[:10]:
            id_store.append(pred.uid)
    # Return a list of user id's
    return id_store

def prediction(movie_title,user_id):
    """Predicts users rating based on movie

    Parameters
    ----------
    movie_title : string
        The name of the movie
    user_id : integer
        The user identification

    Returns
    -------
    value
        The predicted rating based on movie and user

    """
    #movie_id = movieid_to_title_df[movieid_to_title_df['title'] == movie_title]['movieId'].values[0]
    predictions = model.predict(iid=movie_title,uid=user_id, verbose = False)
    return predictions.est

# !! DO NOT CHANGE THIS FUNCTION SIGNATURE !!
# You are, however, encouraged to change its content.
def collab_model(movie_list,top_n=10):
    """Performs Collaborative filtering based upon a list of movies supplied
       by the app user.

    Parameters
    ----------
    movie_list : list (str)
        Favorite movies chosen by the app user.
    top_n : type
        Number of top recommendations to return to the user.

    Returns
    -------
    list (str)
        Titles of the top-n movie recommendations to the user.

    """
    movie_ids = pred_movies(movie_list)
    print('first phase')
    df_init_users = train[train['userId']==movie_ids[0]]
    for i in movie_ids[1:]:
        df_init_users=df_init_users.append(train[train['userId']==i])
    # Getting the user-item matrix
    df_init_users = pd.merge(df_init_users, movieid_to_title_df, on = 'movieId', how = 'left')
    df_init_users = df_init_users.dropna()
    top_users_matrix = df_init_users.groupby(['title','userId'])['rating'].max().unstack()

    # Adding the movies from list into user-item matrix if not there
    for i in movie_list:
        if i not in top_users_matrix.index.values.tolist():
            length = len(top_users_matrix.columns)
            df_nan = pd.DataFrame([[(np.NaN)]*length], index = [i], columns = top_users_matrix.columns)
            top_users_matrix = top_users_matrix.append(df_nan)

    # makinf predictions for those movies based on algorithm
    for i in top_users_matrix.columns:
        for j in top_users_matrix.index.values.tolist():
            if np.isnan(top_users_matrix[i].loc[j]):
                top_users_matrix[i].loc[j] = prediction(j,i)

    # Getting the cosine similarity matrix
    cosine_sim = cosine_similarity(top_users_matrix)
    indices = pd.Series(top_users_matrix.index)
    idx_1 = indices[indices == movie_list[0]].index[0]
    idx_2 = indices[indices == movie_list[1]].index[0]
    idx_3 = indices[indices == movie_list[2]].index[0]

    # Creating a Series with the similarity scores in descending order
    rank_1 = cosine_sim[idx_1]
    rank_2 = cosine_sim[idx_2]
    rank_3 = cosine_sim[idx_3]

    # Calculating the scores
    score_series_1 = pd.Series(rank_1).sort_values(ascending = False)
    score_series_2 = pd.Series(rank_2).sort_values(ascending = False)
    score_series_3 = pd.Series(rank_3).sort_values(ascending = False)

     # Appending the names of movies
    listings = score_series_1.append(score_series_2).append(score_series_3).sort_values(ascending = False)
    recommended_movies = []
    # Choose top 50
    top_50_indexes = list(listings.iloc[1:50].index)
    # Removing chosen movies
    top_indexes = np.setdiff1d(top_50_indexes,[idx_1,idx_2,idx_3])
    for i in top_indexes[:top_n]:
        recommended_movies.append(indices[i])
    return recommended_movies
