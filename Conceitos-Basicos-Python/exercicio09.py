# Solicite ao usuário o número de horas de exercício físico por semana. 
# Calcule o total de calorias queimadas em um mês, considerando uma média de 5 calorias por minuto de exercício.

exerc_horas = float(input('Digite quantas horas por semana você faz exercícios físico: '))

min_semanas = exerc_horas * 60

semanas_mes = 4

calorias_minuto = 5

total_calorias = min_semanas *  calorias_minuto * semanas_mes

print(f'O total de calorias queimadas em um mês é: {total_calorias:.2f} calorias')