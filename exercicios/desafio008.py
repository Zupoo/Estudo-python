m = float(input('Digite uma medida em metros para ser convertida : '))
cm = m * 100
mm = cm * 10

print('{} metros equivale a {:.0f} centimetros e {:.0f} milimetros'.format(m, cm, mm))