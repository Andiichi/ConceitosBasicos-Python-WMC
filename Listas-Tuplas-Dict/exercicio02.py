# 2. Faça um Programa que peça as quatro notas de 5 alunos, calcule e armazene numa lista a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

lista_notas = []

print('~ Programa de calculo de média ~ ')


aluno = 1
notasAluno = {}

while aluno < 6:
    print(f'Aluno nº {aluno}: ')
    mediaNotas = []
    mediaAlunos = []

    for index in range(4):
        resposta = float(input(f'Digite a {index + 1}ª nota: '))
        mediaNotas.append(resposta)
        somaNotas = sum(mediaNotas)
        mediaAluno = somaNotas / len(mediaNotas)
        notasAluno[aluno] = mediaAluno
        index += 1
    

    aluno += 1
    

    if aluno == 6:
        break

mediaNotas2 = []

for alunos, notasMedias in notasAluno.items():
    if notasMedias >= 7:
        mediaNotas2 = notasMedias
        if notasMedias >= 7:
            print(f'O Aluno nº {alunos} teve média das notas acima de 7: {mediaNotas2}! Parabéns!')
        else: print('Nenhum aluno teve media acima de 7!')

