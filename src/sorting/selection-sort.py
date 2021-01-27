import sys


def selection_sort(arr):
    for i in range(len(arr)):
        smaller_idx = i
        for j in range(len(arr) - i):
            j += i
            if arr[smaller_idx] > arr[j]:
                smaller_idx = j
            if j == len(arr) - 1:
                swap(arr, i, smaller_idx)


def swap(arr, idx1, idx2):
    aux = arr[idx1]
    arr[idx1] = arr[idx2]
    arr[idx2] = aux


if __name__ == '__main__':
    print("Type a list of numbers separated by space: ")
    arr = list(map(int, input().split()))

    selection_sort(arr)
    print(arr)
