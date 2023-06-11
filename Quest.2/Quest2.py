print("Codificando palavras")
palavra = input("O que você quer codificar? ")
letrasCodificadas = []
for letra in palavra:
    valorPalavra = ord(letra)
    valorSucessor = valorPalavra + 1
    if letra == 'Z':
        letraCodificada = 'A'
    else:
        letraCodificada = chr(valorSucessor)
    letrasCodificadas.append(letraCodificada)
print("Codificação feita")
print("Resultado: ", "".join(letrasCodificadas))