"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st

# Data handling dependencies
import pandas as pd
import numpy as np

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

# App declaration
def main():

    # Creating load data sign on sidebar
    st.sidebar.subheader(":heavy_check_mark: Data is loaded")
    st.sidebar.text_input("link to train data", "https://raw.githubusercontent.com/Anravus/unsupervised-predict-streamlit-template/developing/resources/data/movies.csv")

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    # Creating multiple pages
    st.sidebar.title("Menu")
    page_options = ["Recommender System","Solution Overview","Our Mission","Machine Learning","Data Exploration","Our Products and Services","About Us","References"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.write("Describe your winning approach on this page")

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.

    # Created Our Mission Page
    if page_selection == "Our Mission":
        st.image("https://raw.githubusercontent.com/Anravus/unsupervised-predict-streamlit-template/developing/resources/images/OurMission.png",
                 use_column_width=True )

    # Created Machine Learning Page
    if page_selection == "Machine Learning":
        st.image("https://raw.githubusercontent.com/Anravus/unsupervised-predict-streamlit-template/developing/resources/images/MachineLearning.png",
                 use_column_width=True)

    # Created Data Exploration page
    if page_selection == "Data Exploration":
        st.image("https://raw.githubusercontent.com/Anravus/unsupervised-predict-streamlit-template/developing/resources/images/DataExploration.png",
                 use_column_width=True)

    # Created Our Products & Services page
    if page_selection == "Our Products and Services":
        st.image("https://raw.githubusercontent.com/Anravus/unsupervised-predict-streamlit-template/developing/resources/images/Products.png",
                 use_column_width=True)

        # OneFlix products offered
        st.title("Products and Services offered")
        st.markdown("""
                        - Work with stakeholders in any organisation to identify opportunities for leveraging company data to drive business solutions.
                        - Assess the effectiveness and accuracy of new data sources and data gathering techniques.
                        - Mine and analyze data from company databases to drive optimization and improvement of product development, marketing techniques and business strategies.
                        - Intelligent Dash-boarding
                        - Distributed computing
                        - Story-telling and visualisation of big data
                        - Develop custom data models and algorithms to apply to data sets.
                        - Use predictive modeling to increase and optimize customer experiences, revenue generation, ad targeting and other business outcomes.
                        - Develop company A/B testing framework and test model quality.
                        - Coordinate with different functional teams to implement models and monitor outcomes.
                        - Develop processes and tools to monitor and analyze model performance and data accuracy.
                    """)

        # Create a contact us widget
        st.header("Contact Us")
        st.markdown("If you wish to contact us please enter your details below and we will get back to as soon as possible")
        st.text_input("Full Name")
        st.text_input("Contact Number", "Optional")
        st.text_input("Email Address")
        st.text_area("Enter a message")

        def func():
            st.write("Submitted, Thank You")
            return
        if st.button("Send"):
            func()


    # Created About Us page
    if page_selection == "About Us":
        st.image("https://raw.githubusercontent.com/Anravus/unsupervised-predict-streamlit-template/developing/resources/images/AboutUs.png",
                 use_column_width=True)

        # Our Company background story
        st.title("OUR STORY")
        st.markdown("""
                    OneFlix started in the Summer of 2019.

                    A group of individuals came together with the same vision:

                            Create recommender systems for content that users would find interesting.

                    A concept now brought to perfection by OneFlix of creators.

                    Today, OneFlix are helping users in selecting various content that peaks their interests and exposing them to sources and sites that they would normally overlook which
                    could be of interest for them.

                    OneFlix features a variety of recommender systems that users can make use of, using a broad spectrum of data preprocessing techniques and parameters.

                    Simply put: There's content for every user, mindset and style.
                    """)

        # Content creators who worked on this assignment
        st.title("MEET THE TEAM")

        st.header("Makhosazane Seroka")

        st.header("Mixo Lucrencia Shitlhangu")

        st.header("Percy Mokone")

        st.header("Precious Sekgathume")

        st.header("Sevha Vukeya")

        st.header("Suvarna Chetty")

    # Created a references page
    if page_selection == "References":
        st.title("REFERENCES")
        st.markdown("A list of websites visited in order for the completion of this assignment")
        st.write("https://www.glassdoor.com/Job-Descriptions/Data-Scientist.htm")


if __name__ == '__main__':
    main()
