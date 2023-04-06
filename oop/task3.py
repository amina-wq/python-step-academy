# Реализуйте класс «Стадион». Необходимо хранить в полях класса: 
# название стадиона, дату открытия, страну, город, вместимость. 
# Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.
from datetime import datetime

class Stadium:
    def __init__(self, name: str, opening_date: str, country: str, city: str, capacity: int) -> None:
        self.name = name
        self.opening_date = datetime.strptime(opening_date, "%d.%m.%Y")
        self.country = country
        self.city = city
        self.capacity = capacity

    def __repr__(self) -> str:
        return f"Name: {self.name}" \
        f"\nOpening date: {datetime.strftime(self.opening_date, '%d.%m.%Y')}" \
        f"\nCountry: {self.country}" \
        f"\nCity: {self.city}" \
        f"\nCapacity: {self.capacity}"

    def get_name(self):
        return self.name
    
    def set_name(self, new_name):
        self.name = new_name

    def get_opening_date(self):
        return self.opening_date
    
    def set_opening_date(self, new_opening_date):
        self.opening_date = datetime.strptime(new_opening_date, "%d.%m.%Y")

    def get_capacity(self):
        return self.capacity
    
    def set_capacity(self, new_capacity):
        self.capacity = new_capacity


if __name__ == "__main__":
    stadium1 = Stadium('Astana Arena', '03.07.2009', 'Kazakhstan', 'Astana', 30200)

    print(stadium1)

    stadium1.set_opening_date('04.07.2009')

    print(stadium1.get_opening_date())