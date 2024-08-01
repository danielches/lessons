numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for number in numbers:
    if number == 1:
        continue
    is_prime = True
    for div in range(2, int(number**0.5) + 1):
        if number % div == 0:
            is_prime = False
            not_primes.append(number)
            break
    if is_prime:
        primes.append(number)
print(primes)
print(not_primes)
