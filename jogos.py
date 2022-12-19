import forca
import adivinhacao

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
