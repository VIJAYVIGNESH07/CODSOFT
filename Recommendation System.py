from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample dataset of movie titles and related movies
movies_and_related = {
    'The Shawshank Redemption': ['The Green Mile', 'Escape from Alcatraz', 'Cool Hand Luke', 'The Hurricane', 'A Man Escaped', 'The Escapist', 'Papillon', 'Murder in the First', 'The Last Castle', 'Brubaker'],
    'The Godfather': ['Goodfellas', 'Scarface', 'Casino', 'The Departed', 'Once Upon a Time in America', 'Donnie Brasco', 'The Untouchables', 'Carlito\'s Way', 'Road to Perdition', 'American Gangster'],
    'The Dark Knight': ['Batman Begins', 'The Dark Knight Rises', 'Joker', 'Batman: Mask of the Phantasm', 'Watchmen', 'Sin City', 'V for Vendetta', 'The Crow', 'Logan', 'Kick-Ass'],
    'Pulp Fiction': ['Reservoir Dogs', 'Jackie Brown', 'Kill Bill: Volume 1', 'Kill Bill: Volume 2', 'True Romance', 'Snatch', 'Lock, Stock and Two Smoking Barrels', 'Inglourious Basterds', 'The Hateful Eight', 'Natural Born Killers'],
    'Schindler\'s List': ['The Pianist', 'Life is Beautiful', 'The Boy in the Striped Pyjamas', 'The Holocaust', 'The Diary of Anne Frank', 'Sophie\'s Choice', 'Jakob the Liar', 'Europa Europa', 'The Counterfeiters', 'Defiance'],
}

# Function to get related movies for a given movie
def get_related_movies(movie_name):
    return movies_and_related.get(movie_name, [])

# Get user input for movie name
user_movie = input("Enter your movie name: ").strip()

# Retrieve related movies for the entered movie
related_movies = get_related_movies(user_movie)

# Print related movies if found, otherwise display a message
if related_movies:
    print(f"Related movies for '{user_movie}':")
    for i, related_movie in enumerate(related_movies, start=1):
        print(f"{i}. {related_movie}")
else:
    print(f"No related movies found for '{user_movie}'.")
