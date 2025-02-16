def longest_unique_substring(s):
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        # If character is already in set, shrink window from the left
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        # Add the new character and update max length
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length

# Example usage
s = "abcabcbb"
print(longest_unique_substring(s))  # Output: 3 (substring "abc")
