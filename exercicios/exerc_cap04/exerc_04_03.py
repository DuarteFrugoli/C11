import numpy as np

np.random.seed()

# Matriz 2x2 de zeros
mtz = np.zeros([2, 2])

# Matriz auxiliar para saber qual local já foi verificado
mtzAux = np.zeros([2, 2])

# Escolhe a linha e a coluna em que o 1 deve ficar
linha, coluna = np.random.randint(0, 2, 2)

# Coloca o 1 na matriz
mtz[linha, coluna] = 1

# Mostra a matriz
print(mtz)

# Testa 3 vezes se o usuário digitou o a posição correta ou incorreta
for _i in range(3):
    while True:
        # Entrada de linha e coluna
        linha = int(input('digite o número de uma linha:')) - 1
        coluna = int(input('digite o número de uma coluna:')) - 1

        # Testa se a posição é válida e se ela já foi testada
        if (not 0 <= linha <= 1) or (not 0 <= coluna <= 1):
            print('escolha uma posição de 1 a 2')
        elif mtzAux[linha, coluna] == 0:
            mtzAux[linha, coluna] = 1
            break
        else:
            print('essa posição já foi testada')
    
    # Se o usuário errar uma vez ele perde, se acertar 3x ele ganha
    if mtz[linha, coluna] == 1:
        print('Game Over! :( Try Again"')
        break
    elif _i == 2:
        print('Congratulations! You beat the game! :)')