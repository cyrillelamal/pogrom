# Осуществить рефакторинг (модификация) скрипта, вычисляющего
# статистические показатели для данных, считанных из CSV, с использованием
# библиотеки научных вычислений numpy.
import numpy as np

data = np.genfromtxt("./data.csv", delimiter=",")
data = data[1:]

costs = data[:, 2]

mean = np.mean(data)  # среднее значение
variance = np.var(data)  # дисперсия
std = np.std(data)  # среднее квадратичное отклонение
