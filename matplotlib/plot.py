import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4])
y = x*2
y2 = x*x

# Nomeando os eixos
plt.xlabel("Valores de X")
plt.ylabel("Valores de Y")

# Marcador circular - "o"
# Linhas pontilhadas "-" :    | Linhas tracejadas - "--"
# Cor verde - "g" (green)     | Cor azul - "b" (blue)
# Largura da linha = 3
# Tamanho dos marcadores = 20
plt.plot(x, y, 'o:g', x, y2, 'o--b', linewidth=3, markersize=20,)

plt.show()