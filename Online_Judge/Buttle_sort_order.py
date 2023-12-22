def selection_sort(arr):
    swaps = []
    n = len(arr)
    
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps.append((arr[i], arr[min_index]))

    return swaps

n, k = map(int, input().split())
arr = list(map(int, input().split))

swaps = selection_sort(arr)

if k > len(swaps):
    print("K exceeds the number of swaps.")
else:
    kth_swap = swaps[k - 1]
    print(*sorted(kth_swap))
