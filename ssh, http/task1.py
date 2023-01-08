#1. Реализуйте программу без интерфейса, 
# которая будет читать файл (data.txt), и записывать в новый файл (new.txt). 
# При этом данные нужно сортировать в порядке убывания и исключить чётные значения.

with open('data.txt') as file:
    nums = [int(x) for x in file.readlines() if int(x) % 2 != 0]

nums.sort()
nums = set(nums)
nums = [str(x) + "\n" for x in nums]

with open('new.txt', 'w') as new_file:
    new_file.writelines(nums)
        
