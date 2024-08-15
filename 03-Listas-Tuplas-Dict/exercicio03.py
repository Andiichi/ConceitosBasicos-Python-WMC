# 3. Crie um dicionário representando um carrinho de compras.
# Adicione produtos (chaves) e quantidades (valores) ao carrinho.
# Calcule o total do carrinho de compra.

carrinhoCompras = {}
contador = 1
totalProd = 0

while True:
 
    produto = str(input(f'Digite o nome do {contador}º: ')).capitalize()
    qts = int(input(f'Digite a quantidade do {produto}: '))

    carrinhoCompras[produto] = qts

    resposta = str(input('\nQuer continuar cadastrando produtos?[Sim ou Não] ')).lower()

    contador += 1

    if resposta == 'sim' or resposta == 's': 
        continue
    elif resposta == 'nao' or resposta == 'n' or resposta == 'não':
        print(f'\nPRODUTO : QUANTIDADES')
        
        for chaves, valores in carrinhoCompras.items():
            print(f'- {chaves} : {valores} ')           
            
            totalProd += valores

    print(f'Total do carrinho: {totalProd}')

    break
        # import time

        # segundos = 10
        # for i in range(segundos):
        #     print(f"{(segundos - i):02d}", end="\r")
        #     time.sleep(1)

