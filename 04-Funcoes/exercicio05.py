# Crie uma função chamada contar_vogais que recebe uma string como parâmetro. 
# Implemente a lógica para contar o número de vogais na string e retorne o total de vogais. 
# Solicite ao usuário para inserir uma frase e utilize a função para contar as vogais.

def contar_vogais(frase):
    vogais = "aeiouAEIOU"
    frase_destacada = ""
    contador = 0

    for letra in frase:
        if letra in vogais:
            frase_destacada += f"[{letra.upper()}]"
            contador += 1
        else:
            frase_destacada += letra

    return contador, frase_destacada

# Solicita ao usuário para inserir uma frase
frase = input("Digite uma frase: ")

# Conta o número de vogais e obtém a frase com as vogais destacadas
total_vogais, frase_destacada = contar_vogais(frase)

# Exibe o resultado
print(f"A frase contém {total_vogais} vogais: {frase_destacada}\n")


