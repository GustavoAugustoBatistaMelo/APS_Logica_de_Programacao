#Responsavel por retonar as cores para formatação das cores das Strings na tela para usuario ou remover a cor
vermelho = "\033[1;31m"
verde ="\033[1;32m"
amarelo ="\033[1;33m"
azul ="\033[1;34m"
Roxo ="\033[1;35m"
cor ="\033[1;36m"
removerCor="\033[m"
def cor (cor):
    cor = str(cor).upper()
    if cor == "vermelho".upper():
        return vermelho
    elif cor == "azul".upper():
        return azul
    elif cor =="remove".upper():
        return removerCor

    