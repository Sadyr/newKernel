Игра "Жизнь”
import random, time, copy
WIDTH = 60
HEIGHT - 20
# Создание списка списков для клеток
nextCells = []
for х in range(WIDTH):
column = []
# создание нового столбца
for у in range(HEIGHT):
if random.randint(0, 1) == 0:
# добавление живой клетки
column.append('#')
else:
column.append(’ ’)
# добавление мертвой клетки
nextCells.append(column)
# переменная nextCells содержит
# список столбцов
while True:
# основной цикл программы
print(’\n\n\n\n\n')
# отделим каждый шаг с помощью
# символов новой строки
currentcells = сору.deepcopy(nextCells)
# Вывод текущих клеток на экран
for у in range(HEIGHT):
for x in range(WIDTH):
print(currentcells[x][у],
print()
# вывод решетки
# или пробела
# вывод символа новой строки в конце
end='’)
# Вычисление клеток на следующем шаге
# на основе клеток текущего шага
for х in range(WIDTH):
for у in range(HEIGHT):
# Получение соседних координат
# Выражение ’% WIDTH' гарантирует, что значение
# leftCoord всегда находится между 0 и WIDTH - 1
leftCoord
(x - 1) 0О WIDTH
rightCoord = (X + 1) а0 WIDTH
aboveCoord = (у - 1) 0О HEIGHT
belowCoord = (У + 1) а о HEIGHTСписки
155
# Вычисление количества живых соседних клеток
numNeighbors = О
if currentcells[leftCoord][aboveCoord] ==
numNeighbors += 1
# жива соседняя клетка
# слева сверху
if currentcells[х][aboveCoord] ==
numNeighbors += 1
# жива соседняя клетка
if currentcells[rightCoord][aboveCoord] ==
numNeighbors += 1
# жива соседняя клетка
# справа сверху
if currentcells[leftCoord] [у] ==
numNeighbors += 1
# жива соседняя клетка
if currentcells[rightCoord][у] ==
numNeighbors += 1
# жива соседняя клетка
if currentcells[leftCoord][belowCoord] ==
numNeighbors += 1
# жива соседняя клетка
# слева снизу
if currentcells[х][belowCoord] ==
numNeighbors += 1
# жива соседняя клетка
if currentcells[rightCoord][belowCoord] ==
numNeighbors += 1
# жива соседняя клетка
# справа снизу
сверху
слева
справа
снизу
# Изменение клетки на основе правил игры "Жизнь"
if currentcells[х][у] ==
and (numNeighbors == 2 or
numNeighbors == 3):
# Живые клетки с двумя или тремя живыми
# соседями остаются живыми
nextCells[х][у] = ’#’
elif currentcells[х][у] == ' ’ and numNeighbors == 3:
# Мертвые клетки с тремя живыми соседями оживают
nextCells[х][у] = ’#’
else:
# Все остальные клетки умирают или остаются мертвыми
nextCells[х][у] = ’ '
time.sleep(1)
# добавим секундную паузу,
# чтобы уменьшить мерцание