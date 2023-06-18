## Questão no. 2 da lista
## Desenvolvido por: Isa Laura e Hildemberg Eling
## Testado e revisado por: Luiz Miguel

## PRIMEIRA VERSÃO DO CÓDIGO:

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

########################################################

## SEGUNDA VERSÃO:

palavra = input("O que você quer codificar? ")
letrasCodificadas = []
for letra in palavra:
    if letra == ' ':   #Modificação feita por Isa para manter o espaço intacto ao codificar frases, antes estava sendo transformado em '!'
        letrasCodificadas.append(letra)
    else:
        letraCodificada = chr(valorSucessor)
        valorPalavra = ord(letra)
        valorSucessor = valorPalavra + 1
        if letra == 'Z':
            letraCodificada = 'A'
        else:
            letraCodificada = chr(valorSucessor)
    letrasCodificadas.append(letraCodificada)
print("Codificação feita")
print("Resultado: ", "".join(letrasCodificadas))

########################################################

## TERCEIRA VERSÃO:

print("Codificando palavras")
palavra = input("O que você quer codificar? ")
palavra = palavra.lower() # Modificação proposta e feita por Luiz e Hildemberg pois o z estava sendo transformado por um símbolo ao colocar ele em uma palavra ou frase
letrasCodificadas = []
for letra in palavra:
    if letra == ' ':
        letrasCodificadas.append(letra)
    else:
        valorPalavra = ord(letra)
        valorSucessor = valorPalavra + 1
        if letra == 'z':  # Modificação proposta e feita por Luiz e Hildemberg pois o z estava sendo transformado por um símbolo ao colocar ele em uma palavra ou frase
            letraCodificada = 'a'
        else:
            letraCodificada = chr(valorSucessor)
    letrasCodificadas.append(letraCodificada)
print("Codificação feita") 
print("Resultado: ", "".join(letrasCodificadas))