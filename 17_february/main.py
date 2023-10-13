def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


if __name__ == "__main__":
    string = 'Hello World'
    array = [ord(x) for x in string if x != ' ']
    result = bubble_sort(array)
    string = ''.join([chr(x) for x in result])
    print(string)

    print(''.join(sorted(string, key=lambda x: ord(x))))
