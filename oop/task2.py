# Реализуйте класс «Книга». Необходимо хранить в полях класса: 
# название книги, год выпуска, издателя, жанр, автора, цену. 
# Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.

class Book:
    def __init__(self, name: str, year: int, publisher: str, genre: str, author: str, price: int) -> None:
        self.name = name 
        self.year = year 
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def __repr__(self) -> str:
        return f"Name: {self.name}" \
        f"\nYear: {self.year}" \
        f"\nPublisher: {self.publisher}" \
        f"\nGenre: {self.genre}" \
        f"\nAuthor: {self.author}" \
        f"\nPrice: {self.price}"
    
    def get_name(self):
        return self.name
    
    def set_name(self, new_name):
        self.name = new_name

    def get_year(self):
        return self.year
    
    def set_year(self, new_year):
        self.year = new_year
    
    def get_publisher(self):
        return self.publisher
    
    def set_year(self, new_publisher):
        self.publisher = new_publisher


if __name__ == "__main__":
    book1 = Book('Anne', 2006, 'Ala', 'romance', 'Brook', 2500)

    print(book1)

    print(book1.get_name())

    book1.set_name('Windy')
    print(book1.name)