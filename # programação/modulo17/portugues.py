import locale
import datetime
# Definir a localização para português.
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
dia_semana = datetime.datetime.now().strftime('%A')
print(dia_semana)