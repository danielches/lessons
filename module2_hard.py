def resh(n):
    result = ""
    for first in range(1, n):
        for second in range(first + 1, n):
            if n % (first + second) == 0:
                result += f"{first}{second}"
    return result


n = int(input("Введите число от 3 до 20\n"))
while n < 3 or n > 20:
    n = int(input("Введите число от 3 до 20\n"))

print(resh(n))
