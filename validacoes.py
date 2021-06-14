#Verifica se os numeros são entre 0 e 10,e retorna o valor, caso não esteja entre esse valores vai repetir até que os valores
#esteja corretos.
def validarNota(numero):
    while True:
        if numero < 0 or numero > 10:
            numero = float(input('Digite uma nota valida! entre 0 e 10: '))
        else:
            return numero
            break



def validarNumeroPositivo(salario):
    while True:
        if salario <0 :
            salario = float(input('Digite uma nota valida! entre maior que 0: '))
        else:
            return salario
            break