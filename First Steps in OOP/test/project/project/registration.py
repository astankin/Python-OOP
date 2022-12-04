from project.library import Library
from project.user import User


class Registration:

    def add_user(self, user: User, library: Library):
        if user not in library.user_records:
            library.user_records.append(user)
            return
        return f"User with id = {user.user_id} already registered in the library!"

    def remove_user(self, user: User, library: Library):
        if user not in library.user_records:
            return "We could not find such user to remove!"
        library.user_records.remove(user)

    def change_username(self, user_id, new_username, library: Library):
        for user in library.user_records:
            if user.user_id == user_id and user.username != new_username:
                if user.username in library.rented_books:
                    rented_books = library.rented_books[user.username]
                    del library.rented_books[user.username]
                    library.rented_books[new_username] = rented_books
                user.username = new_username
                return f"Username successfully changed to: {new_username} for user id: {user_id}"
            if user.user_id == user_id and user.username == new_username:
                return f"Please check again the provided username - it should be different than the username used so far!"
        return f"There is no user with id = {user_id}!"
