# Разработка скрипта, вычисляющего статистические показатели (среднее
# значение, дисперсия, среднее квадратичное отклонение) для данных,
# считанных из CSV-файла.
import csv
import statistics


with open("./data.csv", "rt") as f:
    reader = csv.reader(f)

    costs = list(map(lambda r: r[2], reader))[1:]

    mean = statistics.mean(costs)  # среднее значение
    dispersion = statistics.pvariance(costs)  # дисперсия
    stdev = statistics.stdev(costs)  # среднее квадратичное отклонение
