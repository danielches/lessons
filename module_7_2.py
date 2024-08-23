def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    line = 0
    strings_positions = dict()
    for string in strings:
        line += 1
        pos = file.tell()
        strings_positions[(line, pos)] = string
        file.write(f"{string}\n")
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)