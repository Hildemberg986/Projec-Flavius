## Questão no. 3 da lista
## Desenvolvido por: Isa Laura e Luiz Miguel
## Revisado e testado por: Hildemberg Eling

## PRIMEIRA VERSÃO DO CÓDIGO:

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

########################################################

## SEGUNDA VERSÃO:

print("Contador de letras!") # Adição apenas estética
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