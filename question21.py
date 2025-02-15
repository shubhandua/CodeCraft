from collections import Counter

def character_replacement(s, k):
    left = 0
    max_freq = 0  # Most frequent character count in the window
    char_count = Counter()
    max_length = 0

    for right in range(len(s)):
        char_count[s[right]] += 1
        max_freq = max(max_freq, char_count[s[right]])  # Update max frequency

        # Window size - max frequency character count > k means invalid
        while (right - left + 1) - max_freq > k:
            char_count[s[left]] -= 1  # Remove left character
            left += 1  # Shrink the window
        
        max_length = max(max_length, right - left + 1)  # Update max length

    return max_length

# Example usage
s = "AABABBA"
k = 1
print(character_replacement(s, k))  # Output: 4
