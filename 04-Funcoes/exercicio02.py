# Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

def reverso(numero):
    numero_string = str(numero)
    #join é um metodo 
    numero_reverse =  ''.join(reversed(numero_string)) #função com recursividade
    return f'o número foi: {numero_reverse}'



resposta = int(input('Digite o número para inverter: '))

print(reverso(resposta))