# 3. Faça um Programa que peça a quantidade de quilômetros, transforme em metros, centímetros e milímetros.

quantidade = float(input('Digite a quantidade em Quilômetros: '))

#faz o calculo do metro, centimetro e milimetro
metro = quantidade * 1000
centimetro = quantidade * 100000
milimetro = metro * 1000

print(f'\n{quantidade} km é equivale a:')
print(f'METRO: {round(metro)} m')
print(f'CENTÍMETROS: {round(centimetro)} cm')
print(f'MILÍMETROS: {round(milimetro)} mm')