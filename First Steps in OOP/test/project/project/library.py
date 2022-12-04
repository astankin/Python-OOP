from project.user import User


class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def get_book(self, author, book_name, days_to_return, user: User):
        if book_name in self.books_available[author]:
            user.books.append(book_name)
            self.books_available[author].remove(book_name)
            self.rented_books[user.username] = {book_name: days_to_return}
            return f"{book_name} successfully rented for the next {days_to_return} days!"
        days = 0
        for rented_book in self.rented_books.values():
            if book_name in rented_book:
                days = rented_book[book_name]
        return f'The book "{book_name}" is already rented and will be available in {days} days!'


    def return_book(self, author, book_name, user: User):
        for book in user.books:
            if book == book_name:
                user.books.remove(book)
                self.books_available[author].append(book)
                del self.rented_books[user.username][book_name]
                return
        return f"{user.username} doesn't have this book in his/her records!"
