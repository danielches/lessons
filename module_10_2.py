from threading import Thread
from time import sleep


class Knight(Thread):
    cnt_enemies = 100

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f"{self.name}, на нас напали!")
        cnt_def_enemies = 0
        cnt_days = 0
        while cnt_def_enemies != self.cnt_enemies:
            cnt_days += 1
            if cnt_def_enemies + self.power > self.cnt_enemies:
                cnt_def_enemies += self.cnt_enemies - self.power
            else:
                cnt_def_enemies += self.power
            sleep(1)
            print(
                f"{self.name} сражается {cnt_days} день(дня)..., осталось {self.cnt_enemies - cnt_def_enemies} воинов.\n",
                end='')
        print(f"{self.name} одержал победу спустя {cnt_days} дней(дня)!\n", end='')


# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
print("Все битвы закончились!")
