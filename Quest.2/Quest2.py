print("Codificando palavras")
palavra = input("O que você quer codificar? ")
letrasCodificadas = []
for letra in palavra:
    if letra == ' ':      # Modificação feita para manter o espaço intacto ao codificar frases, antes estava sendo transformado em '!'
        letrasCodificadas.append(letra)
    else:
        valorPalavra = ord(letra)
        valorSucessor = valorPalavra + 1
        if letra == 'Z':
            letraCodificada = 'A'
        else:
            letraCodificada = chr(valorSucessor)
    letrasCodificadas.append(letraCodificada)
print("Codificação feita")
print("Resultado: ", "".join(letrasCodificadas))