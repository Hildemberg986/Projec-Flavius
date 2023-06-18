## Questão no. 5 da lista
## Desenvolvido por: Hildemberg Eling e Luiz Miguel
## Testado e revisado por: Isa Laura

## PRIMEIRA VERSÃO DO CÓDIGO:

import os

nome = input("Digite seu primeiro nome: ")
while nome.isalpha() == False:
  print()
  print("O nome é inválido pois possui caracteres especiais. Por favor, digite novamente.")
  print()
  nome = input("Digite seu primeiro nome: ")
os.system('clear')
snome = input("Digite seu segundo nome: ")
while snome.isalpha() == False:
  print()
  print("O nome é inválido pois possui caracteres especiais. Por favor, digite novamente.")
  print()
  snome = input("Digite seu segundo nome: ")
os.system('clear')
email = input("Digite seu email: ")
while True:
  if email.count("@") == 1 and email.count(".") >= 1:
    arroba = email.index("@")
    ponto = email.index(".")
    if arroba > 0 and arroba < len(email) - 1 and ponto > (arroba + 1) and len(email) - ponto >= 3:
      os.system('clear')
      break
    else:
      print("O e-mail é inválido. Por favor, digite novamente.")
      print()
      email = input("Digite seu email: ")
    os.system('clear')  
  else:
    print("O e-mail é inválido. Por favor, digite novamente.")
    print()
    email = input("Digite seu email: ")
  os.system('clear')  
print("Seu nome é: %s %s"%(nome, snome))
print("Seu email é:", email)

########################################################

## SEGUNDA VERSÃO:
import os
import platform  # Modificação proposta e feita por Isa e Hildemberg para a tela limpar de acordo com o sistema do usuário,
                 #já que estava dando bug no Windows

system = platform.system()
nome = input("Digite seu primeiro nome: ")

while nome.isalpha() == False:
  print()
  print("O nome é inválido pois possui caracteres especiais. Por favor, digite novamente.")
  print()
  nome = input("Digite seu primeiro nome: ")
if system == 'Windows':
  os.system('cls')
else:
  os.system('clear')

snome = input("Digite seu segundo nome: ")
while snome.isalpha() == False:
  print()
  print("O nome é inválido pois possui caracteres especiais. Por favor, digite novamente.")
  print()
  snome = input("Digite seu segundo nome: ")
if system == 'Windows':
  os.system('cls')
else:
  os.system('clear')

email = input("Digite seu email: ")
while True:
  if email.count("@") == 1 and email.count(".") >= 1:
    arroba = email.index("@")
    ponto = email.index(".")
    if arroba > 0 and arroba < len(email) - 1 and ponto > (arroba + 1) and len(email) - ponto >= 3:
      if system == 'Windows':
        os.system('cls')
      else:
        os.system('clear')
      break
    else:
      print("O e-mail é inválido. Por favor, digite novamente.")
      print()
      email = input("Digite seu email: ") 
    if system == 'Windows':
      os.system('cls')
    else:
      os.system('clear')  
  else:
    print("O e-mail é inválido. Por favor, digite novamente.")
    print()
    email = input("Digite seu email: ")  
  if system == 'Windows':
    os.system('cls')
  else:
    os.system('clear')  
print("Seu nome é: %s %s"%(nome, snome))
print("Seu email é:", email)

########################################################

## TERCEIRA VERSÃO:

import os
import platform

system = platform.system()

def limpar_tela(): # Otimização do código proposta e feita por Isa
    if system == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
        
nome = input("Digite seu primeiro nome: ")
while nome.isalpha() == False:
  print()
  print("O nome é inválido pois possui caracteres especiais. Por favor, digite novamente.")
  print()
  nome = input("Digite seu primeiro nome: ")
limpar_tela()

snome = input("Digite seu segundo nome: ")
while snome.isalpha() == False:
  print()
  print("O nome é inválido pois possui caracteres especiais. Por favor, digite novamente.")
  print()
  snome = input("Digite seu segundo nome: ")
limpar_tela()

email = input("Digite seu email: ")
while True:
  if email.count("@") == 1 and email.count(".") >= 1:
    arroba = email.index("@")
    ponto = email.index(".")
    if arroba > 0 and arroba < len(email) - 1 and ponto > (arroba + 1) and len(email) - ponto >= 3:
      limpar_tela()
      break
    else:
      print("O e-mail é inválido. Por favor, digite novamente.")
      print()
      email = input("Digite seu email: ")
    limpar_tela()
  else:
    print("O e-mail é inválido. Por favor, digite novamente.")
    print()
    email = input("Digite seu email: ")
  limpar_tela()
print("Seu nome é: %s %s"%(nome, snome))
print("Seu email é:", email)