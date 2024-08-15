
# Implemente um programa que classifique um aluno com base em sua  pontuação em um exame. 
# O programa deverá solicitar uma nota de 0 a 10.
#  Se a pontuação for maior ou igual a 7, o aluno é aprovado; caso contrário, é reprovado.

nota_aluno = float(input('Digite uma nota entre 0[zero] a 10[Dez]: '))

if nota_aluno >= 7:
    print(f'Parabéns! Sua nota foi {round(nota_aluno)}. Aprovado!')
else:
    print(f'Sua nota foi {round(nota_aluno)}. Reprovado!')
