import random

array_numeros = [random.randint(1, 100) for _ in range(15)]

for i in range(len(array_numeros)):
    min_index = i
    for j in range(i + 1, len(array_numeros)):
        if array_numeros[min_index] > array_numeros[j]:
            min_index = j
    

    array_numeros[i], array_numeros[min_index] = array_numeros[min_index], array_numeros[i]


print(array_numeros)