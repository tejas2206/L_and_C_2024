# Does the provided Book class followed SRP?
# Answer is NO, because of below reasons:
# It handled book-related behavior such as getting the title, author, and page navigation.
# It managed storage responsibilities, like saving the book to a file system.
# It included location management, dealing with physical placement in a library.


# Below is refactored code.
class Book:
    def __init__(self, title, author, pages):
        self._title = title
        self._author = author
        self._pages = pages
        self._current_page = 0

    def get_title(self):
        return self._title

    def get_author(self):
        return self._author

    def turn_page(self):
        if self._current_page < len(self._pages) - 1:
            self._current_page += 1

    def get_current_page(self):
        return self._pages[self._current_page]


class Location:
    def __init__(self, shelf_number, room_number):
        self.shelf_number = shelf_number
        self.room_number = room_number

    def get_location(self):
        return f"Shelf: {self.shelf_number}, Room: {self.room_number}"


class Storage:
    @staticmethod
    def save(book):
        filename = f"/documents/{book.get_title()} - {book.get_author()}"
        with open(filename, "w") as file:
            file.write(str(book.get_current_page()))


class Printer:
    def print_page(self, page):
        raise NotImplementedError


class PlainTextPrinter(Printer):
    def print_page(self, page):
        print(page)


class HtmlPrinter(Printer):
    def print_page(self, page):
        print(f'<div style="single-page">{page}</div>')
