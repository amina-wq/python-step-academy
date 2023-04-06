# Напишите функцию, которая проверяет является ли число степенью двойки. 
# Если истинно выведите True, иначе False. 

def is_pow2(n):
    if n == 1:
        return True
    elif n > 1:
        return is_pow2(n / 2)
    else:
        return False


if __name__ == "__main__":
    n = int(input("Enter the number: "))
    print(f"Is the {n} - pow of 2? - {is_pow2(n)}")