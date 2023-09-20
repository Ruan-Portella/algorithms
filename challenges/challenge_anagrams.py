def is_anagram(first_string, second_string):
    if len(first_string) < 1 and len(second_string) < 1:
        return first_string.lower(), second_string.lower(), False
    first_string = order_string(first_string)
    second_string = order_string(second_string)
    if not first_string == second_string:
        return first_string, second_string, False
    return first_string, second_string, True


def order_string(string):
    aplhabet = 'abcdefghijklmnopqrstuvwxyz'
    string = string.lower()
    ordered_string = ''
    for letter in aplhabet:
        if letter in string:
            ordered_string += letter * string.count(letter)
    return ordered_string
