# IMDB-2024-Data-Scraping-and-Visualizations

This project extracts, processes, visualizes, and interactively filters movie data from IMDb using **Selenium**, **Pandas**, **Streamlit**, and **MySQL**.

---

##  Project Structure

### `data_extraction.ipynb`
An ipynb file that uses Selenium to scrape data from (https://www.imdb.com/search/title/?title_type=feature&release_date=2024-01-01,2024-12-31).

**Extracted attributes:**
- Movie Title
- Genre
- Ratings
- Voting Counts (converted to integer)
- Duration (converted to minutes)

---

### CSV Files by Genre
Contains cleaned and labeled datasets for each genre:
- `adventure.csv`
- `animation.csv`
- `biography.csv`
- `history.csv`
- `sport.csv`

Each file includes:
- `movie_names`, `ratings`, `voting_counts`, `duration_minutes`, `genre`

---

### `imdb.csv`
A merged dataset of all genre-specific files using `pd.concat()` and cleaned with pandas.

---

### `visualization_and_filtering.py`
A **Streamlit** app with two main functionalities:
- **Visualization**: Displays charts and statistics
- **Filtering**: Interactive filters to search movies by genre, rating, duration, and vote count using MySQL queries

---

##  Features

### Visualization Tab
- Top 10 Movies with High Ratings & Voting
- Genre Distribution (Bar Chart)
- Average Duration per Genre (Horizontal Bar)
- Average Votes per Genre
- Rating Histogram
- Top-rated Movie per Genre (Table)
- Most Popular Genres (Pie Chart)
- Shortest & Longest Movies (Table)
- Average Ratings by Genre (Heatmap)
- Correlation: Ratings vs Votes (Scatter Plot)

### Filtering Tab
Filter movies based on:
- **Duration**: `< 2 hrs`, `2–3 hrs`, `> 3 hrs`
- **Minimum Rating** (slider)
- **Minimum Vote Count** (numeric input)
- **Genre** (multi-select from database)

---

## Requirements
- Python
- Selenium
- Pandas
- Streamlit
- MySQL (for advanced filtering)
