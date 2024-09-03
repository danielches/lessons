from threading import Thread, Lock
from random import randint
from time import sleep


class Bank:
    def __init__(self, balance=0):
        self.balance = balance
        self.lock = Lock()

    def deposit(self):
        for _ in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            cur_sum = randint(50, 500)
            self.balance += cur_sum
            print(f"Пополнение: {cur_sum}. Баланс: {self.balance}.\n", end='')
            sleep(0.001)

    def take(self):
        for _ in range(100):
            cur_sum = randint(50, 500)
            print(f"Запрос на {cur_sum}\n", end='')
            if cur_sum <= self.balance:
                self.balance -= cur_sum
                print(f"Снятие: {cur_sum}. Баланс: {self.balance}\n", end='')
            else:
                print(f"Запрос отклонён, недостаточно средств\n", end='')
                self.lock.acquire()


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')