#Trabalho do Jokenpo
jogo = int(input("Bem vindo ao jogo, escolha 1 para jogar e 0 para sair"))
numero_de_jogos = 0
numero_de_empates = 0
numero_de_vitorias_jogador1 = 0
numero_de_vitorias_jogador2 = 0
numero_de_vitorias_computador1 = 0
numero_de_vitorias_computador2 = 0
while (jogo != 1 and jogo != 0):
    jogo = int(input("Escolha um valor entre 0 e 1"))
# loop infinito do modo de jogo
while jogo == 1:
    modo_de_jogo = int(input("Escolha o modo de jogo, digite 1 para jogador vs jogador , 2 para jogador vs computador, 3 para computador 1 vs computador 2"))  # 
type: int
    jogador_vs_jogador = 1
    jogador_vs_jogador_2 = 2
    jogador_2_vs_jogador_2 = 3
    while (modo_de_jogo != 1 and modo_de_jogo != 2 and modo_de_jogo != 3):
        modo_de_jogo = int(input("Escolha o modo de jogo, digite 1 para jogador vs jogador , 2 para jogador vs computador, 3 para computador 1 vs computador 2"))  # 
type: int
    # Modo jogador vs jogador
    if modo_de_jogo == 1:
        jogador_1 = int(input("Jogador_1, digite 0 para pedra, 1 para papel ou 2 para tesoura: "))
        jogador_2 = int(input("Jogador_2, digite 0 para pedra, 1 para papel ou 2 para tesoura: "))
        pedra = 0
        papel = 1
        tesoura = 2
        while (jogador_1 != 0 and jogador_1 != 1 and jogador_1 != 2):
            print("Digite um valor entre 0 e 2")
            jogador_1 = int(input("Jogador_1, digite 0 para pedra, 1 para papel ou 2 para tesoura: "))
        while (jogador_2 != 0 and jogador_2 != 1 and jogador_2 != 2):
            print("Digite um valor entre 0 e 2")
            jogador_2 = int(input("Jogador_2, digite 0 para pedra, 1 para papel ou 2 para tesoura: "))
        if (jogador_1 == jogador_2):
            print("Empate")
            numero_de_empates = numero_de_empates + 1
        elif ((jogador_1 == pedra and jogador_2 == tesoura) or (jogador_1 == papel and jogador_2 == pedra) or (jogador_1 == tesoura and jogador_2 == papel)):
            print("Jogador 1 ganhou")
            numero_de_vitorias_jogador1 = numero_de_vitorias_jogador1 + 1
        else:
            print("Jogador 2 ganhou")
            numero_de_vitorias_jogador2 = numero_de_vitorias_jogador2 + 1
    #Modo de jogo jogador_vs_jogador
    if modo_de_jogo == 2:
        from random import randint
        jogador_1 = int(input("Jogador_1, digite 0 para pedra, 1 para papel ou 2 para tesoura: "))
        computador_1 = randint(0, 2)
        pedra = 0
        papel = 1
        tesoura = 2
        print('O computador escolheu: ', computador_1)
        while (jogador_1 != 0 and jogador_1 != 1 and jogador_1 != 2):
            print("Digite um valor entre 0 e 2")
            jogador_1 = int(input("Jogador_1, digite 0 para pedra, 1 para papel ou 2 para tesoura: "))
            print('O computador escolheu: ', computador_1)
        if (jogador_1 == computador_1):
            print("Empate")
            numero_de_empates = numero_de_empates + 1
        elif ((jogador_1 == pedra and computador_1 == tesoura) or (jogador_1 == 
papel and computador_1  == pedra) or (jogador_1 == tesoura and computador_1 == 
papel)):
            print("Jogador 1 ganhou")
            numero_de_vitorias_jogador1 = numero_de_vitorias_jogador1 + 1
        else:
            print("computador_1 ganhou")
            numero_de_vitorias_computador1 = numero_de_vitorias_computador1 + 1
    #Modo de jogo computador vs computador
    if modo_de_jogo == 3:
        from random import randint
        computador_1 = randint(0, 2)
        computador_2 = randint(0, 2)
        pedra = 0
        papel = 1
        tesoura = 2
        print('O computador_1 escolheu:', computador_1)
        print('O computador_2 escolheu:', computador_2)
        if (computador_1 == computador_2):
            print("Empate")
            numero_de_empates = numero_de_empates + 1
        elif ((computador_1 == pedra and computador_2 == tesoura) or (computador_1 
== papel and computador_2  == pedra) or (computador_1 == tesoura and computador_2 
== papel)):
            print("Computador 1 ganhou")
            numero_de_vitorias_computador1 = numero_de_vitorias_computador1 + 1
        else:
            print("Computador 2 ganhou")
            numero_de_vitorias_computador2 = numero_de_vitorias_computador2 + 1
    numero_de_jogos = numero_de_jogos + 1
    print('Porcentagem de Vitorias do Jogador 1 :', 
numero_de_vitorias_jogador1/numero_de_jogos * 100,"%")
    print('Porcentagem de Vitorias do Jogador 2 :', numero_de_vitorias_jogador2 / 
numero_de_jogos * 100, "%")
    print('Porcentagem de Vitorias do Computador 1 :', 
numero_de_vitorias_computador1 / numero_de_jogos * 100, "%")
    print('Porcentagem de Vitorias do Computador 2 :', 
numero_de_vitorias_computador2 / numero_de_jogos * 100, "%")
    print('Total de número de jogos', numero_de_jogos)
    print('Total de empates dos jogos', numero_de_empates)
    jogo = int(input("Bom jogo, quer jogar novamente? escolha 1 para jogar e 0 para sair"))
    while (jogo != 1 and jogo != 0):
        jogo = int(input("escolher certo"))
    if jogo == 0:
        print('Saindo ...')
        print('Total de número de jogos', numero_de_jogos)
        break
