def is_anagram(first_string, second_string):
    first_string = first_string.lower()
    second_string = second_string.lower()
    if len(first_string) != len(second_string):
        return first_string, second_string, False
    if len(first_string) < 1 and len(second_string) < 1:
        return first_string, second_string, False
    for letter in first_string:
        if letter not in second_string:
            return first_string, second_string, False
    return first_string, second_string, True
