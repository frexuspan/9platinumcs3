class Publication:
    def __init__(self, title, author):
        self.__title = title # Private attribute
        self.__author = author # Private attribute

    def get_title(self):
        return self.__title # Returns the title of the publication

    def get_author(self):
        return self.__author # Returns the author of the publication

    def set_title(self, title):
        self.__title = title # Sets the title of the publication

    def set_author(self, author):
        self.__author = author # Sets the author of the publication

    def display_info(self):
        return f"Title: {self.__title} \nAuthor: {self.__author}" # Returns the title and author of the publication

class Book(Publication):
    def __init__(self, title, author, pages):
        self.__pages = pages # Private attribute
        super().__init__(title, author)  # Calls the constructor of the parent class Publication

    def get_number_of_pages(self):
        return self.__pages # Returns the number of pages in the book

    def set_number_of_pages(self, pages):
        self.__pages = pages # Sets the number of pages in the book

class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        self.__issue_number = issue_number # Private attribute
        super().__init__(title, author)  # Calls the constructor of the parent class Publication

    def get_issue_number(self):
        return self.__issue_number # Returns the issue number of the magazine

    def set_issue_number(self, issue_number):
        self.__issue_number = issue_number # Sets the issue number of the magazine

pub1 = Publication("Journal of Experimental Psychology", "Ratchiff R. & Van Dongen H.")
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
mag1 = Magazine("National Geographic", "Various Authors", 202)

print("Public Information:")
print(pub1.display_info())  # Output: Title: Journal of Experimental Psychology \nAuthor: Ratchiff R. & Van Dongen H.

print("\nBook Information:")
print("Number of pages must be positive.")
print(book1.display_info())  # Output: Title: The Hobbit \nAuthor: J.R.R. Tolkien
print(f"Number of Pages: {book1.get_number_of_pages()}")

print("\nMagazine Information:")
print(mag1.display_info())  # Output: Title: National Geographic \nAuthor: Various Authors
print(f"Issue Number: {mag1.get_issue_number()}")