import streamlit as  st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mysql.connector

path = r"E:/AI and ML/Project imdb/imdb.csv"
df = pd.read_csv(path)

r=st.sidebar.radio('Navigation',['Visualization','Filtering'])

   # Top 10 Movies by Rating and Voting Counts: Identify movies with the highest ratings and significant
   # voting engagement.
if r=='Visualization':
    min_votes = 1000
    df_filtered = df[df["voting_counts"] >= min_votes]
    top_movies = df_filtered.sort_values(by=["ratings", "voting_counts"], ascending=False).head(10)
    st.subheader("Top 10 Movies with High Ratings and Strong Voting")
    st.dataframe(top_movies[["movie_names", "ratings", "voting_counts"]])

    # Genre Distribution: Plot the count of movies for each genre in a bar chart

    st.subheader("Count of movies for each genre")
    data =df['genre'].value_counts()
    fig, ax = plt.subplots()
    data.plot(kind='bar', ax=ax)
    ax.set_xlabel("Genre")
    ax.set_ylabel("Count")
    st.pyplot(fig)

    #Average Duration by Genre: Show the average movie duration per genre in a horizontal bar chart.

    st.subheader("Average movie duration per genre")
    avg_duration = df.groupby('genre')['duration_minutes'].mean()
    fig, ax = plt.subplots(figsize=(8, 6))
    avg_duration.plot(kind='barh', ax=ax)
    ax.set_xlabel("Average Duration (minutes)")
    ax.set_ylabel("Genre")
    st.pyplot(fig)

    #Voting Trends by Genre: Visualize average voting counts across different genres.

    st.subheader("Average voting counts  per genre")
    avg_voting = df.groupby('genre')['voting_counts'].mean()
    fig, ax = plt.subplots(figsize=(8, 6))
    avg_voting.plot(kind='bar', ax=ax)
    ax.set_xlabel("Genre")
    ax.set_ylabel("Average voting counts")
    st.pyplot(fig)

    #Rating Distribution: Display a histogram or boxplot of movie ratings.

    st.subheader("Histogram of movie ratings")
    fig, ax = plt.subplots(figsize=(8, 5))
    df = df['ratings']
    ax.hist(df, bins=10)
    ax.set_xlabel("Rating")
    ax.set_ylabel("Number of Movies")
    st.pyplot(fig)

    #Genre-Based Rating Leaders: Highlight the top-rated movie for each genre in a table.

    path = r"E:/AI and ML/Project imdb/imdb.csv"
    df = pd.read_csv(path)
    st.subheader("Top-rated movie for each genre")
    max_ratings_by_genre = df.groupby('genre')['ratings'].max()
    st.table(max_ratings_by_genre)

    #Most Popular Genres by Voting: Identify genres with the highest total voting counts in a pie chart.

    path = r"E:/AI and ML/Project imdb/imdb.csv"
    df = pd.read_csv(path)
    st.subheader("Genres with the highest total voting counts")
    genre_votes = df.groupby('genre')['voting_counts'].sum()
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(genre_votes, labels=genre_votes.index, autopct='%1.1f%%')
    st.pyplot(fig)

    #Duration Extremes: Use a table or card display to show the shortest and longest movies.

    path = r"E:/AI and ML/Project imdb/imdb.csv"
    df = pd.read_csv(path)
    min_dur = df['duration_minutes'].min()
    max_dur = df['duration_minutes'].max()
    shortest = df[df['duration_minutes'] == min_dur].iloc[0]
    longest = df[df['duration_minutes'] == max_dur].iloc[0]
    extremes_df = pd.DataFrame({
        'Type': ['Shortest Movie', 'Longest Movie'],
        'Movie Name': [shortest['movie_names'], longest['movie_names']],
        'Duration (min)': [min_dur, max_dur]
    })
    st.subheader(" Duration Extremes")
    st.table(extremes_df)

    # Ratings by Genre: Use a heatmap to compare average ratings across genres.

    path = r"E:/AI and ML/Project imdb/imdb.csv"
    df = pd.read_csv(path)
    st.subheader(" Average Ratings by Genre (Heatmap)")
    avg_ratings = df.groupby('genre')['ratings'].mean().to_frame()
    fig, ax = plt.subplots()
    sns.heatmap(avg_ratings, annot=True, cmap='viridis', fmt=".1f", cbar=True, ax=ax)
    st.pyplot(fig)

    #Correlation Analysis: Analyze the relationship between ratings and voting counts using a scatter plot.

    path = r"E:/AI and ML/Project imdb/imdb.csv"
    df = pd.read_csv(path)
    st.subheader("Correlation: Ratings vs Voting Counts")
    fig, ax = plt.subplots()
    ax.scatter(df['voting_counts'], df['ratings'], alpha=0.6, color='green')
    ax.set_xlabel("Voting Count")
    ax.set_ylabel("Ratings")
    st.pyplot(fig)

#Interactive Filtering Functionality


#Connection to mysql server
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database = "imdb"
)
cursor = conn.cursor()
if r=='Filtering':

    st.sidebar.header(" Filter Options")
# Setting up selectbox,slider,number_input and multiselect
    duration_option = st.sidebar.selectbox("Duration (Hours)", ["All", "< 2 hrs", "2-3 hrs", "> 3 hrs"])
    min_rating = st.sidebar.slider("Minimum Rating", 0.0, 10.0, 0.0, step=0.1)
    min_votes = st.sidebar.number_input("Minimum Voting Count", min_value=0, value=0, step=1000)

# Get genres dynamically from database
    cursor.execute("SELECT DISTINCT genre FROM imdb")
    genre_list = [row[0] for row in cursor.fetchall()]
    selected_genres = st.sidebar.multiselect("Select Genre(s)", genre_list)

# Build SQL Query
    query = "SELECT movie_names, genre, ratings, voting_counts, duration_minutes FROM imdb WHERE 1=1"

    if duration_option == "< 2 hrs":
        query += " AND duration_minutes < 120"
    elif duration_option == "2-3 hrs":
        query += " AND duration_minutes BETWEEN 120 AND 180"
    elif duration_option == "> 3 hrs":
        query += " AND duration_minutes > 180"

    query += f" AND ratings >= {min_rating} AND voting_counts >= {min_votes}"

    if selected_genres:
        genres_str = ",".join(f"'{g}'" for g in selected_genres)
        query += f" AND genre IN ({genres_str})"

# Run query and display results
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = ['Movie Name', 'Genre', 'Ratings', 'Voting', 'Duration (Min)']
    df = pd.DataFrame(rows, columns=columns)

    st.subheader("Filtered Movie Results")
    st.write(f"Total Movies Found: {len(df)}")
    st.dataframe(df)

    cursor.close()
    conn.close()

