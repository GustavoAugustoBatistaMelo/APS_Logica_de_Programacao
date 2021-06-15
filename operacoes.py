from cores import cor
from validacoes import validarNota
from validacoes import validarNumeroPositivo
import math

#Funções responsaveis pela operações das questões
#Questão 1
def nomeMedia():
    nome = str(input("Digite o nome do Aluno:".upper().strip()))
    media=0
    c=0
    #for c in range(0,4):
    # Verifica se o Usuário digitou apenas números caso não ele vai repetir até que ele digite números
    while c < 4:
        try:
           nota = float(input(f"{cor('vermelho')}Digite A Nota: "))
           nota = validarNota(nota)
           media += nota
           c += 1
        except ValueError as e:
            print(f"{cor('azul')}Digite apenas Números{cor('remove')}")

    print(f"{cor('vermelho')}-" * 40)
    print(f"{nome} sua Média foi {media / 4}")
    print(f"-" * 40, f"{cor('remove')}")

#Calcula o dobro e o Triplo
#Questão 2
def dobloTriplo():
    # Verifica se o Usuário digitou apenas números caso não ele vai repetir até que ele digite números
    while True:
      try:
        numero = float(input(f"{cor('vermelho')}Digite A Um Número: "))
        print(f"{cor('vermelho')}-" * 60)
        print(f"O dobro e Triplo de {numero} São: Dobro: {cor('azul')}{numero * 2}{cor('vermelho')} e o Triplo:{cor('remove')} {cor('azul')}{numero*3}  ")
        print(f"-" * 60, )
        break
      except ValueError as e:
          print(f"{cor('azul')}Digite Apenas Números{cor('remove')}")


#Questão 3
def aumentoSalario():
 # Verifica se o Usuário digitou apenas números caso não ele vai repetir até que ele digite números
  while True:
    try:
        salario = validarNumeroPositivo(float(input(f"{cor('vermelho')}Digite o Salário: ")))
        print(f"{cor('vermelho')}-" * 40)
        print(f"{cor('remove')}O seu salario com Aumento de 25% é: {cor('azul')}{salario*1.25}  ")
        print(f"-" * 40, f"{cor('remove')}")
        break
    except ValueError as e:
        print(f"{cor('azul')}Digite apenas Números")

#Questão 4
def maiorMenor():
    numeros = []
    c = 0
    # Verifica se o Usuário digitou apenas números caso não ele vai repetir até que ele digite números
    while c < 10:
      try:
        numeros.append(float(input("digite Um valor: ")))
        c += 1
      except ValueError as e:
          print(f"{cor('azul')}Digite apenas Números")

    print(f"{cor('vermelho')}-" * 50)
    print(f"{cor('remove')} O Maior valor : {cor('azul')}{max(numeros)}{cor('remove')} e o Menor valor é: {cor('vermelho')}{min(numeros)} ")
    print(f"{cor('remove')}Media de todos os Números é: {cor('vermelho')}{sum(numeros)/10}")
    print(f"-" * 50, f"{cor('remove')}")


#Questão 5
def imparOuPar():
    lista=[]
    #preenchendo a lista
    for c in range(100,300):
        if c % 2==1:
            lista.append(c)
    print(f"{cor('vermelho')}-" * 40)
    print(f"{cor('azul')}              Ímpares" )
    for c in lista:
         print(f"{c}")
    print(f"-" * 40, f"{cor('remove')}")

#Questão 6
def fatorial():
 numero = 0
 #Verifica se o Usuário digitou apenas números caso não ele vai repetir até que ele digite números
 while True:
     try:
        numero = validarNumeroPositivo(int(input(f"{cor('azul')}Digite o Número para calcularmos o fatorial: ")))
        break
     except ValueError as e:
         print(f"{cor('vermelho')}Digite apenas Números")


 cont = numero
 resultado = 1
 while cont > 0:
     print(f"{cont} ",end='')
     print(' x ' if cont > 1 else '=',end='')
     resultado *= cont
     cont -= 1
 print(" ",resultado)


#Questão 7
def maioresMenoresQueZero():
#maiores,Menores ou iguais a zero
    maior = 0
    menor = 0
    zero = 0
    c = 0
# Verifica se o Usuário digitou apenas números caso não ele vai repetir até que ele digite números
    while c <10:
      try:
        numero = float(input(f"{cor('azul')}Digite um Número: "))
        if numero >0:
               maior += 1
        elif numero <0:
               menor +=1
        elif numero == 0:
               zero+= 1
        c += 1
      except ValueError as e:
        print(f"{cor('vermelho')}Digite Apenas Números")

    print(f"{cor('vermelho')}-" * 40)
    print(f"{cor('remove')}Foram digitados {cor('azul')}{maior}{cor('remove')} maiores que Zero  ")
    print(f"{cor('remove')}Foram digitados {cor('azul')}{menor}{cor('remove')} menores que Zero  ")
    print(f"{cor('remove')}Foram digitados {cor('azul')}{zero}{cor('remove')} iguais que Zero  ")
    print(f"{cor('vermelho')}-" * 40)

#Questão 8

def QuadradodosNumerosSomado():
    numeros = []
    soma = float(0)
    c = 0
    while c <10:
    #for c in range(0,10):
       #Verifica se o Usuário digitou apenas números caso não ele vai repetir até que ele digite números
        try:
            numeros.append(float(input("Digite Um valor: ")))
            soma +=  math.pow(numeros[c],2)
            c += 1
        except ValueError as e:
            print("Digite apenas Números: ")

    print(f"{cor('azul')}-" * 50)
    print(numeros)
    print(f"{cor('remove')}A soma de todo os número elevado ao quadrado é: {cor('vermelho')}{soma}")
    print(f"-" * 50, f"{cor('remove')}")


