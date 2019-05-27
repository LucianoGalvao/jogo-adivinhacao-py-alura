
import random

def bem_vindo():
    print("********************************")
    print("***Bem vindo ao jogo de forca***")
    print("********************************")
    print()

def jogar():

    bem_vindo()

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()


    numero = random.randrange(0,len(palavras))

    nome = input("Por favor, digite seu nome: ")

    print("Olá {}, estou pensando em uma palavra secreta, você é capaz de acertar?".format(nome))
    print()

    palavra_secreta = palavras[numero].upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    print()
     
    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print("Você chutou a letra {}".format(chute))
            if(erros < 5):
                print("Ainda faltam {} tentativas!".format(5-erros))
            elif(erros == 5):
                print("Ainda falta 1 tentativa!")

        enforcou = erros == 5
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

    if(acertou):
        print()
        print("Parabéns {}! Você acertou, a palavra secreta era \"{}\"".format(nome,palavra_secreta))
    elif(enforcou):
        print()
        print("Que pena {}! Infelizmente você não conseguiu acertar a palavra secreta!".format(nome))
        

    print()
    print("Fim de jogo!")
    print()


if( __name__ == "__main__"):
    jogar()