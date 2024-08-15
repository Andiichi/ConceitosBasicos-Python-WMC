
#7.Desenvolver um programa que solicite 
# a idade do usuário 
# e identifique se ele é uma criança,um adolescente,adulto ou idoso.

while True:
    print('\n~ Bem vindos ao programa de idade~\n')

    try:
        idade = int(input('Digite sua idade: '))
        
        if idade <= 12 and idade > 0:
            print(f'\n~ Você é uma criança de {idade} anos! ~')
            break
        elif idade >= 13 and idade < 18:
            print(f'\n~ Você é um(a) adolescente de {idade} anos! ~')
            break
        elif idade >= 18 and idade < 65 :
            print(f'\n~ Você é um(a) adulto(a) de {idade} anos! ~')
            break
        elif idade >= 65 and idade < 110 :
            print(f'\n~ Você é um(a) idoso(a) de {idade} anos! ~')
            break  
        else:
            print(f'\nERRO: {idade}inválidos! Digite novamente')

    except Exception as e:
		    print ("[ERRO] %s" % (e),'- Digite um numero valido!!')
