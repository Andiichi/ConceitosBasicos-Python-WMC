
# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
#  Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

resposta = str(input('Digite qual turno você está [M-matutino ou V-Vespertino ou N-Noturno]: ')).lower()

if resposta == 'm' or resposta == 'matutino':
    print("Bom Dia!")
elif resposta == 'vespertino' or  resposta == 'v':
    print("Boa Tarde!")

elif resposta == 'noturno' or resposta == 'n':
    print("Boa Noite!")
else:
    print("Valor Inválido!")


