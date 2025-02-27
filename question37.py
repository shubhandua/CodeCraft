def longest_common_prefix(strs):
    if not strs:
        return ""

    # Start with the first string as the initial prefix
    prefix = strs[0]

    # Compare the prefix with each subsequent string
    for s in strs[1:]:
        # Adjust the prefix until it's a prefix of s
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""

    return prefix

# Example usage
input_strings = ["flower", "flow", "flight"]
print(longest_common_prefix(input_strings))  # Output: "fl"
