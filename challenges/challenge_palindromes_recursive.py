def is_palindrome_recursive(word, low_index, high_index):
    if (len(word) == 0):
        return False
    if (low_index == len(word)):
        return False
    if (high_index == 0):
        return True
    return verify_palindromo(word, low_index, high_index)


def verify_palindromo(word, low_index, high_index):
    if (low_index == high_index):
        return True
    if (word[low_index] != word[high_index]):
        return False
    if (low_index < high_index + 1):
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    return True
