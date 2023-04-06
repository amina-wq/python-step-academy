# Реализовать декоратор, который превращает в функции на входе, текстовые строки в нижний регистр

def lower(func):
    def inner(*args, **kwargs):
        new_args = []
        new_kwargs = {}

        for i in args:
            if isinstance(i, str):
                new_args.append(i.lower())
            else:
                new_args.append(i)

        for key, value in kwargs.items():
            if isinstance(value, str):
                new_kwargs[key] = value.lower()
            else:
                new_kwargs[key] = value        

        func(*new_args, **new_kwargs)
    return inner        

# a.lower() type(a) <class str> 
# isinstance(a, str)

@lower
def print_info(name: str, surname: str, age: int):
    print(f'Hello, I`m {surname} {name}. I`m {age} years old')

print_info('Stas', 'Zaichikov', 22)
print_info('Stas', age = 22, surname = 'Zaichikov')