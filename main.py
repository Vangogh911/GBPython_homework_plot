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


def change_func(x):
    fall_rise_ind(x)
    plt.title(f'Корней функции бесконечное множество')
    plt.xlabel('Ось X')
    plt.ylabel('Ось Y')
    plt.grid()
    plt.plot([x[0], x[-1]], [0, 0], ':g')
    for i in func_fall:
        y = [func(j) for j in i]
        plt.plot(i, y, 'r')
    for i in func_rise:
        y = [func(j) for j in i]
        plt.plot(i, y, 'b')
    plt.show()


change_func(x)
