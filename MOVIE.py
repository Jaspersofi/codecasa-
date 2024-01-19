# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Defining file paths
movies_path = r"C:\Users\Work\Downloads\MOVIE RECOMENDATION\movies.csv"
ratings_path = r"C:\Users\Work\Downloads\MOVIE RECOMENDATION\ratings.csv"

# Reading data from CSV files
movies = pd.read_csv(movies_path, sep="::", engine="python", header=None, names=["MovieID", "Title", "Genres"])
ratings = pd.read_csv(ratings_path, sep="::", engine="python", header=None, names=["UserID", "MovieID", "Rating", "Timestamp"])

# Merging dataframes
movie_ratings = pd.merge(ratings, movies, on="MovieID")

# Function to get genre recommendations
def get_genre_recommendations(genre):
    # Filtering movies by genre
    genre_movies = movies[movies["Genres"].str.contains(genre, case=False, na=False)]
    
    # Merging ratings with genre-filtered movies
    genre_movie_ratings = pd.merge(ratings, genre_movies, on="MovieID")
    
    # Calculating mean ratings and sorting
    genre_ratings_grouped = genre_movie_ratings.groupby("Title")["Rating"].mean().reset_index()
    genre_ratings_sorted = genre_ratings_grouped.sort_values(by="Rating", ascending=False)
    
    # Getting top recommendations
    genre_recommendations = genre_ratings_sorted.head(10)
    return genre_recommendations

# Getting user input
user_genre = input("Enter a genre: ")

# Generating recommendations based on user input
genre_recommendations = get_genre_recommendations(user_genre)

# Displaying recommendations and plotting graph
if not genre_recommendations.empty:
    print(f"\nTop {user_genre} Movie Recommendations:")
    print(genre_recommendations)
    
    # Plotting graph
    plt.figure(figsize=(10, 6))
    plt.barh(genre_recommendations["Title"], genre_recommendations["Rating"], color='skyblue')
    plt.xlabel('Average Rating')
    plt.title(f'Top {user_genre} Movie Recommendations Based on Ratings')
    plt.show()
else:
    print(f"No movies found for the genre: {user_genre}")
