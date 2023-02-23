import lab1.sensor_base
import lab2.sensor_discr
from sys import argv

if __name__ == '__main__':
    
    if '1' in argv:
        lab1.sensor_base.KolmagorovSmirnov()
    elif '2' in argv:
        lab2.sensor_discr.Game()
    else:
        print("Такого аргумента не существует")