def reverse_word(word):
    stack = []
    rev_word = ""
    for letter in word:
        stack.append(letter)
    while stack:
        rev_word += stack.pop()

    return rev_word


word = "Hello"

reversed_word = reverse_word(word)
print(reversed_word)