from collections import defaultdict

def group_anagrams(words):
    anagrams = defaultdict(list)
    
    for word in words:
        sorted_word = ''.join(sorted(word))  # Sort characters to get the key
        anagrams[sorted_word].append(word)
    
    return list(anagrams.values())

# Example usage
words = ["listen", "silent", "enlist", "rat", "tar", "art", "evil", "vile", "live"]
result = group_anagrams(words)

# Print anagrams together
for group in result:
    print(group)