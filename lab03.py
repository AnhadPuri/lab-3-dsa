#function 1
def factorial(number):
    if (number == 0):
        return 1
    return (number * factorial(number-1))
#function 2
def linear_search(list, key, index=0):
    len_of_list = (len(list) - 1)
    if (list[index] == key):
        return index
    if ((index == len_of_list) and (list[index] != key)):
        return -1
    return linear_search(list, key, index+1)
#function 3
def binary_search(arr, key):
    def binary_search_recursive(arr, key, left, right):
        if left > right:
            return -1  # Key not found

        mid = (left + right) // 2

        if arr[mid] == key:
            return mid  # Key found at index mid
        elif arr[mid] < key:
            return binary_search_recursive(arr, key, mid + 1, right)
        else:
            return binary_search_recursive(arr, key, left, mid - 1)

    return binary_search_recursive(arr, key, 0, len(arr) - 1)
