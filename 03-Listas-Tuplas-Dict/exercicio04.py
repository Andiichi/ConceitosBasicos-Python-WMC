
# 4. Crie um dicionário representando contatos (nome, telefone).
# Permita ao usuário procurar por um contato pelo nome.


agenda = {}

while True:
    nome = str(input('Digite o nome do contato: ')).capitalize()
    contato = str(input(f'Digite o numero da {nome}: '))

    print(f'Contato: {nome}')
    print(f'Telefone: {contato}')

    agenda[nome] = contato

    resposta = input('Deseja adicionar mais contatos?').lower()

    if resposta == 'sim' or resposta == 's': 
        continue

    elif resposta == 'nao' or resposta == 'n' or resposta == 'não':

        pesquisa = str(input('Deseja pesquisar um contato? Ou exibir todos?[SIM ou "EXIBIR TODOS"]: ')).lower()

        if pesquisa == 'sim': 
            procura = str(input('Qual contato deseja procurar? ')).capitalize()
        
            for chaves, valores in agenda.items():
                if chaves == procura:
                    print(f'{chaves}: {valores}')
                    break
                else:
                    print('Não existe {chaves}cadastrado')
                    continue

        elif pesquisa == 'exibir' or pesquisa == 'exibir todos':
            for chaves, valores in agenda.items():
                    print(f'{chaves}: {valores}')
            break
        else: 
            print('Digite SIM ou EXIBIR TODOS!')
            continue





