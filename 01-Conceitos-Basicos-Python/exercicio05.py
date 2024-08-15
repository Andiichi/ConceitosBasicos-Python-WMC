#10. Escreva um programa que calcule o salário líquido.
# Lembrando de declarar o salário bruto e o percentual de desconto do Imposto de Renda.

# ●Renda até R$1.903,98:
## isento de imposto de renda; 
# ●Renda entre R$1.903,99 e R$2.826,65:
# ## alíquota de 7,5%;
# ●Renda entre R$2.826,66 e R$3.751,05:
# ## alíquota de 15%;
# ●Renda entre R$3.751,06 e R$4.664,68:
# ## alíquota de 22,5%;
# ●Renda acima de R$4.664,68:
## alíquota máxima de 27,5%.


while True:
    print('\n~ Bem vindos ao programa de calculo do salário líquido ~')

    try:
        result = float(input('\nDigite o seu salário bruto [ou digite 0[zero] para sair]: '))

        if result != 0:
            if result <= 1903.98:
                print(f'Seu salário líquido é R$ {result}: isento de imposto de renda')
                
            elif result >= 1903.98 and result <= 2826.60:
                salario_liq = result - (result * 7.5 / 100)
                print('\nSeu salario bruto digitado: {:.2f}' .format(result))
                print('Seu salário líquido é R$ {:.2f}: alíquota de 7,5%;'.format(salario_liq))
                
            elif result >= 2826.66 and result <= 3751.05:
                salario_liq = result - (result * 15.0 / 100)
                print('\nSeu salario bruto digitado: {:.2f}' .format(result))
                print(f'Seu salário líquido é R$ {salario_liq}: alíquota de 15%;')
                
            elif result >= 3751.06 and result <= 4664.68:
                salario_liq = result - (result * 22.50 / 100)
                print('\nSeu salario bruto digitado: {:.2f}' .format(result))
                print(f'Seu salário líquido é R$ {salario_liq}: alíquota de 22,5%;')
            
            elif result > 4664.68:
                salario_liq = result - (result * 27.50/ 100)
                print('\nSeu salario bruto digitado: {:.2f}' .format(result))
                print(f'Seu salário líquido é R$ {salario_liq}: alíquota de 27,5%;')
        
        else:
            print('saindo...')
            break
        
    except Exception as e:
		    print ("[ERRO] %s" % (e),'- Digite um numero!!')
