
# Faça um programa que lê três números inteiros e os mostra em ordem crescente.

resposta_numero1 = int(input('Digite o 1º numero: '))
resposta_numero2 = int(input('Digite o 2º numero: '))
resposta_numero3 = int(input('Digite o 3º numero: '))

ordem_lista = [resposta_numero1, resposta_numero2, resposta_numero3]
ordem_lista.sort() #ordena em ordem crescente a lista

print(f'Lista em ordem crescente dos números inseridos é: [{ordem_lista[0]}] [{ordem_lista[1]}] [{ordem_lista[2]}]')
