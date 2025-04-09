import numpy as np

mtz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Printa tudo da terceira linha
print("mtz[2]:\n", mtz[2], "\n")

# Printa toda a primeira e sgunda linha
print("mtz[0:2]:\n", mtz[0:2], "\n")

# Printa tudo da segunda coluna
print("mtz[:, 1]:\n", mtz[:, 1], "\n")

# Printa a primeira e a segunda linha começando da segunda coluna
print("mtz[0:2, 1:]:\n", mtz[0:2, 1:], "\n")

# Condicional, evita o for e diz se a condição é verdadeira para todos os elementos do array
print("mtz > 5:\n", mtz > 5, "\n")

# Condicional como filtro
print("mtz[mtz > 5]:\n", mtz[mtz > 5], "\n")

# Variável para guardar condicional
cond = mtz%2 == 0
print("cond:\n", cond, "\n")
print("mtz[cond]:\n", mtz[cond], "\n")