arquivo = open("texto.txt", "w")

texto = list()

texto.append("Primeira linha.\n")
texto.append("Segunda linha.\n")
texto.append("Terceira linha.\n")

for linha in texto:
    arquivo.write(linha)


arquivo.close()


print("As frases foram escritas no arquivo 'texto.txt'.")