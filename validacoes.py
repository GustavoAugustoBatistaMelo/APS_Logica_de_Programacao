#Funções responsaveis pelas validações

#Verifica se os numeros são entre 0 e 10,e retorna o valor, caso não esteja entre esse valores vai repetir até que os valores
#esteja corretos.
from cores import cor
def validarNota(numero):
    while True:
        if numero < 0 or numero > 10:
            numero = float(input(f"{cor('vermelho')}Digite uma nota valida! entre 0 e 10: "))
        else:
            return numero
            break


#Verifica se o Número é positivo
def validarNumeroPositivo(salario):
    while True:
        if salario <=0 :
            salario = float(input(f"{cor('vermelho')}Digite um Valor valido! Maior que 0: "))
        else:
            return salario
            break