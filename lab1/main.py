from random import random
import numpy as np
import matplotlib.pyplot as plt
from colorama import init, Fore

init(autoreset=True)

# Функция базового сенсора, которая работает только в диапазоне (0, 1)
def sensorBase():
    while(a := random()) == 0:
        pass
    return a

def KolmagorovSmirnov():
    # критическое значение, из таблицы (alpha = 0.1)
    k_alpha = 1.22 
    count = 1000

    empirFunc = np.array([i / count for i in range(count)])
    empirFunc1 = np.array([(i + 1) / count for i in range(count)])
    
    theoreticalFunc = np.array([sensorBase() for i in range(count)])
    theoreticalFunc.sort()
    
    D = max(abs(empirFunc - theoreticalFunc))
    D1 = max(abs(empirFunc1 - theoreticalFunc))
    D = max(D, D1)

    k = np.sqrt(count) * D
    
    print("Эмпирическая функция и теоретическая: ")
    print(empirFunc, empirFunc1, theoreticalFunc, sep='\n', end = '\n\n')
    print(f"k = {k}")
    
    if (k > k_alpha):
        print(Fore.RED + "Эмперические данные противоречат теоретическому закону распределения")
    else:
        print(Fore.RED + "Эмперические данные не противоречат теоретическому закону распределения")

    y = np.array([i / count for i in range(count)])
    plt.plot(theoreticalFunc, y, color = 'b')
    plt.plot(empirFunc, y, color = 'g')
    plt.plot(empirFunc1, y, color = 'g')
    plt.show()

KolmagorovSmirnov()