# В Институте биоинформатики между информатиками и биологами устраивается соревнование. 
# Победителям соревнования достанется большой и вкусный пирог. В команде биологов a человек, а в команде информатиков — b человек.
# Нужно заранее разрезать пирог таким образом, чтобы можно было раздать кусочки пирога любой команде, выигравшей соревнование, 
# при этом каждому участнику этой команды должно достаться одинаковое число кусочков пирога. 
# И так как не хочется резать пирог на слишком мелкие кусочки, нужно найти минимальное подходящее число.
# Напишите программу, которая помогает найти это число.
# Программа должна считывать размеры команд (два положительных целых числа aa и b, каждое число вводится на отдельной строке) 
# и выводить наименьшее число d, которое делится на оба этих числа без остатка.

# Решение через list comprehensions
# a = int(input("Enter the number of people in the team a: "))
# b = int(input("Enter the number of people in the team b: "))
# 
# divisors = [x for x in range(1, a * b + 1) if x % a == 0 and x % b == 0]
# 
# lcm = min(divisors)
# 
# if __name__ == '__main__':
#     print(f'The least common multiple is: {lcm}')


# Второе решение 
def gcd(a, b):
    temp = 0
    while b != 0:
        temp = a % b 
        a = b
        b = temp
    return a 
    

def lcm(a, b):
    lcm = a * b / gcd(a, b)
    return int(lcm)

if __name__ == "__main__":
    a = int(input("Enter the number of people in the team a: "))
    b = int(input("Enter the number of people in the team b: "))
    print(f'The least common multiple is: {lcm(a, b)}')