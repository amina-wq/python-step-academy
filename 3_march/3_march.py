def recursive_palindrome(string: str):
    string = string.lower().replace(' ', '')
    if len(string) < 2:
        return True
    if string[0] != string[-1]:
        return False
    return recursive_palindrome(string[1:-1])


def reverse_palindrome(string: str):
    string = string.lower().replace(' ', '')
    return string == string[::-1]


def two_pointers_palindrome(string: str):
    string = string.lower().replace(' ', '')
    left = 0
    right = len(string) - 1

    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1

    return True


def compress_list(nums: list):
    nums.sort()
    ranges = []
    start_range = nums[0]

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1] + 1:
            if start_range == nums[i - 1]:
                ranges.append(str(start_range))
            else:
                ranges.append(f"{start_range}-{nums[i - 1]}")
            start_range = nums[i]

    if start_range == nums[-1]:
        ranges.append(str(start_range))
    else:
        ranges.append(f"{start_range}-{nums[-1]}")

    return ",".join(ranges)


if __name__ == '__main__':
    # Палиндром
    print(recursive_palindrome('А роза упала на лапу Азора'))
    print(reverse_palindrome('А роза упала на лапу Азора'))
    print(two_pointers_palindrome('А роза упала на лапу Азора'))

    # Сжатие диапазонов
    nums = [1, 4, 5, 2, 3, 9, 8, 11, 0]
    result = compress_list(nums)
    print(result)
