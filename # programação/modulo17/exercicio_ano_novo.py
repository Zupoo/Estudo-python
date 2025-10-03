import time
import locale
# for i in range(10, -1, -1):
#     print(i)
#     time.sleep(1)
# print('FELIZ ANO NOVO!!!')


locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
# teste = time.strftime('%A, %d de %m de %Y , %H:%M', hora_atual)
# print(teste)


ano_novo = 2025, 12, 31, 23, 59, 59, 0, 0, 0
virada_ano = time.mktime(ano_novo)
print(virada_ano)

while True:

    atual = time.localtime()
    hora_atual = time.mktime(atual)


    segundos_virada = virada_ano - hora_atual
    # minutos_virada = segundos_virada / 60
    # horas_virada = minutos_virada / 60
    # dias_virada = horas_virada / 24
    dias_virada = (((segundos_virada / 60) / 60) /24)

    dias = int(dias_virada)
    horas = (dias_virada - int(dias_virada)) * 24
    minutos = (horas - int(horas)) * 60
    segundos = (minutos - int(minutos)) * 60
    print(f'Faltam {int(dias_virada)} dias pra acabar o ano e {int(horas)} horas {int(minutos)} minutos {int(segundos)} segundos', end = '\r')
    time.sleep(0.1)
