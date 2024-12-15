import os
import requests
from dotenv import load_dotenv

# Load the API key from .env
load_dotenv()
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

# Base URL for TMDB API
BASE_URL = "https://api.themoviedb.org/3"

def get_recommendations(movie_id):
    """Get movie recommendations based on a movie ID."""
    url = f"{BASE_URL}/movie/{movie_id}/recommendations"
    params = {"api_key": TMDB_API_KEY}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code, response.text)
        return None

def search_movie(movie_name):
    """Search for a movie by name."""
    url = f"{BASE_URL}/search/movie"
    params = {
        "api_key": TMDB_API_KEY,
        "query": movie_name
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code, response.text)
        return None

# Test the function
if __name__ == "__main__":
    movie_name = input("Enter a movie name: ")
    search_result = search_movie(movie_name)
    if search_result and search_result['results']:
        first_movie = search_result['results'][0]
        print(f"Top match: {first_movie['title']} ({first_movie['release_date']})")
        recommendations = get_recommendations(first_movie['id'])
        if recommendations:
            print("\nRecommendations:")
            for movie in recommendations['results'][:5]:  # Show top 5 recommendations
                print(f"- {movie['title']} ({movie['release_date']})")
    else:
        print("No movie found!")

