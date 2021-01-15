def binary_search(arr, x, left=-1, right=-1):
    if left == -1:
        left = 0

    if right == -1:
        right = len(arr) - 1

    if right >= left:
        mid = left + (right - left) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, x, left, mid - 1)
        else:
            return binary_search(arr, x, mid + 1, right)
    else:
        return -1


aList = [2, 56, 8, 443, 61, 56, 61, 62, 761]

aList.sort()

print(binary_search(aList, 761))
