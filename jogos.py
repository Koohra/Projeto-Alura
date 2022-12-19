import forca
import adivinhacao

def escolhe_jogo():
    print('*' * 19)
    print('Eschola o seu jogo!')
    print('*' * 19)

    print('(1) Forca (2) Adivinhação')

    jogo = int(input('Qual jogo? '))

    if(jogo == 1):
        print('Jogando forca')
        forca.jogar()
    elif(jogo == 2):
        adivinhacao.jogar()
        print('Jogando adivinhação')
    else:
        print('Escolha entre os números solicitados')

if(__name__ == '__main__'):
    escolhe_jogo()
