from cores import cor

#APOS USUARIO ESCOLHER UMA OPÇÃO E VISUALIZAR O RESULTADO PERGUNTA SE DESEJA VOLTA AO MENU PRINCIPAL
#Caso usuario queira continuar irar retornar verdadeiro para que o programa principal repita as opções,se não ira encerrar
def sair():
    sair=str(input("Deseja voltar ao Menu Principal? S/N: ")).upper()
    while True:
       #TEstando se usuario está digitando S ou N.
       #Caso estiver digitando uma opção invalida ira repetir até que seja digitado uma opção valida
        if not sair == "S" and not sair == "N":
             sair=str(input(f"{cor('vermelho')}Opção Invalida! Digite Apenas S/N :"))
        else:
            if sair == "S":
                break
            else:
                print(f"{cor('vermelho')}SISTEMA ENCERRADO!")
                return True
                break

#MENU PRINCIPAL
#exibe o menu principal
#Usado Modulo cores para mudar as cores das Strings
def opcoes():
    print(f"{cor('vermelho')}-"*40)
    print("|               MENU                   |")
    print(f"-" * 40,f"{cor('remove')}")
    print(f"{cor('vermelho')}1{cor('remove')} - {cor('azul')}Nome e media do aluno:")
    print(f"-" * 40, f"{cor('remove')}")
    print(f"{cor('vermelho')}2{cor('remove')} - {cor('azul')}Dobro e Triplo")
    print(f"-" * 40, f"{cor('remove')}")
    print(f"{cor('vermelho')}3{cor('remove')} - {cor('azul')} Aumento de salario em 25%")
    print(f"-" * 40, f"{cor('remove')}")
    print(f"{cor('vermelho')}4{cor('remove')} - {cor('azul')}Maior Valor, Menor valor e Média")
    print(f"-" * 40, f"{cor('remove')}")
    print(f"{cor('vermelho')}5{cor('remove')} - {cor('azul')}Número impares entre 100 e 300")
    print(f"-" * 40, f"{cor('remove')}")
    print(f"{cor('vermelho')}6{cor('remove')} - {cor('azul')}fatorial do Número Inteiro positivo")
    print(f"-" * 40, f"{cor('remove')}")
    print(f"{cor('vermelho')}7{cor('remove')} - {cor('azul')}maior,menor ou igual a Zero")
    print(f"-" * 40, f"{cor('remove')}")
    print(f"{cor('vermelho')}8{cor('remove')} - {cor('azul')}Soma dos Quadrador de 10 Números")
    print(f"-" * 40, f"{cor('remove')}")
    print(f"{cor('vermelho')}9{cor('remove')} -{cor('azul')} sair")
    print(f"-" * 40, )
    opcao = int(input(f"{cor('vermelho')}Digite uma Opção: "))
    return opcao
    print("-"*30)
