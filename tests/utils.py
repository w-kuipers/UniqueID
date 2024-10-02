def has_upper(string: str):
    result = False
    for char in string:
        if char.isupper():
            result = True
            break

    return result

def has_lower(string: str):
    result = False
    for char in string:
        if char.islower():
            result = True
            break

    return result

def has_number(string: str):
    result = False
    for char in string:
        if char.isnumeric():
            result = True
            break

    return result
