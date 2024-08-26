def is_prime(func):
    def wrapper(*args):
        num = func(*args)
        num_is_prime = True
        for div in range(2, int(num ** 0.5) + 1):
            if num % div == 0:
                num_is_prime = False
                break
        if num_is_prime:
            print("Простое")
        else:
            print("Составное")
        return num

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
