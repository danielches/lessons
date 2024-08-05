def get_multiplied_digits(number):
    str_number = str(int(number))
    first = int(str_number[0])
    return first * get_multiplied_digits(int(str_number[1:])) if len(str_number) > 1 else first


result = get_multiplied_digits(240203)
print(result)