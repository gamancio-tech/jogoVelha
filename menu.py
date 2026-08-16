import random

velha = (["","",""] for _ in range(3))

print("Bem vindo ao jogo da velha do Petreis Pitão Edition: \n")
iniciar = input("Iniciar Jogo? (S/N): ")

if iniciar == "N" or iniciar == "n":
    print("Até a próxima!")
    exit()
else:
    nomeUm = input("Insira o nome do jogador Um: ")
    nomeDois = input("Insira o nome do jogador Dois: ")
    escolher = input(f"{nomeUm}, Deseja escolher entre X e O? (S/N): ").lower()
    if escolher == 's':
        jogadorUm = str(input("Escolha entre X e O: ")).lower()
        while (jogadorUm not in ['x', 'o']):
            jogadorUm = input("Escolha inválida, por favor escolha entre X e O: ")
        jogadorDois = ' '
        if jogadorUm == "x":
            jogadorDois = 'o'
        else:
            jogadorUm = 'o'
            jogadorDois = 'x'
    else:
        print("X e O serão escolhidos aleatoriamente: ")
        sorteio = random.choice(['x', 'o'])
        if sorteio == 'x':
            jogadorUm = 'x'
            jogadorDois = 'o'
        else:
            jogadorUm = 'o'
            jogadorDois = 'x'    
print("O jogador um é: ", jogadorUm)
print("O jogador dois é: ", jogadorDois)