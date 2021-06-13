from menu import opcoes,sair
import operacoes
listaOpcao =(1,2,3,4,5,6,7,8,9)
#OBSERVAÇÂO: Toda a logica dos exercicios estão no modulo operacoes
while True:
    #Função que chama o Menu
    resposta= opcoes()
    if resposta in listaOpcao:
        #----------------OPÇÃO 1-----------
        if resposta == 1:
           operacoes.nomeMedia()

        #--------OPÇÃO 2-----------
        elif resposta == 2:
           operacoes.dobloTriplo()

       # --------OPÇÃO 3-----------

        elif resposta == 3:
            operacoes.aumentoSalario()

        # --------OPÇÃO 4-----------

        elif resposta == 4:
            operacoes.maiorMenor()

        # --------OPÇÃO 5-----------

        elif resposta == 5:
            print("Opção 5")
            operacoes.imparOuPar()

        # --------OPÇÃO 6----------

        elif resposta == 6:
            operacoes.fatorial()

        # --------OPÇÃO 7-----------

        elif resposta == 7:
           operacoes.maioresMenoresQueZero()

        # --------OPÇÃO 8-----------

        elif resposta == 8:
           operacoes.QuadradodosNumerosSomado()

        # --------OPÇÃO SAIR -----------

        elif resposta == 9:
            print("SISTEMA ENCERRADO!")
            break
        if sair():
            break
    else:
        print("Opção invalida")
        if sair():
          break





