# Vamos construir um jogo de forca. 
# O programa escolherá aleatoriamente uma palavra secreta de uma lista predefinida. 
# A palavra secreta será representada por espaços em branco, um para cada letra da palavra. 
# O jogador terá um número limitado de 6 tentativas. Em cada tentativa, o jogador pode fornecer uma letra. 
# Se a letra estiver presente na palavra secreta, ela será revelada nas posições correspondentes. 
# Se a letra não estiver na palavra, uma mensagem de erro deverá ser informada. 
# Após um número máximo de erros, o jogador perde. 
# O jogo continua até que o jogador adivinhe a palavra ou exceda o número máximo de tentativas.

# Dica: Você precisará importar uma biblioteca para resolver esse exercício.

import random


palavras_secretas = ['amarelo', 'profissão', 'besouro', 'python']


def hangman_game():
    word = random.choice(palavras_secretas)

    fork = " ".join([("_" if letter not in (" ", "-") else letter) for letter in word]) #fork é a palavra secreta escolhida
    indexs = " ".join([letter for letter in word]) #indexs faz a busca da posicao da letra, que usa a posicao buscada para realizar a substituição.
    anwser = " ".join([letter for letter in word]) #pega tudo que esta em uma list em uma string, e coloca o espaço entra as letras

    print(fork)
    # print(anwser) #debugg

    fork = fork.split(" ")
    indexs = indexs.split(" ")
    anwser = anwser.split(" ")

    attempts, limit = 0, 6

    while attempts < 6:

        if fork == anwser: #verificação se ja acertou a palavra
            print("end game You winner"); break

        letter = input("write your one letter: ") #entrada de uma letra do usuario
          
        #verifique se a letra está dentro da palavra e se o limite de tentativas não execedeu caso tudo ok entra no if
        if letter in indexs and attempts < limit: #verifica se a letra esta dentro dos  indexs 
      
            exchange = indexs.count(letter) #exchange faz contagem de quantas letras daquela inserida pelo usuario tem na palavra
            
            
            for _ in range(exchange): #percorre um range x para verificar quantas letras estao na palavra 
                index = indexs.index(letter) #vai pegar o index da letra e substituir
                fork[index] = letter #fork na posicao do index é igual a letra
                indexs[index] = "_" #e vai trocar o _ pela letra encontrada dentro da palavra

            print(" ".join(fork)) #mostra como esta a palavra secreta apos acerto do usuario

        elif letter not in indexs: #é para verificar se teve entrada de letras repetidas, fazendo a
            attempts += 1

        elif letter not in anwser: #se errar a letra dentro da correta, diminuir a tentativas, que é limitada a 6
            attempts += 1

    if attempts >= limit:
        print("You lose")

hangman_game()