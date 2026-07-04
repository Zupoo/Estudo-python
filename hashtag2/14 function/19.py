area_pintada = int(input('Quantos metros quadrados serao pintados? : '))
latas = 0
galao = 0
litros_necessarios = area_pintada/ 6
if litros_necessarios >= 18:
    latas = litros_necessarios/18
    if latas%1 != 0:
        latas = int(latas)
    litros_necessarios = litros_necessarios - (latas*18)
if litros_necessarios != 0:
    galao = litros_necessarios/ 3.6
    if galao%1 != 0:
        galao = int(galao)+1

custo_normal = (latas * 80) + (galao * 25)
custo_lata_extra = (latas + 1) * 80
if custo_normal < custo_lata_extra:
    print(f'Para pintar {area_pintada} m2 vai ser necessario {latas} latas e {galao} galao de tinta. Vai custar {custo_normal}RS')
else:
    print(f'Para pintar {area_pintada} m2 vai ser necessario {latas+1} latas e vai custar {custo_lata_extra}RS')    
print(latas, galao)        
print(custo_normal)
print(custo_lata_extra)
        
