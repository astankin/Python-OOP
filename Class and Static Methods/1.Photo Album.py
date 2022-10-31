from math import ceil


class PhotoAlbum:
    MAX_PHOTOS_PER_PAGE = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(ceil(photos_count / PhotoAlbum.MAX_PHOTOS_PER_PAGE))

    def add_photo(self, label: str):
        for i in range(self.pages):
            if len(self.photos[i]) < PhotoAlbum.MAX_PHOTOS_PER_PAGE:
                self.photos[i].append(label)
                return f"{label} photo added successfully on page {i + 1} slot {self.photos[i].index(label) + 1}"
        return "No more free slots"

    def display(self):
        delimiter = "-" * 11 + "\n"
        result = delimiter
        for row in self.photos:
            result += ' '.join(["[]" for _ in row]) + '\n'
            result += delimiter
        return result.strip()


album = PhotoAlbum(3)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
