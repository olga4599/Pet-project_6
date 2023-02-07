def partition(array, start, end):
    pivot = array[start]
    i = start + 1 #low
    j = end         #high

    while True:
        while i<= j and array[j] >= pivot:
            j = j-1

        while i <= j and array[i] <= pivot:
            i = i+1

        if i<= j:
            array[i], array[j] = array[j], array[i]
        else:
            break
    array[start], array[j] = array[j], array[start]
    return j

def quick_sort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)

def binary_search(array, x, left, right):
    try:
        if left > right:
            return False

        mid = (right + left) // 2
        if array[mid] == x:
            return mid
        elif x < array[mid]:
            return binary_search(array, x, left, mid - 2)
        else:
            return binary_search(array, x, mid + 1, right)
    except IndexError:
        return "The number is out of range. Please, enter a lower number"

array = [2, 3, 6, 5, 4, 7]
quick_sort(array, 0, len(array) - 1)
print(array)

num = int(input("Enter a number: "))
print(binary_search(array, num, 0, 10))

