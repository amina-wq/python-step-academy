# По данному целому числу N распечатайте все квадраты натуральных чисел, не превосходящие N, в порядке возрастания.

def squares_until_n(n: int) -> list[int]: 
    return [x**2 for x in range(1, int(n**0.5) + 1)]
    

if __name__ == '__main__':
    n = int(input("Enter the number: "))
    print(*squares_until_n(n))