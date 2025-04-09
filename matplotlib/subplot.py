import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4])
y = x*2
y2 = x*x

plt.subplot(1, 2, 1)  # 1 linha, 2 colunas, primeiro gráfico
plt.title("Função Linear")
plt.plot(x, y, 's:r')

plt.subplot(1, 2, 2)  # 1 linha, 2 colunas, primeiro gráfico
plt.title("Função Exponencial")
plt.plot(x, y2, 'o-b')
plt.show()