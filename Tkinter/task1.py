#1. Реализуйте программу без интерфейса, 
# которая будет у пользователя запрашивать два числа 
# и выводить в консоль СУММУ ВСЕХ ЧИСЕЛ МЕЖДУ НИМИ (включительно).

nums = input("Enter two numbers").split()

nums = [int(x) for x in nums]

sum = 0

for i in range(nums[0], nums[1] + 1):
    sum += i 

if __name__ == "__main__":
    print(sum)


