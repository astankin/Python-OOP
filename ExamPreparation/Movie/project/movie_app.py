from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def check_user_in_collection(self, username):
        return username in [user.username for user in self.users_collection]

    def find_user(self, username):
        for user in self.users_collection:
            if user.username == username:
                return user

    def register_user(self, username: str, age: int):
        if self.check_user_in_collection(username):
            raise Exception("User already exists!")
        new_user = User(username, age)
        self.users_collection.append(new_user)
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):  # to be checked
        user = self.find_user(username)
        if not user:
            raise Exception("This user does not exist!")
        if not username == movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")
        user.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        if not username == movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for key, value in kwargs.items():
            if key == "title":  # setattr(movie, attr, new_value)
                movie.title = value
            elif key == "year":
                movie.year = value
            elif key == "age_restriction":
                movie.age_restriction = value
        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        if movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        user = self.find_user(username)
        user.movies_owned.remove(movie)
        self.movies_collection.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        if movie.owner.username == username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")
        user = self.find_user(username)
        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")
        user.movies_liked.append(movie)
        movie.likes += 1
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = self.find_user(username)
        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")
        movie.likes -= 1
        user.movies_liked.remove(movie)
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if not self.movies_collection:
            return "No movies found."
        else:
            result = []
            for movie in sorted(self.movies_collection, key=lambda x: (-x.year, x.title)):
                result.append(movie.details())
            return '\n'.join(result)

    def __str__(self):
        result = []
        if not self.users_collection:
            result.append("All users: No users.\n")
        else:
            usernames = [user.username for user in self.users_collection]
            result.append(f"All users: {', '.join(usernames)}\n")

        if not self.movies_collection:
            result.append("All movies: No movies.")
        else:
            movies_titles = [movie.title for movie in self.movies_collection]
            result.append(f"All movies: {', '.join(movies_titles)}")
        return ''.join(result)
