# IMDB-2024-Data-Scraping-and-Visualizations
This project extracts, processes, visualizes, and interactively filters movie data from IMDb using Selenium, Pandas, Streamlit, and MySQL.
Project Structure
1. data_extraction.ipynb
•	An ipynb file that uses Selenium to scrape data from the https://www.imdb.com/search/title/?title_type=feature&release_date=2024-01-01,2024-12-31
•	Extracted attributes:
o	Movie Title
o	Genre
o	Ratings
o	Voting Counts (converted to integer)
o	Duration (converted to minutes)
2. CSV Files by Genre
•	Contains cleaned and labeled datasets for each genre:
o	adventure.csv
o	animation.csv
o	biography.csv
o	history.csv
o	sport.csv
•	Each file contains:
o	movie_names, ratings, voting_counts, duration_minutes, and genre.
3. imdb.csv
•	A merged dataset of all genre-specific files using pd.concat() and cleaned using pandas.
4. visualization_and_filtering.py
•	A Streamlit app with two main functionalities:
o	Visualization: Displays charts and statistics.
o	Filtering: Interactive filters to search movies by genre, rating, duration, and vote count using a MySQL query.
________________________________________
 Features
 Visualization Tab
•	Top 10 Movies with High Ratings & Voting
•	Genre Distribution (Bar chart)
•	Average Duration per Genre (Horizontal Bar)
•	Average Votes per Genre
•	Rating Histogram
•	Top-rated Movie per Genre (Table)
•	Most Popular Genres (Pie Chart)
•	Shortest & Longest Movie (Table)
•	Average Ratings by Genre (Heatmap)
•	Correlation: Ratings vs Votes (Scatter Plot)
Filtering Tab
•	Filter movies based on:
o	Duration (< 2 hrs, 2–3 hrs, > 3 hrs)
o	Minimum Rating (slider)
o	Minimum Vote Count (numeric input)
o	Genre (multi-select from database)
________________________________________
 Tech Stack
•	Python
•	Selenium – Web scraping
•	Pandas & NumPy – Data processing
•	MySQL – Data storage & filtering
•	Streamlit – Web app for visualization and filters
•	Matplotlib & Seaborn – Charts and plots

