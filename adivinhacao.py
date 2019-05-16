
print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")
import random

numero_secreto = random.randint(1,10)
numero_tentativas = 3
rodada = 1
nome = input("Qual o seu nome? ")
print()
print("Olá {}, estou pensando em um número de 1 a 10.".format(nome)) 
print("Você tem apenas 3 tentativas para acertar.") 

for rodada in range(1, numero_tentativas + 1):
  print("Tentativa {} de {}".format(rodada,numero_tentativas))
  print()
  chute = input("Digite seu chute: ")
  chute = int(chute)
  
  acertou = chute == numero_secreto
  maior = chute > numero_secreto
  menor = chute < numero_secreto

  if(acertou):
    rodadaStr = str(rodada)
    print()
    if(rodada == 1):
      print("Parabéns, você acertou em {} tentativa.".format(rodadaStr))
    elif(rodada != 1):
      print("Parabéns, você acertou em {} tentativas.".format(rodadaStr))
    break

  else:
    if(maior):
      print("Lamento, mas meu número é menor!")
    elif(menor):
      print("Lamento, mas meu número é maior!")
  print()
      
if(rodada > 3):
  print("Que pena {}, mas você gastou todas as suas tentativas!".format(nome))
  numero_secreto = str(numero_secreto)
  print("Eu estava pensando no número {}".format(numero_secreto))

print()
print("Fim de jogo!")
