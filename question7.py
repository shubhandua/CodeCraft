def find_min(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:  
            left = mid + 1  # Minimum is in the right half
        else:
            right = mid  # Minimum is in the left half or at mid

    return nums[left]

# Example Usage
nums = [3, 4, 5, 1, 2]
print(find_min(nums))  # Output: 1
