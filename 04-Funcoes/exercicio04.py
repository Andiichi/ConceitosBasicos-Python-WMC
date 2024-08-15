# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira, e calcule quanto poderia comprar de cada moeda estrangeira.

# Considere a tabela de conversão abaixo:
# Dólar Americano: R$ 4,91
# Peso Argentino: R$ 0,02
# Dólar Australiano: R$ 3,18
# Dólar Canadense: R$ 3,64
# Franco Suíço: R$ 0,42
# Euro: R$ 5,36
# Libra esterlina: R$ 6,21

def loop_sim_ou_nao():
    while True:
        resposta = input('\nDeseja realizar uma nova conversão [S/N]: ').strip().lower() #retira os espaços e deixa em minuscula
        if resposta in ['sim', 's']:
            menu_converter_dinheiro()
        elif resposta in ['nao', 'não', 'n']:
            print('\nOk! Programa encerrado!')
            break
        else:
            print('\nErro! Digite "sim" ou "não" apenas.')

def converter_dinheiro(valor_reais):
    taxas_conversao = {
        "Dólar Americano": 4.91,
        "Peso Argentino": 0.02,
        "Dólar Australiano": 3.18,
        "Dólar Canadense": 3.64,
        "Franco Suíço": 0.42,
        "Euro": 5.36,
        "Libra Esterlina": 6.21
    }

    print(f"\nVocê tem R$ {valor_reais:.2f} na carteira.\n")
    for moeda, taxa in taxas_conversao.items():
        valor_convertido = valor_reais / taxa
        print(f"Você pode comprar [{valor_convertido:.2f}] {moeda}(s).")

def menu_converter_dinheiro():
    try:
        dinheiro = float(input("\nQuanto dinheiro você tem na carteira? R$ ").strip())
        converter_dinheiro(dinheiro)
    except ValueError:
        print("\nErro! Por favor, digite um valor numérico válido.")
        menu_converter_dinheiro()
    
    loop_sim_ou_nao()

# Chamada do menu
print('Olá! Bem-vindo(a)!\n')
menu_converter_dinheiro()
