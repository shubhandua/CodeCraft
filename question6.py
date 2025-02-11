def max_product(nums):
    max_product = nums[0]
    min_product = nums[0]
    result = nums[0]

    for num in nums[1:]:
        if num < 0:
            max_product, min_product = min_product, max_product  # Swap if negative
        
        max_product = max(num, max_product * num)
        min_product = min(num, min_product * num)

        result = max(result, max_product)

    return result

# Example Usage
nums = [2, 3, -2, 4]
print(max_product(nums))  # Output: 6 (Subarray: [2,3])
