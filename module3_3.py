def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(b=25)
print_params(c=[1, 2, 3])
print_params()

values_list = ['1', 1, [1.0, 1.0]]
values_dict = {'a': '2', 'b': 2, 'c': [2.0, 2.0]}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['3', 3]
print_params(*values_list_2, 42)
