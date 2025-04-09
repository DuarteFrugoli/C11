import numpy as np

# NumPy Array Unidimensional
arr = np.array([1, 2, 3, 4, 5])

# NumPy Array Bidimensional
mtz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(arr)
print(mtz)

# NumPy Array o Ndarray só utiliza dados do mesmo tipo
# arr = np.zeros(n) -> Array de zeros
# mtz = np.zeros([n,n]) -> Matriz de zeros
# np.ones -> mesma coisa, mas com uns (1)

# arange -> ordem crescente na array
arr = np.arange(10)

print(arr)

# pode ser espaçado (10 a 20 com 2 de espaçamento)
arr = np.arange(10, 20, 2)

print(arr)

arr = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

# Menor e maior valor do array e seu índice
print(arr.min(), arr.argmin())
print(arr.max(), arr.argmax())

# Soma e média
print(arr.sum(), arr.mean())

# Operações índice a índice
print(arr + arr2)
print(arr * arr2)

# Concatenação
print(np.concatenate((arr, arr2)))