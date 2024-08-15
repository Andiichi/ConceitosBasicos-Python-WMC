# 4. Receba do usuário a quantidade de litros de combustível consumidos e
# a distância percorrida. Calcule e imprima o consumo médio em km/l.

distanciaPercorrida = float(input('Digite a distância percorrida: '))
Litrosombustível = float(input('Digite a quantidade de litros de combustível consumidos: '))

#calculo para saber o consumo medio por litro
consumoVeiculo = distanciaPercorrida / Litrosombustível

print(f'O consumo médio em km/l: {consumoVeiculo}')