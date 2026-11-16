vendas = []
resultado = []

item1 = {
    "nome": "ooga_booga",
    "quantidade": 18,
    "data": "2026-10-30"
}
item2 = {
    "nome": "nice",
    "quantidade": 69,
    "data": "2026-10-31"
}
item3 = {
    "nome": "ᓚᘏᗢ",
    "quantidade": 21,
    "data": "2026-1-14"
}
item4 = {
    "nome": "[hyperlink_blocked]",
    "quantidade": 39,
    "data": "2026-10-31"
}
vendas.append([item1, item2]) #venda1
vendas.append([item3, item4]) #venda2

def media_venda(venda):
    soma = 0
    for item in venda:
        soma += item['quantidade']

    return soma / len(venda)

def classifi_venda():
    for venda in vendas:
        media = media_venda(venda)
        if media >= 30:
            print(f"\nProduto: {venda[0]['nome']}")
            print(f"média: {media}")
            desempenho = "alto"
            print(f"desempenho de venda {desempenho}")
            resultado.append([venda[0]['nome'], media, desempenho])
        elif media >= 10:
            print(f"\nProduto: {venda[0]['nome']}")
            print(f"média: {media}")
            desempenho = "médio"
            print(f"desempenho de venda {desempenho}")
            resultado.append([venda[0]['nome'], media, desempenho])
        else:
            print(f"\nProduto: {venda[0]['nome']}")
            print(f"média: {media}")
            desempenho = "baixo"
            print(f"desempenho de venda {desempenho}")
            resultado.append([venda[0]['nome'], media, desempenho])

            