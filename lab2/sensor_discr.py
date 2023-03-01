import numpy as np
from lab1.sensor_base import sensorBase
N = 1000

def SensorDiscr(p : np.ndarray) -> int:
    if sum(p) > 1:
        raise ValueError("Сумма вероятностей больше 1")

    rand, s, res = sensorBase(), 0, -1
    
    while s < rand:
        res += 1
        s += p[res]
    return res 


def Win(states: dict) -> str:
    winCombinations = {
        'камень - ножницы' : 'камень',
        'бумага - камень' : 'бумага',
        'колодец - камень' : 'колодец',
        'колодец - ножницы' : 'колодец',
        'ножницы - бумага' : 'ножницы',
        'бумага - колодец' : 'бумага',
    }
    if states['blue'] == states['red']:
        return 'draw'

    reg1 = rf"{states['blue']} - {states['red']}"
    reg2 = rf"{states['red']} - {states['blue']}"
    
    if (winner := winCombinations.get(reg1)) != None:
        if winner == states['red']: return 'red'
        else: return 'blue'
    else:
        winner = winCombinations.get(reg2)
        if winner == states['red']: return 'red'
        else: return 'blue'


def Game() -> None:
    choises = ['камень', 'ножницы', 'бумага', 'колодец']
    bluePlayerProbability = np.array([0, 0, 1/2, 1/2])
    #bluePlayerProbability = np.array([1/4, 1/4, 1/4, 1/4])
    redPlayerProbability = np.array([1/4, 1/4, 1/4, 1/4])
    blueStaffCount = {
        'камень' : 0,
        'ножницы': 0,
        'бумага': 0,
        'колодец': 0,
    }
    redStaffCount = {
        'камень' : 0,
        'ножницы': 0,
        'бумага': 0,
        'колодец': 0,
    }
    countOfWin = {
        'blue' : 0,
        'red': 0,
        'draw': 0,
    }
    playersValue = {
        'blue' : 0,
        'red': 0,
    }
    games = []

    for i in range(N):
        states = {
            'blue': choises[SensorDiscr(bluePlayerProbability)],
            'red': choises[SensorDiscr(redPlayerProbability)],
        }
        blueStaffCount[states['blue']] += 1
        redStaffCount[states['red']] += 1

        winner = Win(states)

        match winner:
            case 'red':
                playersValue['blue'] -=1
                playersValue['red'] +=1
                countOfWin['red'] +=1
            case 'blue':
                playersValue['blue'] +=1
                playersValue['red'] -=1
                countOfWin['blue'] +=1
            case 'draw':
                countOfWin['draw'] += 1
        games.append(states)
        games[i]['win'] = winner

    print(f"Количество выигрышей первого игрока: {countOfWin['blue']}")
    print(f"Количество выигрышей второго игрока: {countOfWin['red']}")
    print(f'Количествно партий сыгранных в ничью: {countOfWin["draw"]}')
    # print(f"Выигрыш первого игрока: {playersValue['blue']}")
    # print(f"Выигрыш второго игрока: {playersValue['red']}")
    print(f"Средний выигрыш первого игрока: {playersValue['blue'] / N}")
    print(f"Средний выигрыш второго игрока: {playersValue['red'] / N}")
    #print(f"Все партии:\n {games}")
    print(f"Все выборы первого игрока: {blueStaffCount}")
    print(f"Все выборы воторого игрока: {redStaffCount}")

def CheckSensor():
    arr = np.array([1/4,1/4,1/4,1/4])
    res = []
    for i in range(N):
        res.append(SensorDiscr(arr))
    
    print(f"count 0 -> {res.count(0)}")
    print(f"count 1 -> {res.count(1)}")
    print(f"count 2 -> {res.count(2)}")
    print(f"count 3 -> {res.count(3)}")
    print(f"count 4 -> {res.count(4)}")