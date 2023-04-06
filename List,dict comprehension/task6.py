# Напишите программу для создания списка, длина которого равна N. 
# После создания списка нужно подсчитать нечетные и четные числа. 
# Если нечетных чисел больше, чем четных, вывод должен быть «Нет», в остальных ключах «Да». 

# 1. Создать список длиной N
# 2. Посчитать количество четных и нечетных чисел
# 3. Вывести результат сравнения

def even_or_odd(nums: list[int]) -> str:
    list_even = [x for x in nums if x % 2 == 0]
    list_odd = [x for x in nums if x % 2 != 0]
    if len(list_even) < len(list_odd):
        return "No"
    else:
        return "Yes"
    

if __name__ == '__main__':
    n = int(input("Enter the amount of numbers: "))
    nums = []

    for i in range(n):
        nums.append(int(input()))
    
    print(even_or_odd(nums))