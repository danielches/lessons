def calculate_structure_sum(obj):
    if not obj:
        return 0
    res = 0
    for el in obj:
        if isinstance(el, int):
            res += el
        elif isinstance(el, str):
            res += len(el)
        elif isinstance(el, list) or isinstance(el, tuple) or isinstance(el, set):
            res += calculate_structure_sum(el)
        elif isinstance(el, dict):
            res += calculate_structure_sum(el.items())
    return res


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
print(calculate_structure_sum(data_structure))