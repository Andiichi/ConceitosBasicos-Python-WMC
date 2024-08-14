# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

horasGanhas = float(input('Digite seu ganho por hora: '))
horasTrab = float(input('Digite quantas horas trabalhou: '))

salarioMes = horasGanhas * horasTrab

print(f"\nGanhando R${horasGanhas:.2f} a hora, \ntendo trabalhado R${horasTrab} horas no mês, \nseu salário este mês é de R${salarioMes:.2f}.")