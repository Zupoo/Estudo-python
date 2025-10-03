import datetime
anonasc = int(input('Em que ano voce nasceu? : '))
sexo = input('Digite H se voce for homem e M se for mulher').strip().upper()

if sexo == 'H':

    anoatual = datetime.date.today().year

    alistamento = anonasc + 18
    idade = anoatual - anonasc
    if alistamento < anoatual:
        print('Ja passou do tempo de se alistar')
        calc = anoatual - alistamento
        data = anoatual - calc
        print('Voce deveria ter se alistado ha {} anos atras'.format(calc))
        print('Voce deveria ter se alistado em {}'.format(data))
    elif anoatual == alistamento:
        print('Esta na idade de se alistar')
    else:
        calc = alistamento - anoatual
        data = anoatual + calc
        print('Voce ainda é muito novo pra se preocupar com isso , espere mais {} anos'.format(calc))
        print('Espere até {} para se alistar'.format(data))
else:
    print('Voce é mulher , nao precisa se preocupar com isso, moça!')