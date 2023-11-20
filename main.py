import matplotlib.pyplot as plt
import numpy as np
import scipy.io

# Загрузка данных из файла
mat = scipy.io.loadmat('part_1.mat')

# Извлечение переменной p
p = mat['p']
fpg_data = p[0][0]

# Частота дискретизации
fs = 125  # Гц

# Создание временной оси
t = np.arange(0, len(fpg_data)) / fs

# Построение графика ФПГ от времени
plt.plot(t, fpg_data)
plt.xlabel('Время (сек)')
plt.ylabel('Значение ФПГ')
plt.title('График ФПГ от времени')
plt.grid(True)

# Отображение графика
plt.show()
