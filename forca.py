def jogar():
    print('*' * 28)
    print('Bem vindo ao jogo da Forca!')
    print('*' * 28)
    
    palavra_secreta = 'gato'
    letras_acertadas = ["_", "_", "_", "_",]
    
    enforcou = False
    acertou = False
    tentativas = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):
        
        chute = str(input('Qual letra?')).strip().lower()
        
        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                    print(f'Encontrei a letra {chute} na posição {index}')
                index += 1
        else:
            tentativas += 1

        enforcou = tentativas == 4
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print('Você ganhou')
    else:
        print('Você perdeu.')
    print('Fim do jogo')

if(__name__ == '__main__'):
    jogar()
