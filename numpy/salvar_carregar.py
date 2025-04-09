import numpy as np

# Carregando e salvando arquivo .txt ou .csv
dataset = np.loadtxt("arquivo.txt")
dataset = np.savetxt("arquivo.txt")

# Carregando e salvando arquivo binário .npy
dataset = np.load("arquivo.npy")
dataset = np.save("arquivo.npy")

# Caregando o dataset space.csv
dataset = np.loadtxt('space.csv', delimiter=';', dtype=str, encoding='utf-8')