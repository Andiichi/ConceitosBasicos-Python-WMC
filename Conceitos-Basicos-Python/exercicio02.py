# 2. Peça ao usuário para informar o ano de nascimento. Em seguida,calcule e imprima a idade atual.

nascimento = int(input('Insira o seu ano de nascimento: '))
anoAtual = 2024 #inserção do ano atual
idadeAtual = anoAtual - nascimento #calculo para a idade

print(f'\nSua idade atual é {idadeAtual} anos!')