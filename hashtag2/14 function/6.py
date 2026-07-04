def carga_tributaria (preco, custo, lucro):
    imposto = preco - (custo + lucro)
    carga = (imposto/ preco) * 100
    return carga
print(carga_tributaria(1500, 400, 800))