def product_except_self(nums):
    n = len(nums)
    result = [1] * n
    
    # Compute prefix products
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    # Compute suffix products and multiply with prefix products
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result

# Example Usage
nums = [1, 2, 3, 4]
print(product_except_self(nums))  # Output: [24, 12, 8, 6]
