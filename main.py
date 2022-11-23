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
f_rise_positive = []
f_rise_negative = []
f_fall_positive = []
f_fall_negative = []


def func(x):
    function = -12 * x ** 4 * math.sin(math.cos(x)) - 18 * x ** 3 + 5 * x ** 2 + 10 * x - 30
    return function


def fall_rise_ind(x):
    global f_fall_positive
    global f_fall_negative
    global f_rise_positive
    global f_rise_negative
    rise_flag = False
    x_fall = []
    x_rise = []
    x_above_0 = []
    x_below_0 = []
    buffer_index = 0
    for i in range(len(x) - 1):
        if func(x[i]) > func(x[i + 1]):
            if rise_flag:
                x_fall.append(x[buffer_index: i])
                buffer_index = i
                rise_flag = False
        else:
            if not rise_flag:
                x_rise.append(x[buffer_index: i])
                buffer_index = i
                rise_flag = True

    for k in range(len(x_fall)):
        storage_pos = []
        storage_neg = []
        for j in x_fall[k]:
            if func(j) < 0:
                storage_neg.append(j)
            else:
                storage_pos.append(j)
        x_below_0.append(storage_neg)
        x_fall[k] = storage_pos
    for k in range(len(x_rise)):
        storage_pos = []
        storage_neg = []
        for j in x_rise[k]:
            if func(j) < 0:
                storage_neg.append(j)
            else:
                storage_pos.append(j)
        x_above_0.append(storage_neg)
        x_rise[k] = storage_pos

    f_fall_positive = x_fall
    f_rise_positive = x_rise
    f_fall_negative = x_below_0
    f_rise_negative = x_above_0


def change_func(x):
    fall_rise_ind(x)
    plt.title(f'Корней функции бесконечное множество')
    plt.xlabel('Ось X')
    plt.ylabel('Ось Y')
    plt.grid()
    plt.plot([x[0], x[-1]], [0, 0], ':g')
    for i in f_fall_positive:
        y = [func(j) for j in i]
        plt.plot(i, y, 'r')
    for i in f_fall_negative:
        y = [func(j) for j in i]
        plt.plot(i, y, '--r')
    for i in f_rise_positive:
        y = [func(j) for j in i]
        plt.plot(i, y, 'b')
    for i in f_rise_negative:
        y = [func(j) for j in i]
        plt.plot(i, y, '--b')
    plt.show()


change_func(x)
