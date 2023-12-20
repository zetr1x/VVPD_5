"""Практическая работа по ВВПД №4"""
from random import randint


def generate_matrix(height: int, width: int) -> list:
    """
    Функция генерирует матрицу по заданным параметрам

    Args:
        height: высота матрицы
        width: ширина матрицы

    Returns:
        Матрица(height, width)
    """
    return [[randint(0, 255) for _ in range(width)] for _ in range(height)]


def integral_view(image: list) -> list:
    """
    Функция расчитывает матрицу интегрального представления изображения

    Args:
        image: матрица пикселей изображения

    Returns:
        integral_image: интегральное представление изображения
    """
    height = len(image)
    width = len(image[0])
    integral_image = [[0] * width for _ in range(height)]
    for x in range(width):
        for y in range(height):
            value_1 = image[y][x]
            value_2 = integral_image[y - 1][x - 1] if y > 0 and x > 0 else 0
            value_3 = integral_image[y][x - 1] if x > 0 else 0
            value_4 = integral_image[y - 1][x] if y > 0 else 0
            integral_image[y][x] = value_1 + value_4 + value_3 - value_2
    return integral_image


def rect_sum(integral_image: list, x1: int, y1: int, x2: int, y2: int) -> int:
    """
    Функция находит сумму пикселей произвольного прямоугольника

    Args:
        integral_image: интегральное представление матрицы
        x1: x координата левой верхней точки прямоугольника
        y1: y координата левой нижней точки прямоугольника
        x2: x координата правой верхней точки прямоугольника
        y2: y координата правой нижней точки точки прямоугольника

    Returns:
        Сумма пикселей произвольного прямоугольника
    """
    rect_a = image[y1 - 1][x1 - 1] if y1 > 0 and x1 > 0 else 0
    rect_b = image[y1 - 1][x2] if y1 > 0 else 0
    rect_c = image[y2][x2]
    rect_d = image[y2][x1 - 1] if x1 > 0 else 0
    return rect_a + rect_c - rect_b - rect_d


image = [
    [32, 39, 2, 20, 8, 13, 2, 5, 3],
    [15, 14, 11, 12, 13, 14, 5, 20, 8],
    [7, 14, 1, 0, 14, 6, 5, 13, 8],
    [5, 13, 10, 13, 8, 1, 12, 20, 1],
    [0, 2, 12, 20, 15, 7, 19, 30, 48],
    [23, 54, 11, 10, 76, 30, 44, 11, 22],
    [11, 25, 77, 22, 15, 42, 23, 5, 12],
    [45, 33, 65, 3, 17, 8, 90, 6, 48],
    [25, 1, 54, 54, 88, 6, 13, 56, 23],
    [13, 8, 9, 23, 0, 78, 4, 42, 11],
    [28, 98, 12, 45, 18, 34, 7, 28, 75],
    [79, 14, 6, 43, 33, 89, 14, 41, 28],
    [21, 32, 14, 13, 6, 69, 68, 60, 26],
    [34, 76, 98, 24, 8, 5, 17, 18, 13],
]

integral_image = integral_view(image)

if __name__ == "__main__":
    while True:
        try:
            print(
                "\n[0] - Завершить программу\n"
                "[1] - Сгенерировать новую матрицу\n"
                "[2] - Отобразить матрицу изображения\n"
                "[3] - Отобразить матрицу интегрального представления\n"
                "[4] - Вывести сумму пикселей в прямоугольнике"
            )
            action = int(input("Ввод: "))
            if action == 0:
                print("Программа завершена")
                break
            if action == 1:
                height = int(input("\nВведите высоту матрицы: "))
                width = int(input("Введите ширину матрицы: "))
                if height < 2 or width < 2:
                    raise ValueError
                image = generate_matrix(height, width)
            elif action == 2:
                print("\nМатрица изображения:")
                for row in image:
                    print(row)
            elif action == 3:
                integral_image = integral_view(image)
                print("\nМатрица интегрального представления:")
                for row in integral_image:
                    print(row)
            elif action == 4:
                print("\nВведите координаты углов прямоугольника через пробел")
                x1, y1 = map(int, input("Левого верхнего угла: ").split())
                x2, y2 = map(int, input("Правого нижнего угла: ").split())
                if x1 + y1 == x2 + y2 or x1 + y1 > x2 + y2:
                    raise ValueError
                sum_of_rectangle = rect_sum(integral_image, x1, y1, x2, y2)
                print(f"Сумма пикселей в прямоугольнике: {sum_of_rectangle}")
            else:
                raise ValueError
        except (ValueError, IndexError):
            print("Введены не верные данные!")
        except NameError:
            print("Сгенерируйте матрицу!")
