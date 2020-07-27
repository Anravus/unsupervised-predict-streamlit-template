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
from bokeh.models.widgets import Div

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

# App declaration
def main():

    st.sidebar.image("https://raw.githubusercontent.com/Anravus/unsupervised-predict-streamlit-template/developing/resources/images/OneFlixS%20(1).png",
                     use_column_width=True)
    # Creating load data sign on sidebar
    st.sidebar.subheader(":heavy_check_mark: Data is loaded")
    st.sidebar.text_input("link to train data", "https://raw.githubusercontent.com/Anravus/unsupervised-predict-streamlit-template/developing/resources/data/movies.csv")

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    # Creating multiple pages
    st.sidebar.title("Menu")
    page_options = ["Recommender System","Solution Overview","Our Mission","History Of Cinema","Machine Learning","Data Exploration","Our Products and Services","About Us","References"]

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

        st.image("https://raw.githubusercontent.com/Anravus/unsupervised-predict-streamlit-template/developing/resources/images/OneFlixS%20(2).png",
                 use_column_width=True)
        st.title("🎬 OneFlix 🎬")
        st.markdown("""
                    Wouldn't you like to know what movie to watch next. Tired of the same old boring movies. Would you not like to have a tailored movie experience just for you.
                    Well, OneFlix looks to do just that. Our highly skilled team of data scientists have designed a system that will do all of that and more!

                    We use state of the art Unsupervised Machine Learning techniques to enhance your viewing experience and bring you the best movie recommendations within just a few clicks.

                    Join us for the next level viewing experience.
                    Try out our app now and experience the new way.
                    Advance AI is just one click away.
                    """)

        st.header("Synopsis")
        st.markdown("""
                    In today’s technology driven world, recommender systems are socially and economically critical for ensuring that individuals can make appropriate choices surrounding
                    the content they engage with on a daily basis. One application where this is especially true surrounds movie content recommendations; where intelligent algorithms can
                    help viewers find great titles from tens of thousands of options and discover loads more.

                    Providing an accurate and robust solution to this challenge has immense economic potential, with users of the system being exposed to content they would like to view or
                    purchase - generating revenue and platform affinity, while also enhancing consumer satisfaction.
                    """)

    # Created a history of cinema page
    if page_selection == "History Of Cinema":
        st.image("https://raw.githubusercontent.com/Anravus/unsupervised-predict-streamlit-template/developing/resources/images/History.png",
                 use_column_width=True )

        st.sidebar.title("Table of contents")
        st.sidebar.info("The table of contents is interactive")
        class Toc:

            def __init__(self):
                self._items = []
                self._placeholder = None

            def title(self, text):
                self._markdown(text, "h1")

            def header(self, text):
                self._markdown(text, "h2", " " * 2)

            def subheader(self, text):
                self._markdown(text, "h3", " " * 4)

            def placeholder(self, sidebar = False ):
                self._placeholder = st.sidebar

            def generate(self):
                if self._placeholder:
                    self._placeholder.markdown("\n".join(self._items), unsafe_allow_html=True)

            def _markdown(self, text, level, space=""):
                key = "".join(filter(str.isalnum, text)).lower()

                st.markdown(f"<{level} id='{key}'>{text}</{level}>", unsafe_allow_html=True)
                self._items.append(f"{space}* <a href='#{key}'>{text}</a>")


        toc = Toc()

        toc.placeholder()

        st.image("https://raw.githubusercontent.com/Anravus/unsupervised-predict-streamlit-template/developing/resources/images/A%20short%20history.png",
                 use_column_width=True)

        st.markdown("""
                    Cinematography is the illusion of movement by the recording and subsequent rapid projection of many still photographic pictures on a screen. Originally a product of
                    19th-century scientific endeavour, cinema has become a medium of mass entertainment and communication, and today it is a multi-billion-dollar industry.
                    """)

        toc.title("🎥 Who invented cinema? 🎥")
        st.markdown("""
                    No one person invented cinema. However, in 1891 the Edison Company successfully demonstrated a prototype of the Kinetoscope, which enabled one person at a time to view
                    moving pictures.

                    The first public Kinetoscope demonstration took place in 1893. By 1894 the Kinetoscope was a commercial success, with public parlours established around the world.

                    The first to present projected moving pictures to a paying audience were the Lumière brothers in December 1895 in Paris, France. They used a device of their own making,
                    the Cinématographe, which was a camera, a projector and a film printer all in one.
                    """)
        st.image("https://www.scienceandmediamuseum.org.uk/sites/default/files/styles/embedded_image/public/2020-06/Kinetophonebis1_0.jpg?itok=TWbBGPML", caption ="Publicity image of Edison Kinetophone, c.1895" )
        st.image("https://www.scienceandmediamuseum.org.uk/sites/default/files/styles/smg_carousel_zoom/public/347701996.jpg", caption = "Lumière Cinématographe, c.1896", use_column_width=True)

        toc.title("🎞️ What were early films like? 🎞️")
        st.markdown("""
                    At first, films were very short, sometimes only a few minutes or less. They were shown at fairgrounds, music halls, or anywhere a screen could be set up and a room darkened.
                    Subjects included local scenes and activities, views of foreign lands, short comedies and newsworthy events.

                    The films were accompanied by lectures, music and a lot of audience participation. Although they did not have synchronised dialogue, they were not ‘silent’ as they are
                    sometimes described.
                    """)

        toc.title("📼 The rise of the film industry 📼")
        st.markdown("""
                    By 1914, several national film industries were established. At this time, Europe, Russia and Scandinavia were the dominant industries; America was much less important.
                    Films became longer and storytelling, or narrative, became the dominant form.

                    As more people paid to see movies, the industry which grew around them was prepared to invest more money in their production, distribution and exhibition, so large
                    studios were established and dedicated cinemas built. The First World War greatly affected the film industry in Europe, and the American industry grew in relative importance.

                    The first 30 years of cinema were characterised by the growth and consolidation of an industrial base, the establishment of the narrative form, and refinement of
                    technology.
                    """)

        toc.title("🌈 Adding colour 🌈")
        st.markdown("""
                    Colour was first added to black-and-white movies through hand colouring, tinting, toning and stencilling.

                    By 1906, the principles of colour separation were used to produce so-called ‘natural colour’ moving images with the British Kinemacolor process, first presented to the
                    public in 1909.

                    Kinemacolor was primarily used for documentary (or ‘actuality’) films, such as the epic With Our King and Queen Through India (also known as The Delhi Durbar) of 1912,
                    which ran for over 2 hours in total.

                    The early Technicolor processes from 1915 onwards were cumbersome and expensive, and colour was not used more widely until the introduction of its three‑colour process
                    in 1932. It was used for films such as Gone With the Wind and The Wizard of Oz (both 1939) in Hollywood and A Matter of Life and Death (1946) in the UK.
                    """)
        st.image("https://raw.githubusercontent.com/Anravus/unsupervised-predict-streamlit-template/developing/resources/images/Adding%20Colour.jpg", caption = "1. Frames of stencil colour film, 2. Kinemacolor cine camera made by Moy and Bastie to Charles Urban's design(1909), 3. Advertisement for with our king and queen through India(1912), 4. Advertisement for Kinemacolor, 5. Technicolor cine camera", use_column_width =True )

        toc.title("🎼 Adding sound 🎼")
        st.markdown("""
                    The first attempts to add synchronised sound to projected pictures used phonographic cylinders or discs.

                    The first feature-length movie incorporating synchronised dialogue, The Jazz Singer (USA, 1927), used the Warner Brothers’ Vitaphone system, which employed a separate
                    record disc with each reel of film for the sound.

                    This system proved unreliable and was soon replaced by an optical, variable density soundtrack recorded photographically along the edge of the film, developed originally
                    for newsreels such as Movietone.
                    """)
        st.image("https://www.scienceandmediamuseum.org.uk/sites/default/files/styles/embedded_image/public/2020-06/large_2017_5390__0001__0.jpg?itok=poRniSDa", use_column_width= True, caption= "Vitaphone disc, 1930.")

        toc.title("📀 Cinema's golden age 📀")
        st.markdown("""
                    By the early 1930s, nearly all feature-length movies were presented with synchronised sound and, by the mid-1930s, some were in full colour too. The advent of sound
                    secured the dominant role of the American industry and gave rise to the so-called ‘Golden Age of Hollywood’.

                    During the 1930s and 1940s, cinema was the principal form of popular entertainment, with people often attending cinemas twice a week. Ornate ’super’ cinemas or ‘picture
                    palaces’, offering extra facilities such as cafés and ballrooms, came to towns and cities; many of them could hold over 3,000 people in a single auditorium.

                    In Britain, the highest attendances occurred in 1946, with over 31 million visits to the cinema each week.
                    """)
        st.image("https://www.scienceandmediamuseum.org.uk/sites/default/files/styles/embedded_image/public/2020-06/large_1983_5236_10530_1.jpg?itok=3rZUu2hD", caption = "Cinema audience, 1932, James Jarché.", use_column_width=True)


        toc.title("↖️ What is the aspect ratio? ↘️")
        st.markdown("""
                    Thomas Edison had used perforated 35mm film in the Kinetoscope, and in 1909 this was adopted as the worldwide industry standard. The picture had a width-to-height
                    relationship—known as the aspect ratio—of 4:3 or 1.33:1. The first number refers to the width of the screen, and the second to the height. So for example, for every 4
                    centimetres in width, there will be 3 in height.

                    With the advent of optical sound, the aspect ratio was adjusted to 1.37:1. This is known as the ‘Academy ratio’, as it was officially approved by the Academy of Motion
                    Picture Arts and Sciences (the Oscars people) in 1932.

                    Although there were many experiments with other formats, there were no major changes in screen ratios until the 1950s.
                    """)

        st.title("📺 How did cinema compete with television? 📺")
        st.markdown("""
                    The introduction of television in America prompted a number of technical experiments designed to maintain public interest in cinema.

                    In 1952, the Cinerama process, using three projectors and a wide, deeply curved screen together with multi-track surround sound, was premiered. It had a very large aspect
                    ratio of 2.59:1, giving audiences a greater sense of immersion, and proved extremely popular.

                    However, Cinerama was technically complex and therefore expensive to produce and show. Widescreen cinema was not widely adopted by the industry until the invention of
                    CinemaScope in 1953 and Todd‑AO in 1955. Both processes used single projectors in their presentation.

                    CinemaScope ‘squeezed’ images on 35mm film; when projected, they were expanded laterally by the projector lens to fit the screen. Todd-AO used film with a width of 70mm.
                    By the end of the 1950s, these innovations had effectively changed the shape of the cinema screen, with aspect ratios of either 2.35:1 or 1.66:1 becoming standard.
                    Stereo sound, which had been experimented with in the 1940s, also became part of the new widescreen experience.

                    Specialist large-screen systems using 70mm film were also developed. The most successful of these has been IMAX, which as of 2020 has over 1,500 screens around the world.
                    For many years IMAX cinemas have shown films specially made in its unique 2D or 3D formats but more recently they have shown popular mainstream feature films which have been
                    digitally re-mastered in the IMAX format, often with additional scenes or 3D effects.
                    """)
        st.image("https://www.scienceandmediamuseum.org.uk/sites/default/files/styles/embedded_image/public/2020-06/BR180001.jpeg?itok=V6nJu0ZU", caption= "Installation of IMAX screen at the museum, 1983.", use_column_width= True)

        toc.title("👨‍👩‍👧‍👧 How have cinema attendance figueres changed? 👨‍👩‍👧‍👧")
        st.markdown("""
                    While cinemas had some success in fighting the competition of television, they never regained the position and influence they held in the 1930s and 40s, and over the next
                    30 years audiences dwindled. By 1984 cinema attendances in Britain had declined to one million a week.

                    By the late 2000s, however, that number had trebled. The first British multiplex was built in Milton Keynes in 1985, sparking a boom in out-of-town multiplex cinemas.

                    Today, most people see films on television, whether terrestrial, satellite or subscription video on demand (SVOD) services. Streaming film content on computers, tablets
                    and mobile phones is becoming more common as it proves to be more convenient for modern audiences and lifestyles.

                    Although America still appears to be the most influential film industry, the reality is more complex. Many films are produced internationally—either made in various
                    countries or financed by multinational companies that have interests across a range of media.
                    """)
        st.image("https://www.scienceandmediamuseum.org.uk/sites/default/files/styles/embedded_image/public/2020-06/1200px-MK%2C_The_Point_-_panoramio.jpg?itok=_TMJGmty", caption= "The Point multiplex cinema, Milton Keynes.", use_column_width= True)

        toc.title("⏭️ What's next? ⏭️")
        st.markdown("""
                    In the past 20 years, film production has been profoundly altered by the impact of rapidly improving digital technology. Most mainstream productions are now shot on
                    digital formats with subsequent processes, such as editing and special effects, undertaken on computers.

                    Cinemas have invested in digital projection facilities capable of producing screen images that rival the sharpness, detail and brightness of traditional film projection.
                    Only a small number of more specialist cinemas have retained film projection equipment.

                    In the past few years there has been a revival of interest in 3D features, sparked by the availability of digital technology. Whether this will be more than a short-term
                    phenomenon (as previous attempts at 3D in the 1950s and 1980s had been) remains to be seen, though the trend towards 3D production has seen greater investment and industry
                    commitment than before.
                    """)



        toc.generate()

    # Created Machine Learning Page
    if page_selection == "Machine Learning":
        st.image("https://raw.githubusercontent.com/Anravus/unsupervised-predict-streamlit-template/developing/resources/images/MachineLearning.png",
                 use_column_width=True)

        # table of contents on the sidebar
        st.sidebar.title("Table of contents")
        st.sidebar.info("The table of contents is interactive")
        class Toc2:
            def __init__(self):
                self._items = []
                self._placeholder = None

            def title(self, text):
                self._markdown(text, "h1")

            def header(self, text):
                self._markdown(text, "h2", " " * 2)

            def subheader(self, text):
                self._markdown(text, "h3", " " * 4)

            def placeholder(self, sidebar = False ):
                self._placeholder = st.sidebar

            def generate(self):
                if self._placeholder:
                    self._placeholder.markdown("\n".join(self._items), unsafe_allow_html=True)

            def _markdown(self, text, level, space=""):
                key = "".join(filter(str.isalnum, text)).lower()

                st.markdown(f"<{level} id='{key}'>{text}</{level}>", unsafe_allow_html=True)
                self._items.append(f"{space}* <a href='#{key}'>{text}</a>")


        toc2 = Toc2()

        toc2.placeholder()


        st.image("https://expertsystem.com/wp-content/uploads/2017/03/machine-learning-definition.jpeg",
                 use_column_width= True)

        toc2.title("What is Machine Learning?")
        st.markdown("""
                    Machine learning is an application of artificial intelligence (AI) that provides systems the ability to automatically learn and improve from experience without
                    being explicitly programmed. Machine learning focuses on the development of computer programs that can access data and use it learn for themselves.
                    The process of learning begins with observations or data, such as examples, direct experience, or instruction, in order to look for patterns in data and make
                    better decisions in the future based on the examples that we provide. The primary aim is to allow the computers learn automatically without human intervention
                    or assistance and adjust actions accordingly.
                    But, using the classic algorithms of machine learning, text is considered as a sequence of keywords; instead, an approach based on semantic analysis mimics the
                    human ability to understand the meaning of a text.
                    """)


        toc2.header("🤖 Machine Learning Methods 🤖")
        st.markdown("""
                    Machine learning algorithms are often categorized as supervised or unsupervised.
                    """)

        st.image("https://blog.bismart.com/hs-fs/hubfs/Machinne%20Learning%20Types%20Bismart.png?width=900&name=Machinne%20Learning%20Types%20Bismart.png",
                 use_column_width= True)

        toc2.subheader("Supervised Machine Learning techniques")
        st.markdown("""
                    Supervised machine learning algorithms can apply what has been learned in the past to new data using labeled examples to predict future events. Starting from
                    the analysis of a known training dataset, the learning algorithm produces an inferred function to make predictions about the output values. The system is able
                    to provide targets for any new input after sufficient training.
                    The learning algorithm can also compare its output with the correct, intended output and find
                    errors in order to modify the model accordingly.
                    """)
        st.image("https://miro.medium.com/max/929/1*U5GzWYAm8t1urqdDxpiOFw.jpeg",
                 use_column_width= True)

        toc2.subheader("Unsupervised Machine Learning techniques")
        st.markdown("""
                    Unsupervised machine learning algorithms are used when the information used to train is neither classified nor labeled. Unsupervised learning studies how systems
                    can infer a function to describe a hidden structure from unlabeled data. The system doesn't figure out the right output, but it explores the data and can draw
                    inferences from datasets to describe hidden structures from unlabeled data.
                    """)
        st.image("https://www.newtechdojo.com/wp-content/uploads/2018/03/How-unsupervised-machine-Learning-works.jpg",
                 use_column_width= True)

        toc2.title("Supervised Machine Learning")
        st.image("https://miro.medium.com/max/1400/1*t8igzDSUC-1qaJQRQpbwBA.png",
                 use_column_width = True)
        toc2.header("📚 Classification 📚")
        toc2.subheader("Brief Overview: Classification")
        st.markdown("""
                    Classification is a process of categorizing a given set of data into classes, It can be performed on both structured or unstructured data. The process starts with
                    predicting the class of given data points. The classes are often referred to as target, label or categories.

                    The classification predictive modeling is the task of approximating the mapping function from input variables to discrete output variables. The main goal is to
                    identify which class/category the new data will fall into.
                    """)
        st.image("https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2019/11/classification.png",
                 use_column_width = True)
        toc2.subheader("Types of Algorithms")
        st.markdown("""
                    **Logistic Regression**

                    Logistic regression is a machine learning algorithm for classification. In this algorithm, the probabilities describing the possible outcomes of a single trial are
                    modelled using a logistic function.

                    _Advantages:_

                        Logistic regression is designed for this purpose (classification), and is most
                        useful for understanding the influence of several independent variables on a
                        single outcome variable.

                    _Disadvantages:_

                        Works only when the predicted variable is binary, assumes all predictors are
                        independent of each other and assumes data is free of missing values.
                    """)
        st.image("https://mk0analyticsindf35n9.kinstacdn.com/wp-content/uploads/2018/01/Screen-Shot-2018-01-19-at-10.52.28-AM.png",
                 use_column_width=True)

        st.markdown("""
                    **Naïve Bayes**

                    Naive Bayes algorithm based on Bayes’ theorem with the assumption of independence between every pair of features. Naive Bayes classifiers work well in many
                    real-world situations such as document classification and spam filtering.

                    _Advantages:_

                        This algorithm requires a small amount of training data to estimate the necessary
                        parameters. Naive Bayes classifiers are extremely fast compared to more
                        sophisticated methods.

                    _Disadvantages:_

                        Naive Bayes is is known to be a bad estimator.
                    """)
        st.image("https://mk0analyticsindf35n9.kinstacdn.com/wp-content/uploads/2018/01/Screen-Shot-2018-01-19-at-10.53.58-AM.png",
                 use_column_width=True)

        st.markdown("""
                    **K-Nearest Neighbours**

                    Neighbours based classification is a type of lazy learning as it does not attempt to construct a general internal model, but simply stores instances of the
                    training data. Classification is computed from a simple majority vote of the k nearest neighbours of each point.

                    _Advantages:_

                        This algorithm is simple to implement, robust to noisy training data, and
                        effective if training data is large.

                    _Disadvantages:_

                        Need to determine the value of K and the computation cost is high as it needs
                        to compute the distance of each instance to all the training samples.
                    """)
        st.image("https://mk0analyticsindf35n9.kinstacdn.com/wp-content/uploads/2018/01/Screen-Shot-2018-01-19-at-10.58.19-AM.png",
                 use_column_width=True)

        st.markdown("""
                    **Decision Tree**

                    Given a data of attributes together with its classes, a decision tree produces a sequence of rules that can be used to classify the data.

                    _Advantages:_

                        Decision Tree is simple to understand and visualise, requires little data
                        preparation, and can handle both numerical and categorical data.

                    _Disadvantages:_

                        Decision tree can create complex trees that do not generalise well, and
                        decision trees can be unstable because small variations in the data might
                        result in a completely different tree being generated.
                    """)
        st.image("https://mk0analyticsindf35n9.kinstacdn.com/wp-content/uploads/2018/01/Screen-Shot-2018-01-19-at-10.59.33-AM.png",
                 use_column_width=True)

        st.markdown("""
                    **Random Forest**

                    Random forest classifier is a meta-estimator that fits a number of decision trees on various sub-samples of datasets and uses average to improve the predictive
                    accuracy of the model and controls over-fitting. The sub-sample size is always the same as the original input sample size but the samples are drawn with replacement.

                    _Advantages:_

                        Reduction in over-fitting and random forest classifier is more accurate than
                        decision trees in most cases.

                    _Disadvantages:_

                        Slow real time prediction, difficult to implement, and complex algorithm.
                    """)
        st.image("https://mk0analyticsindf35n9.kinstacdn.com/wp-content/uploads/2018/01/Screen-Shot-2018-01-19-at-11.00.06-AM.png",
                 use_column_width=True)

        st.markdown("""
                    **Support Vector Machine**

                    Support vector machine is a representation of the training data as points in space separated into categories by a clear gap that is as wide as possible. New examples
                    are then mapped into that same space and predicted to belong to a category based on which side of the gap they fall.

                    _Advantages:_

                        Effective in high dimensional spaces and uses a subset of training points in the
                        decision function so it is also memory efficient.

                    _Disadvantages:_

                        The algorithm does not directly provide probability estimates, these are calculated
                        using an expensive five-fold cross-validation.
                    """)
        st.image("https://mk0analyticsindf35n9.kinstacdn.com/wp-content/uploads/2018/01/Screen-Shot-2018-01-19-at-11.00.44-AM.png",
                 use_column_width=True)



        toc2.header("📈 Regression 📈")
        toc2.subheader("Brief Overview: Regression")
        st.markdown("""
                    Regression is another form of supervised learning. The difference between classification and regression is that regression outputs a number rather than a class.
                    Therefore, regression is useful when predicting number based problems like stock market prices, the temperature for a given day, or the probability of an event.
                    """ )
        st.image("https://miro.medium.com/max/1400/1*LbvtG6tsDwTeS7QPn6NfGw.png",
                 use_column_width = True)

        toc2.subheader("Types of Algorithms")
        st.markdown("""
                    **Linear Regression**

                    It is the simplest form of regression. It is a technique in which the dependent variable is continuous in nature. The relationship between the dependent variable and
                    independent variables is assumed to be linear in nature.We can observe that the given plot represents a somehow linear relationship between the mileage and displacement
                    of cars. The green points are the actual observations while the black line fitted is the line of regression
                    """)
        st.image("https://4.bp.blogspot.com/-IOOxgPaXMVc/Wlj3LWvcnjI/AAAAAAAACKE/UeTFYvAxDmUDel5UBjdifeWaApB3-dXVgCLcBGAs/s1600/img1.jpg",
                 use_column_width=True)
        st.image("https://2.bp.blogspot.com/-xbqTM5K3bIU/WkzhtHMPEmI/AAAAAAAACFs/RULnlMKw_0U14oRWOUcuETJNt9TBYiJEgCLcBGAs/s1600/b.jpg",
                 use_column_width=True)

        st.markdown("""
                    **Polynomial Regression**

                    It is a technique to fit a nonlinear equation by taking polynomial functions of independent variable.
                    In the figure given below, you can see the red curve fits the data better than the green curve. Hence in the situations where the relation between the dependent and
                    independent variable seems to be non-linear we can deploy Polynomial Regression Models.
                    """)
        st.image("https://1.bp.blogspot.com/-dODuK8N5h1Q/Wlnyb3V9HFI/AAAAAAAACL4/WxQtCJ1pM5wccDABg4wIrTBUB0vlikXQQCLcBGAs/s1600/poly1.jpg",
                use_column_width=True)
        st.image("https://1.bp.blogspot.com/-wrJdHn0X_Y8/Wln1K2YZO5I/AAAAAAAACMI/gScVjBesYCY0S4bqUV_tVL6DELUjVcvLwCLcBGAs/s1600/poly2.jpg",
                 use_column_width=True)

        st.markdown("""
                     **Ridge Regression**
                     It's important to understand the concept of regularization before jumping to ridge regression.

                     _Regularization_

                        Regularization helps to solve over fitting problem which implies model performing well
                        on training data but performing poorly on validation (test) data. Regularization solves
                        this problem by adding a penalty term to the objective function and control the model
                        complexity using that penalty term.

                    Regularization is generally useful in the following situations:

                        - Large number of variables
                        - Low ratio of number observations to number of variables
                        - High Multi-Collinearity

                    _L1 Loss function or L1 Regularization_

                    In L1 regularization we try to minimize the objective function by adding a penalty term to the sum of the absolute values of coefficients. This is also known as
                    least absolute deviations method. Lasso Regression makes use of L1 regularization.

                    _L2 Loss function or L2 _Regularization_

                    In L2 regularization we try to minimize the objective function by adding a penalty term to thesum of the squares of coefficients.RidgeRegression or shrinkage regression
                    makes use of L2 regularization.

                    > In general, L2 performs better than L1 regularization. L2 is efficient in
                        terms of computation. There is one area where L1 is considered as a preferred
                        option over L2. L1 has in-built feature selection for sparse feature spaces.
                        For example, you are predicting whether a person is having a brain tumor using
                        more than 20,000 genetic markers (features). It is known that the vast majority
                        of genes have little or no effect on the presence or severity of most diseases.

                    """)


        toc2.header("🔗 Differences between Classification & Regression 🔗")
        diff = pd.DataFrame({
                            'Regression': ["In Regression, the output variable must be of continuous nature or real value.",
                                           "The task of the regression algorithm is to map the input value (x) with the continuous output variable(y).",
                                           "Regression Algorithms are used with continuous data.",
                                           "In Regression, we try to find the best fit line, which can predict the output more accurately.",
                                           "Regression algorithms can be used to solve the regression problems such as Weather Prediction, House price prediction, etc.",
                                           "The regression Algorithm can be further divided into Linear and Non-linear Regression."],
                            'Classification': ["In Classification, the output variable must be a discrete value.",
                                               "The task of the classification algorithm is to map the input value(x) with the discrete output variable(y).",
                                               "Classification Algorithms are used with discrete data.",
                                               "In Classification, we try to find the decision boundary, which can divide the dataset into different classes.",
                                               "Classification Algorithms can be used to solve classification problems such as Identification of spam emails, Speech Recognition, Identification of cancer cells, etc.",
                                               "The Classification algorithms can be divided into Binary Classifier and Multi-class Classifier."]
                            })

        st.table(diff)


        toc2.header("⚠️ Challenges ⚠️")
        st.markdown("""
                    - Irrelevant input feature present training data could give inaccurate results
                    - Data preparation and pre-processing is always a challenge.
                    - Accuracy suffers when impossible, unlikely, and incomplete values have been inputted as training data
                    - If the concerned expert is not available, then the other approach is "brute-force." It means you need to think that the right features (input variables) to train
                      the machine on. It could be inaccurate.
                    """)

        toc2.header("👍 Advantages 👍")
        st.markdown("""
                    - Supervised learning allows you to collect data or produce a data output from the previous experience
                    - Helps you to optimize performance criteria using experience
                    - Supervised machine learning helps you to solve various types of real-world computation problems.
                    """)

        toc2.header("👎 Disadvantages 👎")
        st.markdown("""
                    - Decision boundary might be overtrained if your training set which doesn't have examples that you want to have in a class
                    - You need to select lots of good examples from each class while you are training the classifier.
                    - Classifying big data can be a real challenge.
                    - Training for supervised learning needs a lot of computation time.
                    """)

        toc2.title("Unsupervised Machine Learning")
        st.markdown("""
                    _Reasons for using Unsupervised Learning:_

                        - Unsupervised machine learning finds all kind of unknown patterns in data.
                        - Unsupervised methods help you to find features which can be useful for categorization.
                        - It is taken place in real time, so all the input data to be analyzed and labeled in
                          the presence of learners.
                        - It is easier to get unlabeled data from a computer than labeled data, which needs
                          manual intervention.
                    """)
        toc2.header("📉 Types of Unsupervised Learning 📉")
        st.markdown("""
                    Unsupervised learning techniques further grouped into clustering and association problems.
                    """)
        toc2.subheader("Clustering")
        st.image("https://www.guru99.com/images/1/030819_1030_Unsupervise3.png",
                 use_column_width=True)
        st.markdown("""
                    Clustering is an important concept when it comes to unsupervised learning. It mainly deals with finding a structure or pattern in a collection of uncategorized data.
                    Clustering algorithms will process your data and find natural clusters(groups) if they exist in the data. You can also modify how many clusters your algorithms should
                    identify. It allows you to adjust the granularity of these groups.

                    **Hierarchical Clustering:**

                    Hierarchical clustering is an algorithm which builds a hierarchy of clusters. It begins with all the data which is assigned to a cluster of their own. Here, two close
                    cluster are going to be in the same cluster. This algorithm ends when there is only one cluster left.""")
        st.image("https://lh3.googleusercontent.com/proxy/_i8jxxJl4CCrnBqqMt_83pB5L0fxLL0bglnm7TwueffGxnXYvxIMTLiQ14zNKvodo7yWmI4k9YrEzU59KttHaEbVRcLLX31NQ2zhYmw3RLBBthMmfexu34Kwe-X37a-TozasK4YDRPrEy32ZSb3e3lOqQUL_YugN-QWLfSci1-Vn6lbOrPOoJ19NIVUSwVWjwQzXZA", use_column_width=True)

        st.markdown("""
                    **K-means Clustering:**

                    K means it is an iterative clustering algorithm which helps you to find the highest value for every iteration. Initially, the desired number of clusters are selected.
                    In this clustering method, you need to cluster the data points into k groups. A larger k means smaller groups with more granularity in the same way. A lower k means
                    larger groups with less granularity.

                    The output of the algorithm is a group of "labels." It assigns data point to one of the k groups. In k-means clustering, each group is defined by creating a centroid for
                    each group. The centroids are like the heart of the cluster, which captures the points closest to them and adds them to the cluster.

                    _K-mean clustering further defines two subgroups:_

                    Agglomerative clustering

                        This type of K-means clustering starts with a fixed number of clusters.
                        It allocates all data into the exact number of clusters. This clustering
                        method does not require the number of clusters K as an input. Agglomeration
                        process starts by forming each data as a single cluster.

                        This method uses some distance measure, reduces the number of clusters
                        (one in each iteration) by merging process. Lastly, we have one big cluster
                        that contains all the objects.

                    Dendrogram

                        In the Dendrogram clustering method, each level will represent a possible
                        cluster. The height of dendrogram shows the level of similarity between two
                        join clusters. The closer to the bottom of the process they are more similar
                        cluster which is finding of the group from dendrogram which is not natural
                        and mostly subjective.

                    **K- Nearest neighbors**

                    K- nearest neighbour is the simplest of all machine learning classifiers. It differs from other machine learning techniques, in that it doesn't produce a model.
                    It is a simple algorithm which stores all available cases and classifies new instances based on a similarity measure.

                    It works very well when there is a distance between examples. The learning speed is slow when the training set is large, and the distance calculation is nontrivial.

                    **Principal Components Analysis:**

                    In case you want a higher-dimensional space. You need to select a basis for that space and only the 200 most important scores of that basis. This base is known as
                    a principal component. The subset you select constitute is a new space which is small in size compared to original space. It maintains as much of the complexity of data
                    as possible.
                    """)

        toc2.subheader("Association")
        st.markdown("""
                    Association rules allow you to establish associations amongst data objects inside large databases. This unsupervised technique is about discovering interesting
                    relationships between variables in large databases. For example, people that buy a new home most likely to buy new furniture.

                    Other Examples:

                        - A subgroup of cancer patients grouped by their gene expression measurements
                        - Groups of shopper based on their browsing and purchasing histories
                        - Movie group by the rating given by movies viewers
                    """)
        toc2.header("💾 Application 💾")
        st.markdown("""
                    - Clustering automatically split the dataset into groups base on their similarities
                    - Anomaly detection can discover unusual data points in your dataset. It is useful for finding fraudulent transactions
                    - Association mining identifies sets of items which often occur together in your dataset
                    - Latent variable models are widely used for data preprocessing. Like reducing the number of features in a dataset or decomposing the dataset into multiple components
                    """)
        toc2.header("👎 Disadvantages of Unsupervised Learning 👎")
        st.markdown("""
                    - You cannot get precise information regarding data sorting, and the output as data used in unsupervised learning is labeled and not known
                    - Less accuracy of the results is because the input data is not known and not labeled by people in advance. This means that the machine requires to do this itself.
                    - The spectral classes do not always correspond to informational classes.
                    - The user needs to spend time interpreting and label the classes which follow that classification.
                    - Spectral properties of classes can also change over time so you can't have the same class information while moving from one image to another.
                    """)

        toc2.header("🔗 Difference between Supervised & Unsupervised 🔗")
        st.video("https://youtu.be/rHeaoaiBM6Y")

        toc2.generate()

    # Created Data Exploration page
    if page_selection == "Data Exploration":
        st.image("https://raw.githubusercontent.com/Anravus/unsupervised-predict-streamlit-template/developing/resources/images/DataExploration.png",
                 use_column_width=True)

        st.markdown("""
    <iframe width="600" height="375" src="https://app.powerbi.com/view?r=eyJrIjoiMWQ3YTE1MjgtODQ0My00Mzk0LThhZTAtYmQ5ZmFlNDA4ZmQxIiwidCI6IjQ0MTEyYTBhLTlmN2ItNDNhNi05Y2FhLWY0NTA0NDFmMjlhNSIsImMiOjl9&pageName=ReportSection/" frameborder="0" style="border:0" allowfullscreen></iframe>
    """, unsafe_allow_html=True)

        if st.button('Go to Dashboard'):
            js = "window.open('https://app.powerbi.com/view?r=eyJrIjoiMWQ3YTE1MjgtODQ0My00Mzk0LThhZTAtYmQ5ZmFlNDA4ZmQxIiwidCI6IjQ0MTEyYTBhLTlmN2ItNDNhNi05Y2FhLWY0NTA0NDFmMjlhNSIsImMiOjl9&pageName=ReportSection/')"  # New tab or window
            js = "window.location.href = 'https://app.powerbi.com/view?r=eyJrIjoiMWQ3YTE1MjgtODQ0My00Mzk0LThhZTAtYmQ5ZmFlNDA4ZmQxIiwidCI6IjQ0MTEyYTBhLTlmN2ItNDNhNi05Y2FhLWY0NTA0NDFmMjlhNSIsImMiOjl9&pageName=ReportSection/'"  # Current tab
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)
        st.info("Click on the 'Go to Dashboard' button to go to the webpage")


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

        # table of contents on the sidebar
        st.sidebar.title("Table of contents")
        st.sidebar.info("The table of contents is interactive")
        class Toc3:
            def __init__(self):
                self._items = []
                self._placeholder = None

            def title(self, text):
                self._markdown(text, "h1")

            def header(self, text):
                self._markdown(text, "h2", " " * 2)

            def subheader(self, text):
                self._markdown(text, "h3", " " * 4)

            def placeholder(self, sidebar = False ):
                self._placeholder = st.sidebar

            def generate(self):
                if self._placeholder:
                    self._placeholder.markdown("\n".join(self._items), unsafe_allow_html=True)

            def _markdown(self, text, level, space=""):
                key = "".join(filter(str.isalnum, text)).lower()

                st.markdown(f"<{level} id='{key}'>{text}</{level}>", unsafe_allow_html=True)
                self._items.append(f"{space}* <a href='#{key}'>{text}</a>")


        toc3 = Toc3()

        toc3.placeholder()


        # Our Company background story
        toc3.title("OUR STORY")
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
        toc3.title("MEET THE TEAM")

        toc3.header("Makhosazane Seroka")

        toc3.header("Mixo Lucrencia Shitlhangu")
        st.markdown("""
                    Data Scientist in training with a passion to deliver valuable data through analytical functions as well as data retrieval methods.  My focus, as an aspiring professional,
                    is to utilize my strengths in database management to make a positive impact.
                    """)
        st.image("https://raw.githubusercontent.com/Anravus/unsupervised-predict-streamlit-template/developing/resources/images/MixoL.jpg", use_column_width = True)

        toc3.header("Percy Mokone")

        toc3.header("Precious Sekgathume")
        st.markdown("""
                    A Social Sciences graduate who decided to move out of her comfort zone and took a leap into the Data Science field in January 2020. Precious hope to incorporate Data
                    Science and the Social Sciences for the betterment of her career.. She’s an avid reader, a mental health advocate. She has previously worked closely with children and
                    believes greatly that dream work makes the team work..
                    """)
        st.image("https://raw.githubusercontent.com/Anravus/unsupervised-predict-streamlit-template/developing/resources/images/PreciousS.jpeg", use_column_width = True)

        toc3.header("Sevha Vukeya")

        toc3.header("Suvarna Chetty")
        st.markdown("""
                    Innovative and performance-driven Entrepreneur with a deep passion for technology and business. Detail-orientated data science student with a background in Accounting Science.
                    Passionate with a zest for solving problems.
                    """)
        st.image("https://raw.githubusercontent.com/Anravus/unsupervised-predict-streamlit-template/developing/resources/images/Suvarna.jpeg",
                 caption = '"Give me speckled eggs and a computer and I can take on the world"- Suvarna', use_column_width=True)

        toc3.generate()

    # Created a references page
    if page_selection == "References":
        st.title("REFERENCES")
        st.markdown("**A list of websites visited in order for the completion of this assignment**")
        st.markdown("""https://www.glassdoor.com/Job-Descriptions/Data-Scientist.htm
                    https://analyticsindiamag.com/7-types-classification-algorithms/
                    https://www.guru99.com/supervised-machine-learning.html
                    https://www.javatpoint.com/regression-vs-classification-in-machine-learning
                    https://searchenterpriseai.techtarget.com/definition/supervised-learning
                    https://www.guru99.com/unsupervised-machine-learning.html
                    https://searchenterpriseai.techtarget.com/definition/supervised-learning
                    https://www.analyticssteps.com/blogs/7-types-regression-technique-you-should-know-machine-learning
                    https://www.listendata.com/2018/03/regression-analysis.html
                    https://www.analyticsinsight.net/6-types-of-regressions-have-you-heard/
                    https://www.scienceandmediamuseum.org.uk/objects-and-stories/very-short-history-of-cinema
                    """)


if __name__ == '__main__':
    main()
