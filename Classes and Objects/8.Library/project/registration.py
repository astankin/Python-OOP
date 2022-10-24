from project.user import User
from project.library import Library


class Registration:

    def add_user(self, user: User, library: Library):
        for library_user in library.user_records:
            if library_user.user_id == user.user_id:
                return f"User with id = {user.user_id} already registered in the library!"
        library.user_records.append(user)

    def remove_user(self, user: User, library: Library):
        for library_user in library.user_records:
            if library_user.user_id == user.user_id:
                library.user_records.remove(user)
        else:
            return "We could not find such user to remove!"

    def change_username(self, user_id: int, new_username: str, library: Library):
        for library_user in library.user_records:
            if library_user.user_id == user_id and library_user.username != new_username:
                library_user.username = new_username
                for username, record in library.rented_books.items():
                    if library_user.name == username:
                        del library.rented_books[username]
                        library.rented_books[new_username] = record
                return f"Username successfully changed to: {new_username} for user id: {library_user.user_id}"
            if library_user.user_id == user_id and library_user.username == new_username:
                return "Please check again the provided username - it should be different than the username used so far!"
        return f"There is no user with id = {user_id}!"
