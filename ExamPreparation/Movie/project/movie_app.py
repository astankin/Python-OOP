from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def check_user_in_collection(self, username):
        return username in [user.username for user in self.users_collection]

    def register_user(self, username: str, age: int):
        if self.check_user_in_collection(username):
            raise Exception("User already exists!")
        new_user = User(username, age)
        self.users_collection.append(new_user)
        return f"{username} registered successfully."




