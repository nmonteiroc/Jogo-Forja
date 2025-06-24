from personagem import Personagem
from inimigo import Inimigo

def jogo_de_turnos():
    print("Bem-vindo ao jogo de turnos!")
    print("Você é o herói lutando contra o Grande Monstro!")

    heroi = Personagem('Herói', 100, 50)
    monstro = Inimigo('Grande Monstro', 80, 40)

    while heroi.vida > 0 and monstro.vida > 0:
        print('\n--- Turno do Jogador ---')
        print('Escolha uma ação:')
        print('1. Atacar')
        print('2. Defender')
        print('3. Usar habilidade especial')
        escolha = input('Digite o número da ação:')
        
        if escolha == '1':
            dano = heroi.atacar()
            monstro.receber_dano(dano)
        elif escolha == '2':
            heroi.defender()
        elif escolha == '3':
            dano = heroi.usar_habilidade_especial()
            monstro.receber_dano(dano)
        else:
            print('Ação inválida! Você perdeu a vez.')
            
        if monstro.vida <= 0:
            print ('Você derrotou o Grande Monstro! Parabéns!')
            break
        
        print('\n--- Turno do Inimigo ---')
        acao_inimigo = monstro.agir()
        if acao_inimigo == 'atacar':
            dano = monstro.atacar()
            heroi.receber_dano(dano)
        elif acao_inimigo == 'defender':
            monstro.defender()
            
    print('\n--- Fim de Jogo ---')
    if heroi.vida> 0:
        print(f'Parabéns, {heroi.nome} veceu!')
    else:
        print(f'{monstro.nome} venceu a batalha! Tente novamente')
    
