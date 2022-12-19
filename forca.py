def jogar():
    print('*' * 28)
    print('Bem vindo ao jogo da Forca!')
    print('*' * 28)
    
    palavra_secreta = 'gato'
    letras_acertadas = ["_", "_", "_", "_",]
    
    enforcou = False
    acertou = False

    print(letras_acertadas)

    while(not enforcou and not acertou):
        
        chute = str(input('Qual letra?')).strip().lower()
        
        index = 0
        for letra in palavra_secreta:
            if(chute == letra):
                letras_acertadas[index] = letra
                print(f'Encontrei a letra {chute} na posição {index}')
            index += 1

        print(letras_acertadas)

    
    print('Fim do jogo')

if(__name__ == '__main__'):
    jogar()
