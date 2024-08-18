import random

array_numeros = [random.randint(1, 100) for _ in range(15)]

array_numeros.sort()

print("Array de números em ordem crescente:")
print(array_numeros)

array_numeros.sort(reverse=True)

print("\nArray de números em ordem decrescente:")
print(array_numeros)

array_strings = ["nome", "dataNascimento", "cpf", "rg"]

array_strings.sort()

print("\nArray de strings em ordem crescente:")
print(array_strings)

array_strings.sort(reverse=True)

print("\nArray de strings em ordem decrescente:")
print(array_strings)