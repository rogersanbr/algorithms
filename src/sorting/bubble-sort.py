def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[i] < arr[j]:
                aux = arr[i]
                arr[i] = arr[j]
                arr[j] = aux


if __name__ == '__main__':
    print("Type a list of numbers separated by space: ")
    arr = list(map(int, input().split()))

    bubble_sort(arr)
    print(arr)
