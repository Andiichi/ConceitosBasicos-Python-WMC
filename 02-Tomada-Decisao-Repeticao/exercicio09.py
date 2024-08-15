
# O programa deve calcular e apresentar a quantidade de números pares e ímpares inseridos. 
# O processo de leitura deve ser encerrado quando o usuário informar o valor zero. 

# Certifique-se de incluir validações para garantir que apenas números positivos sejam considerados na contagem e cálculos.

numero = 0
numero_par = 0
numero_impar = 0

while True:

    numero = int(input('\n ~ Digite um número: '))

    if numero != 0:
        if numero % 2 == 0:
            numero_par += 1
            print(f'\nEsse número é par!')
        else:
            numero_impar += 1
            print(f'\nEle é ímpar!')
    elif numero == 0:
        print(f'\nTotais de números pares: {numero_par} ')
        print(f'Totais de números impares: {numero_impar} ')
        break
    else:
        print('Valor invalido"!')
