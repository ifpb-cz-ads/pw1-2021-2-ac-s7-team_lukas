estoque = {'tomate': [1000, 2.30],
            'alface': [500, 0.45],
            'batata': [2001, 1.20],
            'feijão': [100, 1.50]
            }


total = 0

while True:
    produto = input('Digite o nome do produto ou fim para sair: ')
    if produto == 'fim':
        break
    if produto in estoque:
        quant = int(input('Quantidade:'))    
        if quant <= estoque[produto][0]:
            preco = estoque[produto][1]
            custo = preco * quant
            print(f'{produto:12s}:{quant:3d} x {preco:6.2f} = {custo:6.2f}')
            estoque[produto][0] -= quant
            total += custo
        else:
            print('Quantidade solicitada não disponivel')
    else:
        print('O produto não consta no estoqueue')

print(f'Custo total das compras ficou em:{total:21.2f} <--\n')
print('estoqueue restante:\n')
for chave, dados in estoque.items():
    print('Descrição: ', chave)
    print('Quantidade: ', dados[0])
    print(f'Preço:{dados[1]:6.2f}\n')