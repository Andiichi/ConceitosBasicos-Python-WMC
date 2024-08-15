
# Criar um programa em Python que solicite três números ao usuário, utilize estruturas condicionais para determinar o maior entre eles e apresente o resultado.


print('Digite abaixo qual o comprimento dos três lados de um triângulo\n')

lado_um = int(input('Digite o 1ª lado do triangulo: '))
lado_dois= int(input('Digite o 2ª lado do triangulo: '))
lado_tres = int(input('Digite o 3ª lado do triangulo: '))


if lado_um == lado_dois == lado_tres:
    print('O triângulo é: Equilátero: todos os lados com o mesmo valor')

elif lado_um == lado_dois or lado_um == lado_tres or lado_dois == lado_tres:
    print('O triângulo é: Isósceles: dois lados com o mesmo valor')
    
else:
    print('O triângulo é: Escaleno: todos os lados com medidas distintas.')