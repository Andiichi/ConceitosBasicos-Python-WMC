#6.Crie um programa que solicite ao usuário um login e uma senha.
# O programa deve permitir o acesso apenas se o  usuário for "admin" e a senha for "admin123",
# caso contrário imprima uma mensagem de erro.

while True:
    print('\n~ Bem vindos ao programa de Login ~\n')

    login = str(input('Digite o seu login: ')).lower()
    senha = str(input('\nDigite a sua senha: ')).lower()

    if login == 'admin' and senha == 'admin123':
        print(f'\n~ LOGIN FEITO COM SUCESSO ~')
        break
    else:
        print(f'\nERRO: {login} e {senha} inválidos! Digite novamente')
        

