def merge_sort(arr):
    if len(arr) == 1:
        return arr

    m = int((len(arr)/2))

    l = merge_sort(arr[:m])
    r = merge_sort(arr[m:])

    return merge(l, r)


def merge(l, r):
    j = 0
    k = 0
    merged = []
    for _ in range(len(l + r)):
        if len(l) == j:
            return merged + r[k:]

        if len(r) == k:
            return merged + l[j:]

        if l[j] <= r[k]:
            merged.append(l[j])
            j += 1
        else:
            merged.append(r[k])
            k += 1

    return merged


if __name__ == '__main__':
    print("Digit list of numbers separated by space: ")
    arr = list(map(int, input().split()))

    sorted = merge_sort(arr)

    print(sorted)
