def has_pair_with_sum(arr, target_sum):
    seen = set()
    for num in arr:
        complement = target_sum - num
        if complement in seen:
            return True
        seen.add(num)
    return False

# Example Usage
arr = [1, 4, 7, 12, 15]
target_sum = 19
print(has_pair_with_sum(arr, target_sum))  # Output: True
