from ex02_BancoDelas import *


if __name__ == "__main__":
    
    # Exemplo de uso, chamada da função de outro arquivo importado
    conta_corrente = ContaCorrente()
    conta_corrente.alterar_nome()
    conta_corrente.alterar_telefone()
    conta_corrente.alterar_renda_mensal() #ex. 2000
    conta_corrente.alterar_sexo()

    print()
    print(conta_corrente)
    print()
    # Realizando operações de depósito e saque
    conta_corrente.depositar(1000.0)
    # conta_corrente.sacar(1500.0)
    conta_corrente.sacar(1500.0)  # Testando saque além do saldo disponível

    print()
    print(conta_corrente)