def all_variants(text):
    step = 1
    while step <= len(text):
        for i in range(len(text) - step + 1):
            yield text[i:i+step]
        step += 1


a = all_variants("abc")
for i in a:
    print(i)
