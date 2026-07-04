rendimento = 6
galao18 = 80
galao18_litro = 18
lata3 = 25
lata3_litro = 3.6

def area_a_ser_pintada():
    area = int(input("Informe área total em m² "))
    return area
def calcular_litros_tinta(area):
    litros = area / rendimento
    return litros
# ---------------------------------------------------
def galoes_latas_litros (litros) :
    galoes = 0
    galoes_inteiros = litros // galao18_litro
    if galoes_inteiros > 0 :
        galoes = galoes_inteiros 
    latas = 0     
    litros_restante = litros % galao18_litro
    litro_lata = (lata3 / lata3_litro) * litros_restante    
    if litro_lata < galao18 :
        dif_latas = litros_restante // lata3_litro
        latas = latas + dif_latas
        residuo_lata = dif_latas % lata3_litro
        if residuo_lata > 0 :
            latas += 1
    else:
        galoes += 1 
    return galoes, latas
# ---------------------------------------------------
def calcular_custo(galoes, latas):
    custo_g = galoes * galao18
    custo_l = latas * lata3
    custo = custo_l + custo_g
    return custo

area = area_a_ser_pintada()
litros = calcular_litros_tinta(area)
galoes, latas = galoes_latas_litros(litros)
custo = calcular_custo(galoes, latas)

print('-'*21, 'Total Área, Litros e Custo', '-'*21)
print()
print('A área de printura: {} m² e será utilizado: {:.2f} litros de tinta. '.format(area,litros))
print('Galões necessários: {} e complemento com Latas: {} de tinta. '.format(round(galoes),round(latas)))
print()
print(f'Com um Custo total de R$: {custo:.2f}')