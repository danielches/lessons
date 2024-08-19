#Лямбда функция
first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda x, y: x == y, first, second))
print(result)


#Замыкание
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        file = open(file_name, 'a')
        for data in data_set:
            file.write(f"{str(data)}\n")
        file.close()

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

#Функтор
from random import choice


class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        res = choice(self.words)
        return res


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
