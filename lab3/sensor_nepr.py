"""

1. В выбранной среде программирования реализовать датчик непрерывной случайной величины для
своего варианта задания (метод моделирования, плотность вероятностей) в виде функции.
2. Вычислить математическое ожидание и дисперсию моделируемой случайной величины.
3. Получить с помощью датчика выборку, вычислить выборочное среднее и несмещѐнную выборочную
дисперсию, сравнить с теоретическими.

Метод суперпозиции. Плотность вероятности
p(x) = 3*e/(1 + 3 * e) * (x ^ -2 + x ^ 2 * e ^ x ^ -3) x >= 1

"""

import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore", message="divide by zero encountered in power")
warnings.filterwarnings("ignore", message="overflow encountered in exp")

from lab2.sensor_discr import SensorDiscr
from lab1.sensor_base import SensorBase

def f(x):
    return 3 * np.exp(1)/(1 + 3 * np.exp(1)) * (x ** -2 + np.power(x, 2) * np.exp(-x ** 3))

def SensorNepr(p: np.ndarray): 
    alfa = SensorBase()
    k = SensorDiscr(p)

    if k == 1:
        return 1 / (1 - alfa)
    else:
        return np.power(1 - np.log(1 - alfa), 1/3)

def Main():
    func = np.frompyfunc(f, 1, 1)
    p = np.array([3 * np.exp(1) / (1 + 3 * np.exp(1)), 1 / (1 + 3 * np.exp(1))])
    
    
    n = 10
    while n < 100001:
        X = np.array([SensorNepr(p) for i in range(n)])

        print(f'n = {n}')
        print(f'Дисперсия : {np.var(X)}')
        print(f'Выборочное среднее: {sum(X) / n}')
        
        print()

        n *= 10

    x = np.linspace(1, 10, 1000)
    X = np.array([SensorNepr(p) for i in range(20)])
    print(X)
    plt.plot(x, func(x), 'red')
    plt.hist(X)
    plt.show()
