n = int(input("Введите число от 3 до 20\n"))
while (n < 3 or n > 20):
    n = int(input("Введите число от 3 до 20\n"))
n = 3
while n < 21:
    print(f"{n} = ", end="")
    for first in range(1, n):
        for second in range(first+1, n):
            if n % (first + second) == 0:
                print(f"{first}{second}", end="")
    print()
    n += 1