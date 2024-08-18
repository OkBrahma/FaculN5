import time

def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

def selection_sort(array):
    n = len(array)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array


palavras = list()
with open("texto.txt", "r") as arquivo:
    for linha in arquivo:
        palavras.extend(linha.split())

start_time = time.time()
bubble_sorted = bubble_sort(palavras.copy())
bubble_time = time.time() - start_time

start_time = time.time()
selection_sorted = selection_sort(palavras.copy())
selection_time = time.time() - start_time

start_time = time.time()
python_sorted = sorted(palavras.copy())
python_time = time.time() - start_time

print("Resultado do Bubble Sort:")
print(bubble_sorted)
print(f"Tempo de execução do Bubble Sort: {bubble_time:.6f} segundos\n")

print("Resultado do Selection Sort:")
print(selection_sorted)
print(f"Tempo de execução do Selection Sort: {selection_time:.6f} segundos\n")

print("Resultado do Sort nativo do Python:")
print(python_sorted)
print(f"Tempo de execução do Sort nativo do Python: {python_time:.6f} segundos\n")

melhor_metodo = min(bubble_time, selection_time, python_time)
if melhor_metodo == bubble_time:
    melhor_resultado = bubble_sorted
elif melhor_metodo == selection_time:
    melhor_resultado = selection_sorted
else:
    melhor_resultado = python_sorted
with open("palavras_ordenadas.txt", "w") as arquivo_saida:
    for palavra in melhor_resultado:
        arquivo_saida.write(palavra + "\n")

print("Palavras ordenadas salvas em 'palavras_ordenadas.txt'.")