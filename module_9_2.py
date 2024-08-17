first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(el) for el in first_strings if len(el) >= 5]
second_result = [(first, second) for first in first_strings for second in second_strings if len(first) == len(second)]
third_result = {el: len(el) for lst in [first_strings, second_strings] for el in lst if len(el) % 2 == 0}

print(first_result)
print(second_result)
print(third_result)