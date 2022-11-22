# f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30
#
# Определить корни
# Найти интервалы, на которых функция возрастает
# Найти интервалы, на которых функция убывает
# Построить график
# Вычислить вершину
# Определить промежутки, на котором f > 0
# Определить промежутки, на котором f < 0

import math
import numpy as np
import matplotlib.pyplot as plt


x = np.arange(-10, 10, 0.01)
rise_flag = False
func_rise = []
func_fall = []


def func(x):
    function = -12*x**4 * math.sin(math.cos(x)) - 18*x**3 + 5*x**2 + 10*x - 30
    return function


def fall_rise_ind(x):
    global rise_flag
    global func_fall
    global func_rise
    buffer_index = 0
    for i in range(len(x) - 1):
        if func(x[i]) > func(x[i + 1]):
            if rise_flag:
                func_rise.append(x[buffer_index: i])
                buffer_index = i
                rise_flag = False
        else:
            if not rise_flag:
                func_fall.append(x[buffer_index: i])
                buffer_index = i
                rise_flag = True


# def sqr_roots(a, b, c):
#     dscrt = b ** 2 - 4 * a * c
#     if dscrt > 0:
#         x1 = (-b + math.sqrt(dscrt)) / (2 * a)
#         x2 = (-b - math.sqrt(dscrt)) / (2 * a)
#         return x1, x2
#     elif dscrt == 0:
#         x = -b / (2 * a)
#         return x
#     else:
#         return None


# min_func = min(func(x))

# x = sqr_roots(a, b, c-min_func)


def change_func(x):
    # y = [func(i) for i in x]
    fall_rise_ind(x)
    # plt.title(f'Корни функции: {round(sqr_roots(a, b, c)[0], 2)}, {round(sqr_roots(a, b, c)[1], 2)}')
    plt.xlabel('Ось X')
    plt.ylabel('Ось Y')
    plt.grid()
    # plt.plot(x, y, 'r')
    for i in func_fall:
        y = [func(j) for j in i]
        plt.plot(i, y, 'r', label="Убывание")
    # plt.plot(x_range_down, func(x_range_down), 'r', label="Убывание")
    for i in func_rise:
        y = [func(j) for j in i]
        plt.plot(i, y, 'b', label="Возрастание")
    # plt.plot(x_range_up, func(x_range_up), 'b', label="Возрастание")
    # plt.plot(x, func(x), 'ro')
    # plt.text(x, func(x) + 30, f'Вершина функции x = {x}')
    plt.legend()
    plt.show()


change_func(x)
