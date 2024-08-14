# Escreva um programa que calcule o tempo de uma viagem. 
# Faça um comparativo do mesmo percurso de avião, carro e ônibus.
# Levando em consideração:
# ● avião = 600 km/h
# ● carro = 100 km/h
# ● ônibus = 80 km/h

distancia = float(input("Digite a distância da viagem em quilômetros: "))

velocidade_aviao = 600
velocidade_carro = 100
velocidade_onibus = 80

tempo_aviao = distancia / velocidade_aviao
tempo_carro = distancia / velocidade_carro
tempo_onibus = distancia / velocidade_onibus

# Exibir os resultados
print(f"Tempo de viagem de avião: {tempo_aviao:.2f} horas")
print(f"Tempo de viagem de carro: {tempo_carro:.2f} horas")
print(f"Tempo de viagem de ônibus: {tempo_onibus:.2f} horas")