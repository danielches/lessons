import math
from typing import Tuple, NoReturn, List


class __Figure:
    sides_count = 0

    def __init__(self, color: Tuple[int, int, int], *sides: int | float, filled: bool = False) -> NoReturn:
        if self.__is_valid_sides(sides):
            self.__sides = sides
        else:
            self.__sides = (1,) * self.sides_count

        self.__color = color
        self.filled = filled

    def get_color(self) -> List[int]:
        return list(self.__color)

    def __is_valid_color(self, r: int, g: int, b: int) -> bool:
        return 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255

    def set_color(self, r: int, g: int, b: int) -> NoReturn:
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def get_sides(self) -> List[int | float]:
        return list(self.__sides)

    def __is_valid_sides(self, sides: Tuple[int | float, ...]) -> bool:
        return len(sides) == self.sides_count and all([x > 0 for x in sides])

    def set_sides(self, *new_sides: int | float) -> NoReturn:
        if self.__is_valid_sides(new_sides):
            self.__sides = new_sides

    def __len__(self) -> NoReturn:
        return sum(self.__sides)


class Circle(__Figure):
    sides_count = 1

    def __init__(self, color: Tuple[int, int, int], *sides: int | float, filled: bool = False) -> NoReturn:
        super().__init__(color, *sides, filled=filled)
        self.__radius = self.get_sides()[0] / (2 * math.pi)

    def get_square(self) -> float:
        return math.pi * self.__radius ** 2


class Triangle(__Figure):
    sides_count = 3

    def __init__(self, color: Tuple[int, int, int], *sides: int | float, filled: bool = False) -> NoReturn:
        super().__init__(color, *sides, filled=filled)

    def __is_valid_sides(self, sides: Tuple[int | float, ...]) -> bool:
        return len(sides) == self.sides_count and all([x > 0 for x in sides]) and \
            sides[0] + sides[1] > sides[2] and sides[0] + sides[2] > sides[1] and sides[1] + sides[2] > sides[0]

    def get_square(self) -> float:
        p = sum(self.get_sides()) / 2
        return math.sqrt(p * (p - self.get_sides()[0]) * (p - self.get_sides()[1]) * (p - self.get_sides()[2]))


class Cube(__Figure):
    sides_count = 12

    def __init__(self, color: Tuple[int, int, int], *sides: int | float, filled: bool = False) -> NoReturn:
        if self.__is_valid_sides(sides):
            correct_sides = (sides[0],) * self.sides_count
        else:
            correct_sides = (1,) * self.sides_count
        super().__init__(color, *correct_sides, filled=filled)

    def __is_valid_sides(self, sides: Tuple[int | float, ...]) -> bool:
        return len(sides) == 1 and sides[0] > 0

    def get_volume(self) -> int | float:
        return self.get_sides()[0] ** 3


# Код для проверки:
triangle1 = Triangle((222, 35, 130), 6, 3, 6)
circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
