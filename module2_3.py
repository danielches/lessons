my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
while True:
    if i >= len(my_list) or my_list[i] < 0:
        break
    if my_list[i] == 0:
        i += 1
        continue
    print(my_list[i])
    i += 1
