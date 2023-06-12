print("Contador de letras!")
palavra = input("Escolha uma palavra: ")
palavra = palavra.upper()
dicio = {}
for letra in palavra:
    if letra not in dicio:
        dicio[letra] = 1
    else:
        dicio[letra] += 1
elementos = ["%s = %sx" % (letra, quantidade) for letra, quantidade in dicio.items()]
resultado = ", ".join(elementos)
print("A palavra %s possui: %s" % (palavra, resultado))