def merge(left, right):
    sorted_arr = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    return sorted_arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)
def has_length(arr, target_p):
    n = len(arr)
    if n < 3:
        return False
    
    arr = merge_sort(arr)
    
    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            val1 = arr[i]
            val2 = arr[left]
            val3 = arr[right]
            current_sum = val1 + val2 + val3

            if current_sum == target_p:
                if val1 != val2 and val2 != val3 and val1 != val3:
                    return True
                else:
                    left += 1
                    right -= 1
                    
            elif current_sum < target_p:
                left += 1
            else:
                right -= 1
    return False
            