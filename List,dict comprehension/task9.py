# Написать рекурсивную функцию, которая по заданному целому числу возвращает n-e число Фибоначчи. 
# Ряд Фибоначчи  0, 1, 1, 2, 3, 5, 8, 13,…… 

def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n - 1) + fibonacci(n - 2)
    else:
        raise ValueError("Number must be positive")


if __name__ == "__main__":
    n = int(input("Enter index of fibonacci number: "))
    print(f"{n}-ое число Фибоначчи: {fibonacci(n)}")