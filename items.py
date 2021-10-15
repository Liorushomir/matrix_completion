class Items():
    genre_list = ["unknown", "Action", "Adventure", "Animation",
                  "Children's", "Comedy", "Crime", "Documentary", "Drama", "Fantasy",
                  "Film-Noir", "Horror", "Musical", "Mystery", "Romance", "Sci-Fi",
                  "Thriller", "War", "Western"]

    def __init__(self, movie_id, movie_title, release_date, video_release_date,
                 IMDb_URL, genres):
        self.movie_id = movie_id
        self.movie_title = movie_title
        self.release_date = release_date
        self.video_release_date = video_release_date
        self.imdb_url = IMDb_URL
        self.genres = [genre for genre, match in zip(self.genre_list, genres) if match == 1]
