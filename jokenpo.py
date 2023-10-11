import random
'''
Jogo de Pedra, Papel e tesoura
'''

opcoes = ['Pedra','Papel','Tesoura']

 
while True:
    minha_opcao = int(input('0 - Pedra\n1 - Papel\n2 - Tesoura\nEscolha uma numero dessas opções:'))
    computador = random.choice(opcoes)

    if minha_opcao < 0 or minha_opcao > 2:
        print('Não existe essa opcoes, escolha novamente.')
    else:
        print('existe')
        if minha_opcao == 0:
            minha_opcao == opcoes[0]
        elif minha_opcao == 1:       
            minha_opcao == opcoes[1]
        elif minha_opcao == 2:       
            minha_opcao == opcoes[2] 
        print(f'Você Escolheu {minha_opcao} e o computador:{computador}')
        empate = minha_opcao == 0 and computador == opcoes[0] or minha_opcao == 1 and computador == opcoes[1] or minha_opcao == 2 and computador == opcoes[2]
        if empate:
            print('Empate!!')
            break
        else:
            print('continue')

        