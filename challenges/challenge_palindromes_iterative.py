def is_palindrome_iterative(word):
    if len(word) == 0:
        return False
    wordReversed = word[::-1]
    if word == wordReversed:
        return True
    else:
        return False
