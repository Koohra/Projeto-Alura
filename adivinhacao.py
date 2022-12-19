from random import randint

print('*' * 33)
print('Bem vindo no jogo de Adivinhação!')
print('*' * 33)

total_tentativas = 0
numero_secreto = randint(1, 100)
pontos = 1000

print('Qual nivel de dificuldade?')
print('(1) Fácil (2) Médio (3) Difício')

nivel = int(input('Defina um nível: '))

if(nivel == 1):
    total_tentativas = 20

elif(nivel == 2):
    total_tentativas = 10

else:
    total_tentativas = 5

for rodada in range (1, total_tentativas + 1): 
    print(f'Tentativa {rodada} de {total_tentativas}')
    chute = int(input('Digite um numero entre 1 e 100: '))

    if(chute < 1 or chute > 100):
        print('Você deve digitar um número entre 1 e 100!')
        continue
    
    acertou = chute == numero_secreto
    maior   = chute >  numero_secreto
    menor   = chute <  numero_secreto

    if(acertou):
        print(f'Você digitou {chute}')
        print(f'Voce acertou e fez {pontos}')
        break
    else:
        if(maior):
            print('Você errou! O seu chute foi maior do que o número secreto.')
        elif(menor):
            print('Você errou! O seu chute foi menor do que o número secreto.')
    pontos_perdidos = abs(numero_secreto - chute)
    pontos -= pontos_perdidos
    

print('Fim do jogo')
print(f'Esse é o numero secreto {numero_secreto}')
 