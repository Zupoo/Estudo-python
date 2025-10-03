import random
user = input('Escolha Pedra Papel ou Tesoura').strip().upper()
pc = random.choice(['PEDRA', 'PAPEL', 'TESOURA'])
print(pc)

if user == 'PEDRA' and pc == 'PEDRA' or user == 'PAPEL' and pc == 'PAPEL' or user == 'TESOURA' and pc == 'TESOURA':
    print('Empate , voce escolheu {} e o computador tambem escolheu {}'.format(user, pc))
elif user == 'PEDRA' and pc == 'TESOURA' or user == 'PAPEL' and pc == 'PEDRA' or user == 'TESOURA' and pc == 'PAPEL':
    print('Voce ganhou , o computador escolheu {}'.format(pc))
else:
    print('Voce perdeu o computador escolheu {}'.format(pc))