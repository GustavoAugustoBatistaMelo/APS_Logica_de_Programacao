from cores import cor
from validacoes import validarNota
from validacoes import validarNumeroPositivo

#Funções responsaveis pelas validações







#Funções responsaveis pela operações das questões
#Questão 1
def nomeMedia():
    nome = str(input("Digite o nome do Aluno:".upper().strip()))
    media=0
    for c in range(0,4):
           nota = float(input("Digite A Nota: "))
           nota = validarNota(nota)
           media += nota
    print(f"{cor('vermelho')}-" * 40)
    print(f"{nome} sua Média foi {media / 4}")
    print(f"-" * 40, f"{cor('remove')}")
#Calcula o dobro e o Triplo
#Questão 2
def dobloTriplo():
    numero = float(input("Digite A Um Número: "))
    print(f"{cor('vermelho')}-" * 60)
    print(f"{cor('remove')}O dobro e Triplo de {numero} São: Dobro: {cor('azul')}{numero * 2}{cor('remove')} e Triplo: {cor('vermelho')}{numero*3}  ")
    print(f"-" * 60, f"{cor('remove')}")


#Questão 3
def aumentoSalario():
    salario = validarNumeroPositivo(float(input("Digite o Salário: ")))
    print(f"{cor('vermelho')}-" * 40)
    print(f"{cor('remove')}O seu salario com Aumento de 25% é: {cor('azul')}{salario*1.25}  ")
    print(f"-" * 40, f"{cor('remove')}")


#Questão 4
def maiorMenor():
    numeros = []
    for c in range (0,10):
        numeros.append(float(input("digite Um valor: ")))

    print(f"{cor('vermelho')}-" * 50)
    print(f"{cor('remove')} O Maior valor : {cor('azul')}{max(numeros)}{cor('remove')} e o Menor valor é: {cor('vermelho')}{min(numeros/10)} ")
    print(f"{cor('remove')}Media de todos os Números é: {cor('vermelho')}{sum(numeros)}")
    print(f"-" * 50, f"{cor('remove')}")


#Questão 5
def imparOuPar():
    lista=[]
    #preenchendo a lista
    for c in range(100,300):
        if c % 2==1:
            lista.append(c)
    print(f"{cor('vermelho')}-" * 40)
    print(f"{cor('azul')}              Pares" )
    for c in lista:
         print(f"{c}")
    print(f"-" * 40, f"{cor('remove')}")

#Questão 5
def fatorial():
 numero =  validarNumeroPositivo(int(input('Digite o Número para calcularmos o fatorial: ')))
 cont = numero
 resultado = 1
 while cont > 0:
     print(f"{cont} ",end='')
     print(' x' if cont > 1 else '=',end='')
     resultado *= cont
     cont -= 1
 print(resultado)




#Questão 7
def maioresMenoresQueZero():
#maiores,Menores ou iguais a zero
    maior = 0
    menor = 0
    zero = 0
    for c in range(0,10):

        numero = float(input("Digite um número"))
        if numero >0:
               maior += 1
        elif numero <0:
               menor +=1
        elif numero == 0:
               zero+= 1
    print(f"{cor('vermelho')}-" * 40)
    print(f"{cor('remove')}Foram digitados {cor('azul')}{maior}{cor('remove')} maiores que Zero  ")
    print(f"{cor('remove')}Foram digitados {cor('azul')}{menor}{cor('remove')} menores que Zero  ")
    print(f"{cor('remove')}Foram digitados {cor('azul')}{zero}{cor('remove')} iguais que Zero  ")
    print(f"{cor('vermelho')}-" * 40)

#Questão 8

def QuadradodosNumerosSomado():
    numeros = []
    soma = float(0)
    for c in range (0,10):
        numeros.append(float(input("digite Um valor: ")))
        soma += (numeros[c] * numeros[c])
    print(f"{cor('azul')}-" * 50)
    print(numeros)
    print(f"{cor('remove')}A soma de todo os número elevado ao quadrado é: {cor('vermelho')}{soma}")
    print(f"-" * 50, f"{cor('remove')}")

