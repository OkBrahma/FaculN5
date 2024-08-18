arquivo = open("loremipsum.txt", "r")

conteudo_completo = arquivo.read()
print("Conteúdo completo do arquivo:\n")
print(conteudo_completo)

arquivo.seek(0)

primeira_linha = arquivo.readline()
print("\nPrimeira linha do arquivo:\n")
print(primeira_linha)

arquivo.seek(0)

tres_primeiros_caracteres = arquivo.read(3)
print("\nOs 3 primeiros caracteres do arquivo:\n")
print(tres_primeiros_caracteres)


arquivo.close()


print("\nConteúdo do arquivo utilizando 'with':\n")
with open("loremipsum.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)