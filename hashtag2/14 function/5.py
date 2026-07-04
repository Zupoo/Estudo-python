# passar mais de 1 argumento
produtos = ['beb46275','TFA23962','TFA64715','TFA69555','TFA56743','BSA45510','TFA44968','CAR75448','CAR23596','CAR13490','BEB21365','BEB31623','BSA62419','BEB73344','TFA20079','BEB80694','BSA11769','BEB19495','TFA14792','TFA78043','BSA33484','BEB97471','BEB62362','TFA27311','TFA17715','BEB85146','BEB48898','BEB79496','CAR38417','TFA19947','TFA58799','CAR94811','BSA59251','BEB15385','BEB24213','BEB56262','BSA96915','CAR53454','BEB75073']

def verificar_categoria (produto, cod_categoria):
    if cod_categoria.upper() in produto.upper():
        return True
    else:
        return False
codigo = input('Qual codigo do produto que voce esta procurando? ')
for produto in produtos:
    if verificar_categoria(produto= produto, cod_categoria = codigo):
        print(f'Codigo {codigo} encontrado no produto {produto}')   


# tb pode passar o parametro pra função por nome (keyword argument)
# em vez dele pegar em sequencia ele vai colocar cada 1 no seu por exemplo:
# def verificar_categoria (produto, cod_categoria):
#pra passar por posição é só fazer normal:   verificar_categoria(produto, codigo):
# pra passar por argumento : verificar_categoria(produto = produto, cod_categoria= codigo):
