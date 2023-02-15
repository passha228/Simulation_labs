from random import random

# Функция базового сенсора, которая работает только в диапазоне (0, 1)
def sensorBase():
    return random() if (a := random()) != 0 else random()


def checkSensor():
    pass

randSet = []
randSet += [sensorBase() for i in range(1000)]

randSet.sort()
print(randSet)