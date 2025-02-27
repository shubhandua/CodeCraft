def is_sentence_palindrome(sentence):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = ''.join(char.lower() for char in sentence if char.isalnum())
    # Check if the cleaned sentence is equal to its reverse
    return cleaned == cleaned[::-1]

# Example usage
sentence = "A man, a plan, a canal, Panama!"
if is_sentence_palindrome(sentence):
    print("The sentence is a palindrome.")
else:
    print("The sentence is not a palindrome.")
