# На основе данных, предоставленных преподавателем, реализовать
# отображение данных на точечной диаграмме с помощью библиотеки
# mathplotlib. Создать модель (квадратичная функция) для предсказания новых
# данных и нанести график этой функции на точечную диаграмму. Вычислить
# отклонение данных модели от реальных данных.
import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("./habitations.tsv", delimiter=",")
x = data[1:, 0]  # площадь
y = data[1:, 2]  # цена

fp = np.polyfit(x, y, 1, full=False)  # Polynomial coefficients, highest power first. (k & b)
f = np.poly1d(fp)  # y = kx + b

fx = np.linspace(0, x, 500)
plt.scatter(x, y, s=10)
plt.plot(fx, f(fx), linewidth=1.0, color='r')
plt.title('Площадь от цены')
plt.xlabel("цена")
plt.ylabel("площадь")
plt.autoscale(tight=True)
plt.grid(True, linestyle="-", color='0.8')
plt.show()
