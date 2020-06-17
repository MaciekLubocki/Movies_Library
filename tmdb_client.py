import requests

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlMWYwMDliNmE5OTYxYTRhMmY0MDQ2YmE3OTU4NjdhNSIsInN1YiI6IjVlZTg4ZmVhNjhiNzY2MDAyM2JhNmRjZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Gasjj-1s35UiWCzTFzH7x0ybmYBDi77vtuHzXsY9kvk"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_poster_url(poster_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/" 
    return f"{base_url}{size}/{poster_path}"

