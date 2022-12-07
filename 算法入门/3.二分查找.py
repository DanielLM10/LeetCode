def binary_search(li, val):
    left, right = 0, len(li) - 1
    while left <= right:
        mid = (right - left) // 2 + left
        if li[mid] == val:
            return mid
        elif li[mid] > val:
            right = mid - 1
        else:
            left = mid + 1
    return None


li = [-1, 0, 3, 5, 9, 12]
val = 9
print(binary_search(li, val))
