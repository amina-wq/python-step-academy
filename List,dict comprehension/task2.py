# По данному натуральном n вычислите сумму 1!+2!+3!+...+n!1!+2!+3!+...+n!. 
# В решении этой задачи можно использовать только один цикл. 
# Пользоваться математической библиотекой math в этой задаче запрещено.


def summary(n):
    factorial = 1
    sum = 0
    while n > 1:
        factorial *= n
        n -= 1
        sum += factorial
    return sum

if __name__ == '__main__':
    n = int(input("Enter the number: "))
    print(f'1!+2!+3!+...+n! = {summary(n)}')