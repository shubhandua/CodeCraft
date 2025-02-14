from collections import Counter

def are_anagrams(str1, str2):
    return Counter(str1) == Counter(str2)

# Example usage
print(are_anagrams("listen", "silent"))  # True
print(are_anagrams("hello", "world"))    # False
