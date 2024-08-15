
# Faça um programa que peça uma nota, entre zero e dez. 
# Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.


while True:
    resposta = int(input('Digite um numero entre 0 [zero] a 10 [dez]:'))
    
    if resposta >= 0 and resposta <= 10:
        print(f'Digitou um numero valido! Digitou: {resposta}')
        break
    else:
        print('Digite um numero valido!')
        