#1st program
print(9**0.5*5)

#2st program
print(9.99 > 9.98 and 1000 != 1000.1)

#3st program
a, b = 1234, 5678
print(a%1000//10 + b%1000//10)

#4st program
from decimal import Decimal
a, b = 13.42, 42.13
print(int(a) == int(b % 1 * 100) or int(b) == int(a % 1 * 100))