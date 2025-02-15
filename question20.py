from collections import Counter

def smallest_window(s, t):
    if not s or not t:
        return ""

    char_count = Counter(t)  # Count of characters in t
    required = len(char_count)  # Unique characters in t
    left, right = 0, 0
    formed = 0  # Number of characters that match the required frequency
    window_counts = {}
    
    min_len = float("inf")
    min_window = ""

    while right < len(s):
        # Add current character to window
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1

        # If this character matches the required frequency in t, increase `formed`
        if char in char_count and window_counts[char] == char_count[char]:
            formed += 1

        # Try to contract the window if all required characters are present
        while left <= right and formed == required:
            char = s[left]

            # Update minimum window
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_window = s[left:right + 1]

            # Remove leftmost character from window
            window_counts[char] -= 1
            if char in char_count and window_counts[char] < char_count[char]:
                formed -= 1

            left += 1  # Shrink the window

        right += 1  # Expand the window

    return min_window if min_len != float("inf") else ""

# Example usage
s = "ADOBECODEBANC"
t = "ABC"
print(smallest_window(s, t))  # Output: "BANC"
