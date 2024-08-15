# Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

soma_resposta = []

def soma(resposta): 
    return soma_resposta.append(resposta)


print('~ Somatório de números ~ ')
for index in range(5):
    soma(resposta = int(input(f'Digite o {index+1}º: ')))


print(f'A soma dos números é:', sum(soma_resposta))