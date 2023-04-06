# Реализуйте класс «Автомобиль». Необходимо хранить в полях класса: 
# название модели, год выпуска, производителя, объем двигателя, цвет машины, цену. 
# Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.


class Car:
    def __init__(self, model: str, year: int, brand: str, volume: int, color: str, price: int) -> None:
        self.model = model
        self.year = year
        self.brand = brand
        self.volume = volume
        self.color = color
        self.price = price 

    def __repr__(self) -> str:
        return f"Model: {self.model}" \
            f"\nYear: {self.year}" \
            f"\nBrand: {self.brand}" \
            f"\nVolume: {self.volume}" \
            f"\nColor: {self.color}" \
            f"\nPrice: {self.price}"
    
    def get_model(self):
        return self.model

    def set_model(self, new_model):
        self.model = new_model

    def get_year(self):
        return self.year

    def set_year(self, new_year):
        self.year = new_year

    def get_brand(self):
        return self.brand

    def set_brand(self, new_brand):
        self.brand = new_brand
    
    ...

if __name__ == "__main__":

    auto1 = Car('X5', 2022, 'BMW', 65, 'Black', 30_000_000)

    print(auto1)

    print(auto1.get_model())

    auto1.set_model('X6')

    print(auto1.model)
