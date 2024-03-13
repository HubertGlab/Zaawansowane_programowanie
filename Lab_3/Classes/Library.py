class Library:
    def __init__(self, city, street, zip_code, open_hours: str, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f'Biblioteka {self.city} {self.street} {self.zip_code}' \
               f', otwarta {self.open_hours},telefon: {self.phone}'


class Employee:
    def __init__(self, first_name, last_name, hire_date,
                 birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f'{self.first_name} {self.last_name}' \
               f', zatrudniony {self.hire_date},\nur. {self.birth_date} ' \
               f'{self.city} {self.street} {self.zip_code},' \
               f' telefon: {self.phone}'


class Book:
    def __init__(self, library, publication_date,
                 author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f'Autor: {self.author_name} {self.author_surname},' \
               f' opublikowana: {self.publication_date}\n' \
               f'{self.library}, {self.number_of_pages}'


class Order:
    def __init__(self, employee, student, books: list, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        book_details = "\n".join([f"{book}" for book in self.books])
        return f'Zamówienie {self.student}, obsłużone przez:' \
               f' {self.employee} {self.order_date}\nKsiążki:\n{book_details}'



