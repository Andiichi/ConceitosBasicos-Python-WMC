# Solicite ao usuário o peso em kg e a altura em metros. Calcule e
# imprima o Índice de Massa Corporal (IMC) usando a fórmula:
# IMC = peso / (altura x altura).

print('~ IMC é a sigla para Índice de Massa Corpórea, parâmetro adotado pela Organização Mundial de Saúde para calcular o peso ideal de cada pessoa. ~ \n')
pesoKg = float(input('Digite seu peso corporal: '))
alturaMt = float(input('Digite a sua altura: '))

print('\nO índice é calculado da seguinte maneira: \nDivide-se o peso do paciente pela sua altura elevada ao quadrado. \nDiz-se que o indivíduo tem peso normal quando o resultado do IMC está entre 18,5 e 24,9.\n ')

imc = pesoKg / (alturaMt ** 2)


if imc <= 18.5:
    classIMC = 'Magreza'
elif  18.5 >= imc or imc <= 24.9:
    classIMC = 'Normal'
elif  25 >= imc or imc  <= 29.9:
    classIMC = 'Sobrepeso'
elif  30 >= imc or imc <= 34.9:
    classIMC = 'Obesidade grau I'
elif  35 >= imc or imc <= 39.9:
    classIMC = 'Obesidade grau II'
elif imc >= 40:
    classIMC = 'Obesidade grau III'
else:
    print("Valor inválido")

print(f'Seu IMC: {float(imc):.2f}')
print(f'Sua classificação é {classIMC}')

