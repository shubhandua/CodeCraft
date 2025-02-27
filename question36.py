def count_palindromic_substrings(s):
    count = 0

    def expand_around_center(left, right):
        nonlocal count
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1

    for i in range(len(s)):
        expand_around_center(i, i)     # Odd-length palindromes
        expand_around_center(i, i + 1) # Even-length palindromes

    return count

# Example Usage
s = "abc"
print("Total Palindromic Substrings:", count_palindromic_substrings(s))
