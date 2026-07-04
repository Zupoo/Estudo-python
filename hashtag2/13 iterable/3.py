# set é tipo uma lista mas nao tem ordem ex meu_set[0] só q a vantagem dele é q
#  nao tem valores duplicados

# como criar um set
criando_um_set = {'este', 'é', 'é', 'um', 'um', 'um', 'set', 'repare que a ordem é aleatória mas nada se repete'}
print(criando_um_set)
animais_aquario = ['peixe palhaço', 'peixe palhaço', 'anemona', 'anemona', 'anemona', 'anemona',
                   'torch', 'torch', 'torch', 'hammer']


print(f"Tem {len(animais_aquario)} animais no aquario")


set_animais_aquario = set(animais_aquario)
print(f'Tem {len(set_animais_aquario)} espécies diferentes no aquario')
print(f'São eles {set_animais_aquario}')