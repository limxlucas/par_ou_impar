import random
numFinal = 0
resultado = ''
while True:
    numBot = random.randrange(0, 11)
    numUsuario = int(input("Digite um número "))
    escolhaUsuario = str(input("Par ou ímpar? [P/I] ")).strip().upper()[0]    
    numFinal = numBot + numUsuario
    if numFinal % 2 == 0:
        resultado = 'par'
    else:
        resultado = 'impar'
    if escolhaUsuario in 'Pp' and resultado == 'par' or escolhaUsuario in 'Ii' and resultado == 'impar':
        print(f"Você jogou {numUsuario} e o BOT jogou {numBot}, entao é {resultado}.")
        print("Você ganhou !")
    else:
        print(f"Você jogou {numUsuario} e o BOT jogou {numBot}, entao é {resultado}.")
        print("Você perdeu !")
        volta = str(input("Quer jogar novamente ?[S/N] ")).strip().upper()[0]
        if volta in 'Nn':
            print("Obrigado")
            break
