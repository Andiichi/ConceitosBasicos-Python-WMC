# Escreva um script que pergunta ao usuário se ele deseja converter uma temperatura de grau Celsius para Fahrenheit ou vice-versa. Para cada opção, crie uma função.

# Extra: Crie uma terceira, que é um menu para o usuário escolher a opção desejada, onde esse menu chama a função de conversão correta.


 # ums função loop para caso queira fazer nova conversão novamente
def loop_sim_ou_nao(resposta):
    while True:
        if resposta in ['sim', 's']:
            menu()

        elif resposta in ['nao', 'não', 'n']: #valida entre as opções com operador 'in'
            print('\nOk! Programa encerrado!')
            break

        else:
            print('\nErro! Digite sim ou não somente.')
    
    return resposta

# Função para converter Celsius para Fahrenheit
def celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Função para converter Fahrenheit para Celsius
def fahrenheit_para_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9 
    return celsius

# Função de menu que permite ao usuário escolher a conversão desejada
def menu():
    print("Escolha a opção de conversão:\n")
    print("1. Converter Celsius para Fahrenheit")
    print("2. Converter Fahrenheit para Celsius")
    print("3. Sair do programa")
    
    opcao = int(input("Digite uma opção acima: "))

    if opcao == 1:
        celsius = float(input("Digite a temperatura em Celsius: "))
        resultado = celsius_para_fahrenheit(celsius)
        print(f"\nResposta = {celsius}°C [Celsius] é igual a {resultado}°F [Fahrenheit].")
    elif opcao == 2:
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        resultado = fahrenheit_para_celsius(fahrenheit)
        print(f"\nResposta = {fahrenheit}°F [Fahrenheit] é igual a {resultado}°C [Celsius].")
    elif opcao == 3:
        print('\nOk! Programa encerrado!')
        exit
        
    else:
        print("Opção inválida! Tente novamente.")

    if opcao != 3:
        loop_sim_ou_nao(resposta = input('\nDeseja realizar uma nova conversão [S/N]: ').lower())
    

# Executa o menu para o usuário escolher
menu()
